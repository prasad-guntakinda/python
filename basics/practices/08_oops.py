

def greet(username):
    print("Welcome ", username)
    
    
name = "Bhanu"
name2 = "Hello"
greet(name)
greet(name2)


# functions: code reusability

# 100 students

std_id = 1234
std_name = "Bhanu"
batch = 2025
branch = "AI/ML"



std_id = 1235
std_name = "Hari"
batch = 2025
branch = "AI/ML"

year = 3
semister = 2


class Student: # Classification: 

    def __init__(self, id, name, batch, branch):
        self.id = id
        self.name = name
        self.batch = batch
        self.branch = branch
        
    def __str__(self):
        return (f"{self.id}, {self.name}, {self.batch}")
        

std1 = Student(12345, "Bhanu", 2026, "CSC") # Object: 
num = str([1,2,3,4])
print(num)

print(std1)
   
   
class Std:
    def __init__(self):
        print("This function is called", self)

print(Std)
#print(dir(Std)) 

s1 = Std()    

class Person :
    isHuman = True # 
    
    def set_name(self,name):
        self.name = name
    def set_age(self, age):
        self.age = age
        
p1 = Person()
p1.set_name("Bhanu")
print(p1.isHuman)

print(Person.isHuman)

print("===================================")

class Dog:
    
    def __init__(self, breed, weight): # self={} name="bhanu", name.uppercase(),name[0], len(name)
        print("This is Dog constructor")
        print(self.__dict__)
        self.b = breed
        self.w = weight
        print(self.__dict__)
        
    
    def printme():
        print("This is a dog of breed ")  
        
d1 = Dog("abc", 54)
print(d1.b)
print(Dog.printme())
d2 = {}
d2["id"] = 123

print(d2)


# class, object
# class level variables, class level methods
# object level variables, object level methods
# self, __dict__, __init__. 
# private variables, private methods










