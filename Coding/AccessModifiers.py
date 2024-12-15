class Employee:
    no_of_leaves=8
    var=10
    _prot=15
    __priv=20
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name}.Role is {self.role}.Salary is {self.salary}."
    
emp=Employee("Harry",200000,"Developer")
print(emp._prot)
print(emp._Employee__priv)   #Name Mangling
        
        
# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())