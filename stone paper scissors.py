import random
print("This is stone paper scissor game \n(you vs computer)")
print("Enter:\n1 for STONE\n2 for PAPER\n3 for SCISSOR")
print("Enter 0 to end the game")
l=["STONE","PAPPER","SCISSOR"]
d=y=c=m=0
while (1):
  print()
  n=int(input())
  if(n==0):
    break
  elif(not(n>0 and n<4)):
    print("Enter valid input")
    break
  else:
    i=random.choice([1,2,3])
    print("You ",l[n-1],"VS Computer ",l[i-1])
    m=m+1
    if(n==i):
      print("Draw")
      d=d+1
    elif((n==1 and i==3) or(n==2 and i==1) or (n==3 and i==2)):
      print("You wins")
      y=y+1
    else:
      print("Computer wins")
      c=c+1
print("Match ended results are...")
print("Totall matches played :",m)
print("Number of winning is  :",y)
print("Number of loses is.   :",c)
print("Number of draws is.   :",d)
