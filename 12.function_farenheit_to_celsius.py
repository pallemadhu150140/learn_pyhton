def celcius(x):
    y = (5/9)* (x-32)
    return y
a = int(input("Enter Farenheit Value : "))
b = celcius(a)
print("The Celsius Degree is = ",b)