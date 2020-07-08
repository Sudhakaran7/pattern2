n=int(input())
for i in range(n):
    for j in range(i):
      if(i%2==0):
        print ('* ', end="")
      else:
        print(j+1,end=' ')
    print('')

for i in range(n,0,-1):
    for j in range(i):
      if(i%2==0):
        print ('* ', end="")
      else:
        print(j+1,end=' ')
    print('')
