T=int(input())

for i in range(T):
    n=int(input()) #first input
    cityList=['']*n #creating an empty list to put the cities into 
    for x in range(n):
        city=input() # second input
        cityList[x]=city #putting the cities into the list
    distinctTrips=len(set(cityList)) #using set to find the distinct cities then finding the number of them
    print(distinctTrips)



