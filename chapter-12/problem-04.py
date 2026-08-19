
try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    c=a/b
except ZeroDivisionError as z:
    print("infinite")