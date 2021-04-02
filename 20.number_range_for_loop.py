#user Input Range taking Input From the User

a = int(input("Enter First value = "))
b = int(input("Enter Last Value = "))

def ran(x,y):
    for values in range(a,b):
        values = values+1
        print(values)
    
c = ran(a,b)
