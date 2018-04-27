from tkinter import *
class BMICalculator(object):
	"""docstring for BMICalculator"""
	def __init__(self):
		window=TK()
		window.title("BMI Calculator")

		Label(window, text = "Name").grid(row = 1,column = 1, sticky = W)
		Label(window, text = "Weight").grid(row = 2,column =1, sticky = W)
		Label(window, text = "Height").grid(row = 3,column = 1, sticky = W)
		Label(window, text = "BMI").grid(row = 4,column = 1, sticky = W)
		Label(window, text = "State").grid(row = 5,column = 1, sticky = W)

		self.NameVar = StringVar()
		Entry(window, textvariable = self.NameVar, justify = RIGHT).grid(row = 1, column = 2)
		Entry(window, textvariable = self.Weight, justify = RIGHT).grid(row = 2, column = 2)
		Entry(window, textvariable = self.Height, justify = RIGHT).grid(row = 3, column = 2)
		self.BMI=StringVar()
		TheBMI=Label(window, textvariable = self.BMI).grid(row = 4, column = 2, sticky = E)
		self.State=StringVar()
		TheState=Label(window, textvariable = self.State).grid(row = 5, column = 2, sticky = E)

	def computeBMI(self):
		self.BMI= self.Calculator(float(self.Weight.get()),float(self.Height.get()))
		self.State=computeState(slef.BMI)

	def Calculator(self,a,b):
		return a/b**2
	
	def computeState(self,a):
		if a<18.5:
			print("thin")
		if a>18.5 and a<24.99:
			print("normal")
		if a<28 and a>25:
			print("fat")
		if a<32 and a>28:
			print("very fat")




