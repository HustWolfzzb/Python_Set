import math
def calculator():
	print('请输入你想要进行的操作：\n0:退出\n1：进入计算（第一个输入第一个运算数，然后输入+ - * ／ % 最后输入另一个运算数）\n2：计算一位操作数函数（首先输入sin/acrsin/arccos/cos/tan/cot/sinh/asinh/cosh/acosh/tanh/atanh/ln/lg/sqrt）,然后输入你想要计算的数字\n3:先输入操作字符，然后输入一个或者两个操作数(pow/log(x,[,n])')
	judge=eval(input("输入操作："))
	if judge==1:
		DoIt()
	elif judge==2:
		DoIt2()
	elif judge==3:
		DoIt3()
	else:
		print('what do you want ?')




def DoIt():
	s=1
	if s==1:
		a=input('the first number:')
		operate=input('the action you want:')
		b=input('the second number:')
		
		if JudgeOperate(b)!=0:
			print('*********************************\n')
			print('                                *\n')
			calcaute(a,operate,b)
			print('                                *\n')
			print('*********************************\n\n')
			s=int(input('what do you want to do next?\n please tell me\n0:turn off calculator\n1:continue\n2:choose new opration\n0/1/2 :'))
		else:
			print('Hey! what do you want?')
	elif s==2:
		main()
	elif s==0:
		print("thanks for your using")



def DoIt2():
	s=1
	if s==1:
		a='sin'
		a=input('the operate you want: ')
		b=1
		b=input('the number: ')
	#	JudgeOperate2(a,b)
		if b:
			pass
		#	if JudgeOperate2(a,b)!=0:
			print('*********************************\n')
			print('                                *\n')
			calcaute2(a,b)
			print('                                *\n')
			print('*********************************\n\n')
			s=int(input('what do you want to do next?\n please tell me\n0:turn off calculator\n1:continue\n2:choose new opration\n0/1/2 :'))
		else:
				print('Hey! what do you want?')
	elif s==2:
		main()
	elif s==0:
		print("thanks for your using")




def DoIt3():
	s=1
	if s==1:
		operate=input('the operate:')
		a=input('the first number（底数）:')
		b=input('the second number（运算数）:')
		
		if operate in 'pow' or 'log':
			print('*********************************\n')
			print('                                *\n')
			calcaute3(operate,a,b)
			print('                                *\n')
			print('*********************************\n\n')
			s=int(input('what do you want to do next?\n please tell me\n0:turn off calculator\n1:continue\n2:choose new opration\n0/1/2 :'))

		else:
			print('Hey! what do you want?')
	elif s==2:
		main()
	elif s==0:
		print("thanks for your using")




def JudgeOperate(b):
	if b==0:
		return 0


#def JudgeOperate2(a,b):
#	if (x=='sin' or x=='cos') and (u<0 or u>1 ):
#		return 0



def calcaute(a,operate,b):
	a=float(a)
	b=float(b)
	s=0.00
	if   operate=='+':
		s=a+b
		print("%f + %f=%f"%(a,b,s))
	elif operate=='-':
		s=a-b
		print("%f - %f=%f"%(a,b,s))
	elif operate=='*':
		s=a*b
		print("%f * %f=%f"%(a,b,s))
	elif operate=='/':
		s=a/b
		print("%f / %f=%f"%(a,b,s))
	elif operate=='%':
		s=a%b
		print("%f % %f=%f"%(a,b,s))

def calcaute2(a,b):
	a=str(a)
	b=float(b)
	if   a=='sin':
		print("%s(%f)=%f"%(a,b,math.sin(b)))
	elif a=='cos':
		print("%s(%f)=%f"%(a,b,math.cos(b)))
	elif a=='tan':
		print("%s(%f)=%f"%(a,b,math.tan(b)))
	elif a=='arcsin':
		print("%s (%f)=%f"%(a,b,math.asin(b)))
	elif a=='arccos':
		print("%s (%f)=%f"%(a,b,math.acos(b)))
	elif a=='arctan':
		print("%s (%f)=%f"%(a,b,math.atan(b)))
	elif a=='sinh':
		print("%s (%f)=%f"%(a,b,math.sinh(b)))
	elif a=='asinh':
		print("%s (%f)=%f"%(a,b,math.asinh(b)))
	elif a=='cosh':
		print("%s(%f)=%f"%(a,b,math.cosh(b)))
	elif a=='acosh':
		print("%s(%f)=%f"%(a,b,math.acosh(b)))
	elif a=='tanh':
		print("%s(%f)=%f"%(a,b,math.tanh(b)))
	elif a=='atanh':
		print("%s(%f)=%f"%(a,b,math.atanh(b)))
	elif a=='ln':
		print("%s(%f)=%f"%(a,b,math.log(b)))
	elif a=='log':
		print("%s(%f)=%f"%(a,b,math.log10(b)))
	elif a=='sqrt':
		print("%s(%f)=%f"%(a,b,math.sqrt(b)))

def calcaute3(operate,a,b):
	a=float(a)
	b=float(b)
	if operate=='pow':
		print("pow(%f,%f)=%f"%(a,b,math.pow(a,b)))
	elif operate=='log':
		print("log结果是：%f"%math.log(b,a))

calculator()
