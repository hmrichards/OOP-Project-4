done=False
people=[] 
nameList=[]
sets=0

while not done:
    n=int(input()) #first input
    sets+=1
    if n>0:
        people.clear()
        for i in range(n):
            name=input() #second input
            people.append(name)
        people1=people[::2] #taking every other person starting at index 0
        people2=people[1::2] #taking every other person starting at index 1
        newPeople=people1+people2[::-1] #adding the lists together using reverse of people2
        nameList.append('Set '+ str(sets)) #adding set number before the names
        for p in newPeople:
            nameList.append(p) #adding each name from new list to create ordered list
        
    else:
        done=True
    

for l in nameList:
    print(l) #printing everything in the list 


            
                

