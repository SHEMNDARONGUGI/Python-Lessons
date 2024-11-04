



number = 67 #integer
second = 45.98 #Float
greeting = "Hello There" #string
isPythonInteresting = True #Boolean


#Data Structures - Multiple values stored in a single variable
cars = ["Audi", "Mercedes", "BMW"] #List - Ordered and Changeable(mutable)
fruits = ("Mango", "Apple", "Banana", "Passion") #Tuple - Ordered but unchangeable
countries = {"USA", "Kenya", "Tunisia", "Algeria"} #Set - Unordered and unchangeable(immutable)
student = {
    "FirstName" : "Mitchelle",
    "LastName" : "Wambui",
    "age" : 20,
    "Course" : "Hospitality",
    "Gender" : "Female",
} #Dictionary - key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["Course"])


print(number)
print(second)
print(greeting)
print(isPythonInteresting)

#Determining a datatype
print(type(student))
print(type(fruits))

# Typecasting - converting from one datatype to another
print(float(number))
print(int(second))
print(len(fruits))
