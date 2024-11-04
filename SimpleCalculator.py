a = int(input("INPUT AN INTEGER VALUE: "))
b = int(input("INPUT A SECOND INTEGER VALUE: "))
c = input("INPUT EITHER OF THE VALUES(+ , - , * , /): ")
if c == '+' :
    print("The Sum is:", a + b)
elif c== '-' :
    print("The value after subtraction is:",a - b)
elif c == '/' :
    print("The value after division is:",a/b)
elif c == '*' :
    print("The product is:",a*b)
else:
    print("WRONG INPUT!!!")
