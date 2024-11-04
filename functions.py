#Built-In Library functions

y = max(34, 78, 56, 10)
print(y)

x = min(54,23,56,42)
print(x)

z = pow(3,4)
print("The result is: ", z)

#User-Defined Functions
def greeting():
    print("Hello there")
greeting() #function call

def add():
    num1 = 7
    num2 = 20
    print(num1 + num2)
add()

def multiply(x,y):
    # return x * y
    print(x * y)
multiply(2,3)
multiply(5,30)

def doctor(name):
    print(name)
doctor("Shem")
doctor("Ndaro")
doctor("Ngugi")