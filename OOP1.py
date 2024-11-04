class Person:
    #properties/variables/Attributes/Xristics
    def __init__(self, name,age,gender,school):
        self.name = name
        self.age = age
        self.gender = gender
        self.school = school

    #Behaviour/Method/Function
    def study(self):
        print("Student is studying")

        #creating and object
student1 = Person("Hussein",19, "male", "Moringa")
print(student1.name,student1.age,student1.gender,student1.school)
student1.study()
print()

student2 = Person("Wambui",20,"female","Moringa")
print(student2.name,student2.age,student2.gender,student2.school)
student2.study()
print()

student3 = Person("Shem",20, "male", "eMobilis")
print(student3.name,student3.age,student3.gender,student3.school)
student3.study()


