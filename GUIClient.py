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
import webbrowser

caiji = ["未采", "已采"]


class ClientUI():
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
    local = 'localhost'
    port = 8808
    global clientSock
    flag = False

    # 初始化类的相关属性，类似于Java的构造方法

    def __init__(self):
        print("Start Now! ")
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
        self.root = tkinter.Tk()
        self.root.title(self.title)
        # 监听键盘！
        self.root.bind('<Key>',self.Key_Input)
        # 总窗口，所有的部件都挂在这上面
        self.GUI = Frame(self.root)
        # 窗口面板, 用7个面板布局
        self.frame = [Frame(self.GUI), Frame(self.GUI), Frame(self.GUI), Frame(self.GUI), Frame(self.GUI),
                      Frame(self.GUI), Frame(self.GUI)]


        # 最上方的两个按钮！
        self.bt1 = Button(self.frame[0], text="自动", command=self.ButtonEventAuto, width=15, height=3, bg="red",
                          fg="black")
        self.bt1.grid(row=1, column=1)
        self.bt2 = Button(self.frame[0], text="手动", command=self.BottonEventHand, width=15, height=3, bg="black",
                          fg="black")
        self.bt2.grid(row=1, column=2)
        self.frame[0].pack()

        # 采水情况 和 采水深度 两个10元素列表的Label ！
        self.label1 = Label(self.frame[1], text="采水情况", width=15, height=3, bg="pink", fg="red")
        self.label1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.label2 = Label(self.frame[1], text="采水深度", width=15, height=3, bg="pink", fg="red")
        self.label2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.frame[1].pack()

        self.Label_of_Collect = []
        self.var1 = []
        for i in range(10):
            self.var1.append(StringVar())
            self.Label_of_Collect.append(
                Label(self.frame[2], textvariable=self.var1[i], width=15, height=2, bg="black", fg="blue"))
            self.Label_of_Collect[i].grid(row=i + 1, column=1)

        self.Label_of_Depth = []
        self.var2 = []
        for i in range(10):
            self.var2.append(StringVar())
            self.Label_of_Depth.append(
                Label(self.frame[2], textvariable=self.var2[i], width=15, height=2, bg="black", fg="blue"))
            self.Label_of_Depth[i].grid(row=i + 1, column=2)
        self.UpdateVarDepth()
        self.frame[2].pack()

        # 三个参数的名字显示的Label ！
        self.label3 = Label(self.frame[3], text="Temp", width=10, height=3, bg="pink", fg="red")
        self.label3.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label4 = Label(self.frame[3], text="Depth", width=10, height=3, bg="pink", fg="red")
        self.label4.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label5 = Label(self.frame[3], text="Depth", width=10, height=3, bg="pink", fg="red")
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
        self.label6 = Label(self.frame[5], text="Connection？", width=10, height=3, bg="pink", fg="red")
        self.label6.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label7 = Label(self.frame[5], text="采泥启动？(M)", width=10, height=3, bg="pink", fg="red")
        self.label7.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label8 = Label(self.frame[5], text="探照灯？(P)", width=10, height=3, bg="pink", fg="red")
        self.label8.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.frame[5].pack()

        self.light = Canvas(self.frame[6], bg="white", height=60, width=270)
        for i in range(3):
            self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="red")
        self.light.pack()
        self.frame[6].pack()
        self.GUI.pack()

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
        while True:
            try:
                if self.flag == True:
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
                        print("I Receive the Message from Raspberry Pi!\n")
                        self.Go()
                        self.DECODE(self.serverMsg)
                        self.UpdateVarDepth()
                        self.UpdateParmeter()
                        self.UpdateStatus()
                        self.sendMessage()
                        time.sleep(0.3)
                else:
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
        sys.exit()

    # for Client to decode the info from Server !

    def DECODE(self, msg):
        # 解析来自主机的26个变量！
        x = msg.split(" ")
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
        t = threading.Thread(target=self.receiveMessage, args=())
        t.start()

    def Key_Input(self, event):
        print("pressed", repr(event.char))
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
        elif event.char=='u':
            self.Status_Need[0] = (self.Status_Need[0]+1)%2
            print("self.Status_Need[0]：", self.Status_Need[0])
        elif event.char == 'm':
            self.Status_Need[1] = (self.Status_Need[1]+1)%2
            print("self.Status_Need[1]：", self.Status_Need[1])
        elif event.char == 'p':
            self.Status_Need[2] = (self.Status_Need[2]+1)%2
            print("self.Status_Need[2]：", self.Status_Need[2])
        self.sendMessage()

    def Go(self):
        self.count += 1
        if self.count > 50:
            self.count = 0
        for i in self.Status_Now:
            print(" Now The Status_Now is : ", i)

    def UpdateVarDepth(self):
        for i in range(10):
            self.var1[i].set(caiji[self.is_Collect[i]])

        for i in range(10):
            self.var2[i].set(str(self.Depth_Collect[i]))
            if self.is_Collect[i] == 1:
                self.Label_of_Collect[i]['bg'] = "white"
                self.Label_of_Depth[i]['bg'] = "white"
            elif self.is_Collect[i] == 0:
                self.Label_of_Collect[i]['bg'] = "black"
                self.Label_of_Depth[i]['bg'] = "black"

    def UpdateParmeter(self):
        for i in range(3):
            self.var3[i].set(str(self.Parameter[i]))

    def UpdateStatus(self):
        for i in range(3):
            if self.Status_Now[i] == 1:
                self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="green")
            if self.Status_Now[i] == 0:
                self.light.create_oval(25 + 90 * i, 10, 65 + 90 * i, 50, fill="red")

    def ButtonEventAuto(self):
        print("You have Changed The Way of Control to Automatic!")
        self.Status_Need[0] = 1
        self.bt1['fg'] = "red"
        self.bt2['fg'] = "black"

    def BottonEventHand(self):
        print("You have Changed The Way of Control to Handle!")
        self.Status_Need[0] = 0
        self.bt2['fg'] = "red"
        self.bt1['fg'] = "black"


def main():
    client = ClientUI()
    client.startNewThread()
    client.root.mainloop()


if __name__ == '__main__':
    # webbrowser.open("http://www.bilibili.com")
    main()
