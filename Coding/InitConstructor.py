class Employee:
    no_of_leaves=10
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name}.Role is {self.role}.Salary is {self.salary}"
    
    @classmethod  #With the help of class method objects can change class variable
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
     
    @classmethod #classmethod as alternative constructor
    def from_dash(cls,String):
        return cls(*String.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is string:"+string)    

harry=Employee("Harry",50000,"Software Developer")
print(harry.printdetails())
harry.change_leaves(30)
print(harry.no_of_leaves)   
karan=Employee.from_dash("Karan-40000-WebDeveloper")
print(karan.name)   
print(karan.role)
karan.printgood("Harry is me")