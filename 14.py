#to check the number input by user which one is greater
a=int(input("Enter the first number:\t"))
b=int(input("Enter the second number:\t"))
c=int(input("Enter the third number:\t"))
if (a>b) and (a>c) :
    largest = a
elif (b>a) and (b>c) :
    largest = b
else :
    largest = c

print("the largest number is",largest )
