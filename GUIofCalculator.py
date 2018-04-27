import math
from tkinter import *
class GUI:
	def __init__(self):
		#the self function 
		window=Tk()
		window.title("Calculator made by HustWolf")
		menubar=Menu(window)
		window.config(menu=menubar)
		operationMenu=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="Operation",menu=operationMenu)
		operationMenu.add_command(label="operation1",command=self.operation1)
		operationMenu.add_command(label="operation2",command=self.operation2)
		operationMenu.add_command(label="operation3",command=self.operation3)
		exitmenu=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="Exit",menu=exitmenu)
		exitmenu.add_command(label="exit",command=window.quit)
		frame0=Frame(window)
		frame0.grid(row=1,column=1,sticky=W)
		Button(frame0,text="operation1",bg="red",command=self.operation1).grid(row=1,column=1,sticky=W)
		Button(frame0,text="operation2",bg="green",command=self.operation2).grid(row=1,column=2)
		Button(frame0,text="operation3",bg="blue",command=self.operation3).grid(row=1,column=3)

		frame1=Frame(window)
		frame1.grid(row=2,column=1,pady=50)
		Label(frame1,text="number1:").pack(side=LEFT)
		self.v1=StringVar()
		Entry(frame1,width=5,textvariable=self.v1,justify=RIGHT).pack(side=LEFT)
		Label(frame1,text="operation").pack(side=LEFT)
		self.v2=StringVar()
		Entry(frame1,width=5,textvariable=self.v2,justify=RIGHT).pack(side=LEFT)

		Label(frame1,text="number2:").pack(side=LEFT)
		self.v3=StringVar()
		Entry(frame1,width=5,textvariable=self.v3,justify=RIGHT).pack(side=LEFT)
		
		# Label(frame1,text="Result:").pack(side=LEFT)
		

		frame2=Frame(window)
		frame2.grid(row=3,column=1,pady=50)

		self.v4=StringVar()
		Label(frame2,text="Result: ").pack(side=LEFT)
		result=Label(frame2,width=20,textvariable=self.v4,justify=LEFT).pack(side=LEFT)


		window.mainloop()



	def operation1(self):
		judge=1
		a=float(self.v1.get())
		b=float(self.v3.get())
		operate=self.v2.get()
		res=0.00
		if operate=='+':
			res=a+b

		elif operate=='-':
			res=a-b

		elif operate=='*':
			res=a*b

		elif operate=='/':
			res=a/b

		elif operate=='%':
			res=a%b

		self.v4.set(str(res))

	def operation2(self):
		judge=2
		a=float(self.v1.get())
		b=float(self.v3.get())
		operate=self.v2.get()
		res=0.00
		if operate=='sin':
			res=math.sin(a*b)

		elif operate=='cos':
			res=math.cos(a*b)

		elif operate=='tan':
			res=math.tan(a*b)

		elif operate=='arcsin':
			res=math.asin(a*b)

		elif operate=='arccos':
			res=math.acos(a*b)

		elif operate=='arctan':
			res=math.atan(a*b)

		elif operate=='sinh':
			res=math.sinh(a*b)

		elif operate=='asinh':
			res=math.asinh(a*b)

		elif operate=='cosh':
			res=math.cosh(a*b)

		elif operate=='acosh':
			res=math.acosh(a*b)

		elif operate=='tanh':
			res=math.tanh(a*b)

		elif operate=='atanh':
			res=math.atanh(a*b)

		elif operate=='ln':
			res=math.log(a*b)

		elif operate=='log':
			res=math.log10(a*b)

		elif operate=='sqrt':
			res=math.sqrt(a*b)

		self.v4.set(str(res))

	def	operation3(self):
		judge=3
		a=float(self.v1.get())
		b=float(self.v3.get())
		operate=self.v2.get()
		res=0.00
		if operate=='pow':
			res=math.pow(a,b)
		elif operate=='log':
			res=math.log(b,a)
		self.v4.set(str(res))



#Run the program

GUI()








