import random
ch=int(input("Enter number of characters needed in password:"))
num=int(input("Enter number of number needed in password:"))
s=""
n=""
for i in range(ch):
    nn=random.choice([1,2,3])
    if(nn==1):r1=random.randrange(65,91)
    elif(nn==2):r1 = random.randrange(97,123)
    else:r1 = random.randrange(58,64)
    s=s+chr(r1)
for j in range(num):
    r2=random.randrange(48,58)
    n=n+chr(r2)
p=s+n
lp=list(p)
random.shuffle(lp)
pw=""
for z in range(len(lp)):
    pw=pw+lp[z]
print("recommended password :"+pw)

