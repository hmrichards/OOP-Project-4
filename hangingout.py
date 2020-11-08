inputs=input().split(' ') #first input
L=int(inputs[0])
x=int(inputs[1])
totalPeople=0
deny=0 #initializing number of people denied

for i in range(x):
    enterOrleave=input().split(' ') #second input
    direction=enterOrleave[0] 
    number=int(enterOrleave[1])
    if direction=='enter':
        totalPeople+=number
        if totalPeople>L: #if the number of people in group exceed the limit, they are sent out
            totalPeople-=number
            deny+=1 #number of denied groups goes up by one
    else:
        totalPeople-=number 
            
print(deny)
