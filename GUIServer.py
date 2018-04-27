# _*_ coding:utf-8 _*_
# Filename:GUIServer.py
# 水下作业机器人树莓派服务器端

import tkinter
#import tkFont
import tkinter.font
import socket
import threading
import time
import sys

class Server():
    # from the 传感器！
    count = 0
    is_Collect = []
    # from the 传感器！
    Depth_Collect = []
    # from the 传感器！
    Parameter = []
    # from the Pi! Connection  P U M
    Status_Now = []

    # from the client ! PC :P U M
    Status_Need = []
    # from the client ! PC :W A S D B
    Action = []

    SendMsg = ""
    local = ''
    port = 8808
    global serverSock
    flag = False
    received = False


#初始化类的相关属性，类似于Java的构造方法

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

    #接收消息
    def receiveMessage(self):
        #建立Socket连接

        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((self.local, self.port))
        self.serverSock.listen(15)
        self.buffer = 1024
        print('The Server is Ready!......')
        #循环接受客户端的连接请求
        while True:
            self.connection , self.address = self.serverSock.accept()
            self.flag = True
            while True:
                #接收客户端发送的消息
                self.clientMsg = self.connection.recv(self.buffer).decode()
                if not self.clientMsg:
                    continue
                elif self.clientMsg == 'Y':
                    self.Status_Now[0] = 1
                    self.sendMessage()
                    self.connection.send('Y'.encode())
                elif self.clientMsg == 'N':
                    self.Status_Now[0] = 0
                    self.connection.send('N'.encode())
                else:
                    self.DECODE(self.clientMsg)
                    print("I Receive the Message from PC!")
                    self.Go()
                    self.sendMessage()
                    time.sleep(0.3)
    
    #发送消息
    def sendMessage(self) -> object:
        self.test()
        self.count += 1
        if self.count > 100:
            self.count = 0
        self.ENCODE()
        self.connection.send(self.SendMsg.encode())

    #关闭消息窗口并退出
    def close(self):
        sys.exit()

    def ENCODE(self):
        # 主机打包26个变量发送到从机PC
        self.SendMsg = ""
        for i in self.Status_Now:
            self.SendMsg += (str(i)+" ")
        for i in self.Parameter:
            self.SendMsg += (str(i)+" ")
        for i in self.is_Collect:
            self.SendMsg += (str(i)+" ")
        for i in self.Depth_Collect:
            self.SendMsg += (str(i)+" ")

    def DECODE(self, msg):
        x = msg.split(" ")
        for i in range(5):
            self.Action[i] = int(x[i])
        for i in range(3):
            self.Status_Need[i] = int(x[i+5])
            print(self.Status_Need[i])

    def Go(self):
        for i in self.Status_Now:
            print(" Now The Status_Now is : ", i)


    #启动线程接收客户端的消息
    def startNewThread(self):
        #启动一个新线程来接收客户端的消息
        #thread.start_new_thread(function, args[, kwargs])函数原型，
        #其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        #receiveMessage函数不需要参数，就传一个空元组
        #thread.start_new_thread(self.receiveMessage, ())
        t=threading.Thread(target=self.receiveMessage, args=())
        t.start()

    def test(self):
        count1 = self.count
        print("I am in the Test!")
        self.is_Collect[count1%10]= (self.is_Collect[count1%10]+1)%2
        if count1 > 100:
            count1 = 0
        self.Depth_Collect[count1%10] = count1%6
        self.Parameter[count1%3] = count1
        if self.Status_Need[0] == 0:
            self.getDepth()
            self.getIsCollent()
            self.getStatus()
            self.getParameter()
            self.setStatus()
            self.setAction()
        if self.Status_Need[0] == 1:
            self.Automatic_Action()


    def Automatic_Action(self):
        pass

    def getIsCollent(self):
        # get the info from device
        pass

    def getDepth(self):
        # get the info of Depth from device
        pass

    def getStatus(self):
        self.Status_Now[1] = self.Status_Need[1]
        self.Status_Now[2] = self.Status_Need[2]
        # get the Status[0-2] from the device
        pass

    def getParameter(self):
        # get the press,temp,depth  Parameter[0-2]
        pass

    def setStatus(self):
        # use the Status_Need to change the status of the device! if Auto is open! nothing but the automatic program!
        pass

    def setAction(self):
        # deal the control info from Status_Need! if Auto is open! nothing but the automatic program!
        pass


def main():
    server = Server()
    # server.startNewThread()
    while True:
        server.receiveMessage()
    
if __name__  == '__main__':
    main()
