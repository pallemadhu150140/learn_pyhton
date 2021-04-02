#solve the Quadratic Equation 
#discrimant = b*b-4ac
#sol1 = -b-sqrt(discriminat)/2a
#sol2 = -b+sqrt(discriminat)/2a

import cmath

a=int(input("Enter A Number = "))
b=int(input("Enter B Number = "))
c=int(input("Enter C Number = "))

d= (b*b)-(4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solutions are {0} and {1}".format(sol1,sol2))