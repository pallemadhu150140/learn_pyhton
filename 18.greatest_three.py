# Greatest of the three Numbers

a=int(input("Enter A Value = "))
b=int(input("Enter B value = "))
c=int(input("Enter C Value = "))

def greatest(x,y,z):
    if(x>y and x>z):
        print("X is the Greatest Number among all",x)
    elif(y>x and y>z):
        print("Y is the Greatest Number among all",y)
    elif(z>x and z>y):
        print("Z is the Greatest Number among all",z)
    
d = greatest(a,b,c)
