# _*_ coding:utf-8 _*_
# Filename:GUIClient.py
# 水下作业机器人树莓派客户端

from tkinter import *
# import tkFont
import tkinter.font
import socket
import threading
import time
import sys
import inspect
import ctypes
import webbrowser
from tkinter.messagebox import askyesno


caiji = ["未采", "已采"]
Flag = False

def stop_thread(thread):
    res = 1
    while res != 0:
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
        sys.exit()



class ClientUI(Frame):
    Record = False

    count = 0
    # from the Pi！
    is_Collect = []
    # from the Pi！
    Depth_Collect = []
    # from the 传感器！
    Parameter = []
    # from the client ! PC Connection P M B
    Status_Now = []

    # from the client ! PC WASD B
    Action = []
    # from the Key_Input!
    Status_Need = []

    SendMsg = ""

    title = '水下作业机器人操作界面！'
    local = ''
    port = 8808
    global clientSock
    flag = False

    # 初始化类的相关属性，类似于Java的构造方法

    def __init__(self,root=None):
        self.root=root
        super().__init__(root)
        for i in range(3):
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
        self.root.title(self.title)
        # 监听键盘！
        self.root.bind('<Key>',self.Key_Input)
        # 总窗口，所有的部件都挂在这上面
        self.GUI = Frame(self.root)
        # 窗口面板, 用7个面板布局
        self.frame = [Frame(self.GUI), Frame(self.GUI), Frame(self.GUI), Frame(self.GUI), Frame(self.GUI),
                      Frame(self.GUI), Frame(self.GUI)]

        # 最上方的两个按钮！
        self.bt1 = Button(self.frame[0], text="自动", command=self.ButtonEventAuto, width=15, height=2, bg="green",
                          fg="red")
        self.bt1.grid(row=1, column=1)
        self.bt2 = Button(self.frame[0], text="手动", command=self.BottonEventHand, width=15, height=2, bg="white",
                          fg="black")
        self.bt2.grid(row=1, column=2)
        self.frame[0].pack()

        self.Status_Need[0] = 1
        # 采水情况 和 采水深度 两个10元素列表的Label ！
        self.label1 = Label(self.frame[1], text="采水深度", width=15, height=2, bg="WHEAT", fg="black")
        self.label1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.label2 = Label(self.frame[1], text="采水情况", width=15, height=2, bg="WHEAT", fg="black")
        self.label2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.frame[1].pack()

        self.Label_of_Collect = []
        self.var1 = []
        for i in range(10):
            self.var1.append(StringVar())
            self.Label_of_Collect.append(
                Label(self.frame[2], textvariable=self.var1[i], width=15, height=2, bg="black", fg="PURPLE"))
            self.Label_of_Collect[i].grid(row=i + 1, column=1)

        self.Label_of_Depth = []
        self.var2 = []
        for i in range(10):
            self.var2.append(StringVar())
            self.Label_of_Depth.append(
                Label(self.frame[2], textvariable=self.var2[i], width=15, height=2, bg="black", fg="PURPLE"))
            self.Label_of_Depth[i].grid(row=i + 1, column=2)
        self.UpdateVarDepth()
        self.frame[2].pack()

        # 三个参数的名字显示的Label ！
        self.label3 = Label(self.frame[3], text="Temp", width=10, height=2, bg="WHEAT", fg="black")
        self.label3.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label4 = Label(self.frame[3], text="Depth", width=10, height=2, bg="WHEAT", fg="black")
        self.label4.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label5 = Label(self.frame[3], text="Press", width=10, height=2, bg="WHEAT", fg="black")
        self.label5.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.frame[3].pack()

        # 三个参数的数值显示的Label
        self.Label_of_Parameter = []
        self.var3 = []
        for i in range(3):
            self.var3.append(StringVar())
            self.Label_of_Parameter.append(
                Label(self.frame[4], textvariable=self.var3[i], width=10, height=2, bg="white", fg="blue"))
            self.Label_of_Parameter[i].grid(row=1, column=i + 1)
        self.UpdateParmeter()
        self.frame[4].pack()

        # 三个状态的的名字的Label ！
        self.label6 = Label(self.frame[5], text="连接", width=10, height=2, bg="WHEAT", fg="black")
        self.label6.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label7 = Label(self.frame[5], text="采泥器(M)", width=10, height=2, bg="WHEAT", fg="black")
        self.label7.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label8 = Label(self.frame[5], text="探照灯(P)", width=10, height=2, bg="WHEAT", fg="black")
        self.label8.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.frame[5].pack()

        self.light = Canvas(self.frame[6], bg="white", height=50, width=270)
        for i in range(3):
            self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="red")
        self.light.pack()
        self.frame[6].pack()
        self.Update()
        self.GUI.pack()
        self.pack()

    def Fileopen(self):
        if not self.Record:
            T = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            TIMETXT = str(T)+'.txt'
            self.f=open(TIMETXT,'w')
            self.Record = True

    def Write_in(self):
        self.f.write("序列\t状态\t深度\n")
        str1=""
        for x in range(len(self.is_Collect)):
            str1+=str(x)+"\t"+str(self.is_Collect[x])+"\t"+str(self.Depth_Collect[x])+'\n'
        self.f.write(str1)
        strxxx="\nTemp\tDepth\tPress\n"
        str2=strxxx+str(self.Parameter[0])+"\t"+str(self.Parameter[1])+"\t"+str(self.Parameter[2])+"\n\n\n"
        self.f.write(str2)

    def updatethread(self):
        if self.root:
            t = threading.Thread(target=self.Update(),args=())
            t.setDaemon(True)
            t.start()
        else:
            return

    def Fileclose(self):
        if self.Record:
            self.f.close()
            self.Record = False

    def Update(self):
        print("I Receive the Message from Raspberry Pi!\n")
        self.Go()
        if not Flag:
            self.UpdateVarDepth()
            self.UpdateParmeter()
            self.UpdateStatus()
            if self.Record:
                self.Write_in()

    # 接收消息
    def receiveMessage(self):
        try:
            # 建立Socket连接
            self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSock.connect((self.local, self.port))
            print("Start Connect!")
            self.flag = True
        except:
            self.flag = False
            print("Connect Failed!")
            return

        self.buffer = 1024
        self.clientSock.send('Y'.encode())
        count = 0
        while True:
            print("我还活在线程里！")
            try:
                if self.flag:
                    # 连接建立，接收服务器端消息
                    self.serverMsg = self.clientSock.recv(self.buffer).decode()
                    if self.serverMsg == 'Y':
                        print("OK! Connect NOW!")
                        self.Status_Now[0] = 1
                    elif self.serverMsg == 'N':
                        print("Connect Failed! ")
                    elif not self.serverMsg:
                        continue
                    else:
                        self.DECODE(self.serverMsg)
                        time.sleep(0.1)
                        self.sendMessage()
                        try:
                            self.Update()
                        except RuntimeError as msg:
                            print(msg)
                            return
                        except TclError as msg:
                            print(msg)
                            return
                else:
                    print("终于离开了！")
                    break
            except EOFError as msg:
                raise msg
                self.clientSock.close()
                break

    # 发送消息
    def sendMessage(self):
        # 得到用户在Text中输入的消息
        self.ENCODE()
        if self.flag == True:
            # 将消息发送到服务器端
            self.clientSock.send(self.SendMsg.encode())
            for i in range(4):
                self.Action[i] = 0
        else:
            # Socket连接没有建立，提示用户
            print('您还未与服务器端建立连接，服务器端无法收到您的消息\n')

    # 关闭消息窗口并退出
    def close(self):
        self.Fileclose()
        Flag = True

    # for Client to decode the info from Server !
    def DECODE(self, msg):
        # 解析来自主机的26个变量！我也是见了鬼了！为毛会出来一个Y ?!!!
        s = msg.split(" ")
        x=[]
        for i in s:
            if i.find('Y') != -1:
                x.append(i[i.find('Y')+1:])
            elif i.find('Y') == -1:
                x.append(i)
        print(x)
        for i in range(len(self.Status_Now)):
            self.Status_Now[i] = int(x[i])
        for i in range(len(self.Parameter)):
            self.Parameter[i] = float(x[i + len(self.Status_Now)])
        for i in range(len(self.is_Collect)):
            self.is_Collect[i] = int(x[i + len(self.Status_Now) + len(self.Parameter)])
        for i in range(len(self.Depth_Collect)):
            self.Depth_Collect[i] = float(x[i + len(self.Status_Now) + len(self.Parameter) + len(self.is_Collect)])

    def ENCODE(self):
        # 从机打包8个变量发送到从机PC
        self.SendMsg = ""
        for i in self.Action:
            self.SendMsg += (str(i) + " ")
        for i in range(3):
            self.SendMsg += (str(self.Status_Need[i]) + " ")

    # 启动线程接收服务器端的消息
    def startNewThread(self):
        # 启动一个新线程来接收服务器端的消息
        # thread.start_new_thread(function, args[, kwargs])函数原型，
        # 其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        # receiveMessage函数不需要参数，就传一个空元组
        # thread.start_new_thread(self.receiveMessage, ())
        self.t = threading.Thread(target=self.receiveMessage,args=())
        self.t.setDaemon(True)
        self.t.start()

    def Key_Input(self, event):

        if event.char == 'z':
            self.Fileclose()
            stop_thread(self.t)
            print("啊啊啊 被杀了！")
            print(self.t.is_alive())
            if self.t.is_alive():
                stop_thread(self.t)
            print(self.t.is_alive())
            sys.exit(1)
        print("pressed", repr(event.char))
        if event.char=='u':
            if self.Status_Need[0] == 0:
                self.ButtonEventAuto()
            elif self.Status_Need[0] == 1:
                self.BottonEventHand()
            print("self.Status_Need[0]：", self.Status_Need[0])

        if event.char=='r':
            self.Fileopen()
        if event.char=='t':
            if self.Record:
                self.Fileclose()

        if self.Status_Need[0] == 1:
            return
        if event.char=='w':
            self.Action[0]=1
        elif event.char=='s':
            self.Action[1]=1
        elif event.char=='a':
            self.Action[2]=1
        elif event.char=='d':
            self.Action[3]=1
        elif event.char=='b':
            self.Action[4]=(self.Action[4]+1)%2
        elif event.char == 'm':
            self.Status_Need[1] = (self.Status_Need[1]+1)%2
            print("self.Status_Need[1]：", self.Status_Need[1])
        elif event.char == 'p':
            self.Status_Need[2] = (self.Status_Need[2]+1)%2
            print("self.Status_Need[2]：", self.Status_Need[2])

    def Go(self):
        self.count += 1
        if self.count > 50:
            self.count = 0
        for i in self.Status_Now:
            print(" Now The Status_Now is : ", i)

    def UpdateVarDepth(self):
        if Flag:
            return
        for i in range(10):
            if self.root:
                self.var1[i].set(caiji[self.is_Collect[i]])

        for i in range(10):
            self.var2[i].set(str(self.Depth_Collect[i]))
            if self.is_Collect[i] == 1:
                self.Label_of_Collect[i]['bg'] = "MEDIUM SPRING GREEN"
                self.Label_of_Depth[i]['bg'] = "MEDIUM SPRING GREEN"
                self.Label_of_Depth[i]['fg'] = "SLATE BLUE"
                self.Label_of_Collect[i]['fg'] = "SLATE BLUE"

            elif self.is_Collect[i] == 0:
                self.Label_of_Collect[i]['bg'] = "DARK GREY"
                self.Label_of_Depth[i]['bg'] = "DARK GREY"
                self.Label_of_Depth[i]['fg'] = "red"
                self.Label_of_Collect[i]['fg'] = "red"

    def UpdateParmeter(self):
        if Flag:
            return
        for i in range(3):
            self.var3[i].set(str(self.Parameter[i]))

    def UpdateStatus(self):
        if Flag:
            return
        for i in range(3):
            if self.Status_Now[i] == 1:
                self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="green")
            if self.Status_Now[i] == 0:
                self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="red")

    def ButtonEventAuto(self):
        print("You have Changed The Way of Control to Automatic!")
        self.Status_Need[0] = 1
        self.bt1['fg'] = "red"
        self.bt1['bg'] = "green"
        self.bt2['fg'] = "black"
        self.bt2['bg'] = "white"

    def BottonEventHand(self):
        print("You have Changed The Way of Control to Handle!")
        self.Status_Need[0] = 0
        self.bt2['fg'] = "red"
        self.bt2['bg'] = "green"
        self.bt1['fg'] = "black"
        self.bt1['bg'] = "white"




def main():
    r=Tk()
    # def closeWindow():
    #     ans = askyesno(title='Warning', message='Close the window?')
    #     if ans:
    #         r.destroy()
    #         stop_thread(client.t)
    #     else:
    #         return
    # r.protocol('WM_DELETE_WINDOW', closeWindow)
    client = ClientUI(root=r)
    client.startNewThread()
    try:
        r.mainloop()
    except RuntimeError as msg:
        print(msg)
        client.close()
    if client.t.is_alive():
        print("杀了他！求你！")
        stop_thread(client.t)
    client.Fileclose()
    return


if __name__ == '__main__':
    # webbrowser.open("http://www.bilibili.com")
    main()