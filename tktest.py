
from tkinter import *
#import tkFont
import tkinter.font
import socket
import threading
import time
import sys
import webbrowser

caiji= ["未采","已采"]
class ClientUI():
    Falg = False
    count = 0
    # from the Pi！
    is_Collect = []
    # from the Pi！
    Depth_Collect = []
    # from the 传感器！
    Parameter = []
    # from the client ! PC Connection P U M
    Status_Now = []


    # from the client ! PC WASD B
    Action = []
    # from the Key_Input!
    Status_Need = []

    SendMsg = ""
    title = '水下作业机器人操作界面！'
    local = 'localhost'
    port = 8808
    global clientSock
    flag = False

    def __init__(self):
        print("Start Now! ")
        for i in range(4):
            self.Status_Now.append(0)
        for i in range(3):
            self.Parameter.append(0)
        for i in range(10):
            self.is_Collect.append(0)
        for i in range(10):
            self.Depth_Collect.append(0)

        for i in range(5):
            self.Action.append(0)
        for i in range(3):
            self.Status_Need.append(0)

        self.root = Tk()
        self.root.title(self.title)
        self.root.bind('<Key>',self.key)
        #总窗口，所有的部件都挂在这上面
        self.GUI = Frame(self.root)

        #窗口面板, 用7个面板布局
        self.frame = [Frame(self.GUI), Frame(self.GUI) ,Frame(self.GUI),Frame(self.GUI), Frame(self.GUI), Frame(self.GUI),Frame(self.GUI)]
        # 监听键盘！

        #最上方的两个按钮！
        self.bt1 = Button(self.frame[0],text = "自动",command = self.ButtonEventAuto, width=15, height=3, bg="red",fg = "black")
        self.bt1.grid(row = 1, column = 1)
        self.bt2 = Button(self.frame[0],text = "手动",command = self.BottonEventHand, width=15, height=3, bg="black",fg = "black")
        self.bt2.grid(row = 1, column = 2)
        self.frame[0].pack()

        # 采水情况 和 采水深度 两个10元素列表的Label ！
        self.label1 = Label(self.frame[1],text = "采水情况", width=15, height=3, bg="pink",fg = "red")
        self.label1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.label2 = Label(self.frame[1],text = "采水深度", width=15, height=3, bg="pink",fg = "red")
        self.label2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.frame[1].pack()

        self.Label_of_Collect = []
        self.var1 = []
        for i in range(10):
            self.var1.append(StringVar())
            self.Label_of_Collect.append(Label(self.frame[2], textvariable = self.var1[i], width=15, height=2,bg = "black", fg = "blue"))
            self.Label_of_Collect[i].grid(row = i+1,column = 1)

        self.Label_of_Depth = []
        self.var2 = []
        for i in range(10):
            self.var2.append(StringVar())
            self.Label_of_Depth.append(Label(self.frame[2], textvariable = self.var2[i], width=15, height=2,bg = "black",fg = "blue"))
            self.Label_of_Depth[i].grid(row = i+1,column = 2)
        self.UpdateVarDepth()
        self.frame[2].pack()

        # 三个参数的名字显示的Label ！
        self.label3 = Label(self.frame[3],text = "Temp", width=10, height=3, bg="pink",fg = "red")
        self.label3.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label4 = Label(self.frame[3],text = "Depth", width=10, height=3, bg="pink",fg = "red")
        self.label4.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label5 = Label(self.frame[3],text = "Depth", width=10, height=3, bg="pink",fg = "red")
        self.label5.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.frame[3].pack()

        #三个参数的数值显示的Label
        self.Label_of_Parameter = []
        self.var3 = []
        for i in range(3):
            self.var3.append(StringVar())
            self.Label_of_Parameter.append(Label(self.frame[4], textvariable = self.var3[i], width=10, height=2,bg = "white", fg = "blue"))
            self.Label_of_Parameter[i].grid(row = 1,column = i+1)
        self.UpdateParmeter()
        self.frame[4].pack()

        # 三个状态的的名字的Label ！
        self.label6 = Label(self.frame[5],text = "Connection？", width=10, height=3, bg="pink",fg = "red")
        self.label6.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label7 = Label(self.frame[5],text = "采泥启动？", width=10, height=3, bg="pink",fg = "red")
        self.label7.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label8 = Label(self.frame[5],text = "探照灯？", width=10, height=3, bg="pink",fg = "red")
        self.label8.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.frame[5].pack()


        self.light = Canvas(self.frame[6], bg = "white", height = 60, width = 270)
        # self.label9 = Label(self.frame[6],image = self.image1, width=20, height=3, bg="pink",fg = "red")        
        for i in range(3):
            self.light.create_oval(25+90*i, 10, 65+90*i, 50, fill = "red")
        # self.label9.pack(fill=tkinter.BOTH)
        self.light.pack()
        self.frame[6].pack()
        self.GUI.pack(side = tkinter.RIGHT)
        


     
    def UpdateVarDepth(self):
        for i in range(10):
            self.var1[i].set(caiji[self.is_Collect[i]])   

        for i in range(10):
            self.var2[i].set(str(self.Depth_Collect[i]))   
            if self.is_Collect[i]==1:
                self.Label_of_Collect[i]['bg']="white"
                self.Label_of_Depth[i]['bg']="white"
            elif self.is_Collect[i]==0:
                self.Label_of_Collect[i]['bg']="black"
                self.Label_of_Depth[i]['bg']="black"

    def UpdateParmeter(self):
        for i in range(3):
            self.var3[i].set(str(self.Parameter[i]))

    def UpdateStatus(self):
        for i in range(3):
            if self.Status_Now[i] == 1:
                self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="green")
            if self.Status_Now[i] == 0:
                self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="red")


    #启动线程接收服务器端的消息
    def startNewThread(self):
        #启动一个新线程来接收服务器端的消息
        #thread.start_new_thread(function, args[, kwargs])函数原型，
        #其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        #receiveMessage函数不需要参数，就传一个空元组
        #thread.start_new_thread(self.receiveMessage, ())
        t = threading.Thread(target=self.test, args=())
        t.start()

    def ButtonEventAuto(self):
        print("You have Changed The Way of Control to Automatic!")
        self.Status_Need[0]=1
        self.bt1['fg']="red"
        self.bt2['fg']="black"

    def BottonEventHand(self):
        print("You have Changed The Way of Control to Handle!")
        self.Status_Need[0]=0
        self.bt2['fg']="red"
        self.bt1['fg']="black"

    #关闭消息窗口并退出
    def close(self):
        self.ThreadStop = True
        self.Flag = True
        time.sleep(2)
        sys.exit()

    def test(self):
        count = 0 
        while True:
            print("I am in the Thread!")
            self.is_Collect[count%10]= (self.is_Collect[count%10]+1)%2
            count=count+1
            if count>100:
                count=0
            self.Depth_Collect[count%10] = count%6
            self.Parameter[count%3]=count
            self.Status_Now[count%3+1]=count%2
            self.UpdateVarDepth()
            self.UpdateParmeter()
            self.UpdateStatus()
            time.sleep(0.2)
            if self.Flag:
                break

    def key(self, event):
        print('event.char = ',event.char)
        print('event.keycode = ',event.keycode)
        if event.keycode == 3473435:
            sys.exit()

client = ClientUI()
client.startNewThread()
client.root.mainloop()
