# Factorial (!)

number = (int)(input("Enter a number: "))
factorial = 1
a = 0

while(a<number):
    a = a + 1
    factorial *= a

print(" ")
print("The factorial of", number, "is...", factorial)
