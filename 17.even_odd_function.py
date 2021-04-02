# Even Or Odd 
def even(x):
    if(x%2 == 0):
        print("X is Even Number",x)
    elif(x%2 != 0):
        print("X is Odd Number",x)
    elif(x==0):
        print("O is Neither Odd and Nor Even",x)
    else:
        print("Please Check the Number",x)

a=int(input("Enter a Number = "))
c = even(a)