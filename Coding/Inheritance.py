                   #SINGLE INHERITANCE
# class Employee:
#     no_of_leaves=10
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#     def printdetails(self):
#         return f"Name is {self.name}.Role is {self.role}.Salary is {self.salary}.\n"
# class Programmer(Employee):
#       no_of_holiday=50
#       def __init__(self,aname,asalary,arole,aexperience):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#         self.experience=aexperience
#       def printprog(self):
#         return f"Name is {self.name}.Role is {self.role}.Salary is {self.salary}.My coding experience is of {self.experience} years.\n"
# harry=Employee("harry",50000,"software Developer")
# karan=Programmer("Karan",60000,"Data Scientist",10)
# print(harry.printdetails())
# print(karan.printprog()) 
# print(karan.printdetails())  
# print(harry.no_of_leaves)
# print(karan.no_of_leaves)
# print(karan.no_of_holiday)
# # print(harry.printprog) 


# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# d = Dog("Dog", "Doggerman")
# d.make_sound()

# a = Animal("Dog", "Dog")
# a.make_sound()

                          
                          
                          #MULTIPLE INHERITANCE
    
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")
        
# class Mammal:
#     def __init__(self, name, fur_color):
#         self.name = name
#         self.fur_color = fur_color
        
# class Dog(Animal, Mammal):
#     def __init__(self, name, breed, fur_color):
#         Animal.__init__(self, name, species="Dog")
#         Mammal.__init__(self, name, fur_color)
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")
        
                                  
# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

# o  = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show() 
# print(DancerEmployee.mro())


                          
# class Employee:
#   no_of_leaves=8
#   var=10
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def printdetails(self):
#     return f"Name is {self.name}.Role is {self.role}.Salary is {self.salary}.\n"

# class Player:
#   no_of_games=4
#   var=14
#   def __init__(self,aname,agame):
#     self.name=aname
#     self.game=agame
#   def printdetails(self):
#     return f"Player name is {self.name}.Game is {self.game}"
  
# class CoolProgrammer(Employee,Player): #Employee ki method access hogi
#   language="C++"
#   def printlanguage(self):
#     print(self.language)

# harry=Employee("Harry",50000,"Developer")
# shubham=Player("Shubham","Snake and Ladders")
# karan=CoolProgrammer("Karan",10000,"Student")
# print(karan.printdetails())
# karan.printlanguage()
# print(karan.var)
    
                                  #MULTILEVEL INHERITANCE
                                  
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = Dog("tommy", "Black")
# o.show_details()
# print(GoldenRetriever.mro())

                                  
# class Dad:
#   basketball=6
# class Son(Dad):
#   dance=1
#   basketball=55
#   def isdance(self):
#     return f"Yes I dance {self.dance} times"
# class Grandson(Son):
#   dance=6
#   guitar=10
#   def isdance(self):
#     return f"Dance {self.dance} times.Guitar {self.guitar} times."

# jayesh=Dad()
# harry=Son()
# jay=Grandson()
# print(jayesh.basketball)
# print(harry.basketball)
# print(harry.dance)
# print(harry.isdance())
# print(jay.guitar)
# print(jay.dance)
# print(jay.basketball)
# print(jay.isdance())
                                            
                                  