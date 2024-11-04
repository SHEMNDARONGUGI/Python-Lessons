from pickle import APPEND

courses = ["MIT", "Cybersecurity", "Datascience"]

print(courses)

#Accessing an element in arrays using index position

print(courses[0])

for x in courses:
    print("Course is", x)

#Adding a new element
courses.append("Web Development")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)

