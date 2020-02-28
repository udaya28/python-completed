#udaya 19CSR118
#whatsup no :9788676364
#please report if you find any problem
import sys
def inp(s):
    i=input(s)
    for x in i:
        if((ord(x)>=48) and (ord(x)<=57) or ord(x)==45):
           pass
        else:
            print("\nINVALID INPUT \nInput must be a integer  ")
            sys.exit()
    return i
print("MESH ANALYSIS by Udaya \t   HAPPY CODDING")
print("For reporting and other contact \nsee top or bottom of the code")
c=int(inp("Enter 2 for 2 equation\nEnter 3 for 3 equation : "))
if(c==2):
    print("\nEnter the coefficients of first equation : ")
    x1=int(inp("Enter the coefficient of I1 : "))
    y1=int(inp("Enter the coefficient of I2 : "))
    p1=int(inp("Enter the constant of the equation : "))

    print("\nEnter the coefficients of second equation : ")
    x2=int(inp("Enter the coefficient of I1 : "))
    y2=int(inp("Enter the coefficient of I2 : "))
    p2=int(inp("Enter the constant of the equation : "))

    a=((x1*y2)-(x2*y1))
    print("\n\nDell = ",a)
    if(a==0):
         print("INVALID INPUT\nDell will not be Zero")
         sys.exit()

    a1=((p1*y2)-(p2*y1))
    print("\nDell I1 = ",a1)

    a2=((x1*p2)-(x2*p1))
    print("\nDell I2 = ",a2)

    i1=round(a1/a,4)
    i2=round(a2/a,4)

    print("\nI1 = ",i1,"A")
    print("\nI2 = ",i2,"A")
    print("\nI1 + I2 = ",abs(round(i1+i2,4)),"A")
    print("\nI1 - I2 = ",abs(round(i1-i2,4)),"A")
elif(c==3):
    print("\nEnter the coefficients of first equation : ")
    x1=int(inp("Enter the coefficient of I1 : "))
    y1=int(inp("Enter the coefficient of I2 : "))
    z1=int(inp("Enter the coefficient of I3 : "))
    p1=int(inp("Enter the constant of the equation : "))

    print("\nEnter the coefficients of second equation : ")
    x2=int(inp("Enter the coefficient of I1 : "))
    y2=int(inp("Enter the coefficient of I2 : "))
    z2=int(inp("Enter the coefficient of I3 : "))
    p2=int(inp("Enter the constant of the equation : "))

    print("\nEnter the coefficients of third equation : ")
    x3=int(inp("Enter the coefficient of I1 : "))
    y3=int(inp("Enter the coefficient of I2 : "))
    z3=int(inp("Enter the coefficient of I3 : "))
    p3=int(inp("Enter the constant of the equation : "))

    a=(x1*((y2*z3)-(y3*z2)))-(y1*((x2*z3)-(x3*z2)))+(z1*((x2*y3)-(x3*y2)))
    print("\n\nDell = ",a)
    if(a==0):
         print("INVALID INPUT\nDell will not be zero")
         sys.exit()

    a1=(p1*((y2*z3)-(y3*z2)))-(y1*((p2*z3)-(p3*z2)))+(z1*((p2*y3)-(p3*y2)))
    print("\nDell I1 = ",a1)

    a2=(x1*((p2*z3)-(p3*z2)))-(p1*((x2*z3)-(x3*z2)))+(z1*((x2*p3)-(x3*p2)))
    print("\nDell I2 = ",a2)

    a3=(x1*((y2*p3)-(y3*p2)))-(y1*((x2*p3)-(x3*p2)))+(p1*((x2*y3)-(x3*y2)))
    print("\nDell I3 = ",a3)

    i1=round(a1/a,4)
    i2=round(a2/a,4)
    i3=round(a3/a,4)

    print("\nI1 = ",i1,"A")
    print("\nI2 = ",i2,"A")
    print("\nI3 = ",i3,"A")

    print("\nI1 + I2 = ",abs(round(i1+i2,4)),"A")
    print("\nI1 + I3 = ",abs(round(i1+i3,4)),"A")
    print("\nI2 + I3 = ",abs(round(i2+i3,4)),"A")
    print("\nI1 - I2 = ",abs(round(i1-i2,4)),"A")
    print("\nI1 - I3 = ",abs(round(i1-i3,4)),"A")
    print("\nI2 - I3 = ",abs(round(i2-i3,4)),"A")
else:
    print("INVALID INPUT")
#udaya 19CSR118
#whatsup no :9788676364
#please report if you find any problem
#happy codding
