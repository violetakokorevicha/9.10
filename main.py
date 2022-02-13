list=[ ]
N = int(input("How many people was:"))
for i in range(N):
  mass=int(input("Your mass: "))
  list.append(mass)
listsum=sum(list)
print(listsum)
listavg=sum(list)/len(list)
print(listavg)
if listsum > 300:
  print("They can't go  all together")
else:
  print("They can go all together")