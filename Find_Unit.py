shoplist=['apple','mango','carrot','banana']
shoptuple=tuple(shoplist)

def Find_Unit(shoptuple):
    size=len(shoptuple)
    Unit=[]
    for i in range(len(shoptuple[0])):
        count=0
        s=shoptuple[0][i]
        # print s
        for x in range(size):
            if shoptuple[x].find(s)!=-1 and x!=0:
                print 'In \'%s\', We have find the \'%s\' '%(shoptuple[x],s)
                count=count+1
        if count==size:
            print s
            Unit.append(s)

Find_Unit(shoptuple)