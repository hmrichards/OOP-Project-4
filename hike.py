n=int(input())
temp=input().split(' ')
t=[int(x) for x in temp]
bestStartDay=0
bestHikingTemps=[40,40]

for i in range(n-2):
    startTemp=t[i] #temperature on the first day
    endTemp=t[i+2] #temperature on the second day
    hikingTemps=[startTemp, endTemp]
    if max(hikingTemps)<max(bestHikingTemps):
        bestHikingTemps=hikingTemps
        bestStartDay=i+1

print(bestStartDay, max(bestHikingTemps))





