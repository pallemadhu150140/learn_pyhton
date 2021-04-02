
def grade(x):
    if(x>=90 and x<=100):
        print("Excellent")
    elif(x>=80 and x<80):
        print("A Grade")
    elif(x>=70 and x<80):
        print("B Grade")
    elif(x>=60 and x<70):
        print("C Grade")
    elif(x>=50 and x<60):
        print("D Grade")
    else:
        print("Remidial")


a=int(input("Enter A subjuct Marks = "))
b=int(input("Enter B subjuct Marks = "))
c=int(input("Enter C subjuct Marks = "))
d=int(input("Enter D subjuct Marks = "))
e=int(input("Enter E subjuct Marks = "))
total = (a+b+c+d+e)/5
print("Total Marks Got = ",total)
grade = grade(total)
