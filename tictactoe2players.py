import sys 
def inpu():
  n=int(input())
  if(n not in s and n<10 and n>0):
    s.append(n)
    return(n)
  else:
    print("you entered invalid position")
    print("restart the game")
    sys.exit()
    return(n)
def win(i):
  if(i%2!=1):
    print("winner is ",na)
  else:
    print("winner is ",nb)
def check():
  x=(a[0]==a[1]==a[2]!="_" or a[3]==a[4]==a[5]!="_" or a[6]==a[7]==a[8]!="_")
  y=(a[0]==a[3]==a[6]!="_" or a[1]==a[4]==a[7]!="_" or a[2]==a[5]==a[8]!="_")
  z=(a[0]==a[4]==a[8]!="_" or a[6]==a[4]==a[2]!="_")
  return(x or y or z)
def dis():
  print("| ",a[0]," | ",a[1]," | ",a[2]," |   ","| ","1"," | ","2"," | ","3"," |")
  print("| ",a[3]," | ",a[4]," | ",a[5]," |   ","| ","4"," | ","5"," | ","6"," |")
  print("| ",a[6]," | ",a[7]," | ",a[8]," |   ","| ","7"," | ","8"," | ","9"," |")
  print()
a=["_","_","_","_","_","_","_","_","_"]
s=[]
na=input("Enter first player name ")
nb=input("Enter second player name ")
for i in range(1,10):
  dis()
  if(check()):
    win(i)
    break
  print("Enter your position ")
  if(i%2==1):
    print(na,"'s Turn ")
    n=inpu()
    a[n-1]="X"
  else:
    print(nb,"'s Turn ")
    n=inpu()
    a[n-1]="O"
else:
  print("match is draw")

  
