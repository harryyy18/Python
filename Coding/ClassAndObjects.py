class Student:
    #class variable
    no_of_leaves=10
#object Creation
harry=Student()
larry=Student()

#instance Variables
harry.name="Harry"
harry.city="Navsari"
harry.age=19
print(harry.name,harry.city,harry.age)

print(harry.no_of_leaves)
harry.no_of_leaves=12
print(harry.no_of_leaves)
Student.no_of_leaves=15
print(Student.no_of_leaves)
print(harry.no_of_leaves)
