# import math
# def sinx(x):
#     return float(x)/1000,math.sin(float(x)/1000)

# file=open('/Users/zhangzhaobo/program/python/sint.txt','w+')
# s=map(sinx,range(0,6281))
# file.write(str(s))
# file.close()



def SuShu(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
        return x
    else:
        return 0
print(SuShu(5))