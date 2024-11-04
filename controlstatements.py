temperature = int(input("Enter Temperature:"))

if temperature > 25:
    print("It is too hot")

else:
    print("It is too cold")

#A python program that checks three numbers and returns the smallest
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")

#Program to check whether a number is even or odd

num = 5
if num % 2 == 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

