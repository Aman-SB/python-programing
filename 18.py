# greatest of four number
a=int(input("Enter the number 1 :"))
b=int(input("Enter the number 2 :"))
c=int(input("Enter the number 3 :"))
d=int(input("Enter the number 4 :"))
 
if(a>b):
    F1=a
else:
    F1=b

if(c>d):
    F2=c
else:
    f2=d

if(F1>F2):
    print(str(F1), "is greater")
else:
    print(str(F2), "is greater")
