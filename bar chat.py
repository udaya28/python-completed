a=[]
c=int(input("no of column"))
print("size of each column")
for x in range(0,c):
  y=int(input())
  a.append(y)
m=max(a)
print(a)
g=[0 for l in range(c) ]
for i in range(0,m):
  print()
  for j in range(0,c):
      if(m-a[j]==i or g[j]==1):
         print("**",end=" ")
         g[j]=1
      else:
         print("  ",end=" ")
print()
n=c*2+(c-1)  
print("*"*n)
