from datetime import date


#while loop

#increasing values
number = 20;
while number <= 25:
    print(number)
    number += 1

print(" ")
#decreasing values
count = 105
while count >= 100 :
    print(count)
    count -= 1

#For loop
print(" ")
for x in range(1,5):
    print(x)

print(" ")
for num in range(10,30,2):
    print(num)

#List
languages = ["python", "Java", "Kotlin", "PHP"]
print("")
for lang in languages:
    print(lang)

print(date.today())
print("The date today is: "+str(date.today()))