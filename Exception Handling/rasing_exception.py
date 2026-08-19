a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if(b==0):
    raise ZeroDivisionError("Hey our program doesn't let you divide a number by 0")
else:
    print(f"The division is {a/b}")
