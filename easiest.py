done=False
pList=[]
while not done:
    N=input()
    equal=False
    if int(N)>0:
        s1=0
        s2=0
        for i in range(len(N)):
            s1+=int(str(N)[i])
        while not equal:
            for p in range(11, 10000):
                
                s2=0
                mult=int(N)*p
                for n in range(len(str(mult))):
                    s2+=int(str(mult)[n])
                    if s1==s2:
                        equal=True
        pList.append(p) 
            
    else:
        done=True
print(s1)
print(pList)

        

