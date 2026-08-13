class Student:
    COLLEGE_NAME="ABCD"
    college_addr = "Hyderabad"
    def __init__(self, id, name): # constructor
        #print("Student Object is getting created......")
        #print(self.__dict__)
        self.id = id
        self.name = name
        #print(self.__dict__)
        
    def full_name(self): # instance methods
        return self.first_name +". "+ self.last_name
    
    @classmethod
    def postal_address(cls): 
        return cls.COLLEGE_NAME + "\n" +" "+ cls.college_addr
    
    @staticmethod
    def marks_sum(*marks): # static methods 
        sum = 0
        for m in marks:
            sum = sum + m
        return sum
    
#MathUtils.pow(2,4)
#CollectionUtils.sort(list/set)
#FileUitls.copyFile(src, dest)





def upper_case_name(std1):
    return std1.first_name.upper()

std = Student() # std={}=self
std.first_name = "Bhanu" # defining variables on object/self reference 
std.last_name = "Ch"
std.uppercase = upper_case_name
#print(std)
print(std.__dict__)
print(std.first_name)
print(" ", std.full_name())
print(std.uppercase(std))
#print("College Name: ", Student.COLLEGE_NAME)
#print("Address: ", std.college_addr)
#Student.COLLEGE_NAME = "xyz"
#print("College Name: ", Student.COLLEGE_NAME)
#print(dir(std))
print("Marks Sum: ", std.marks_sum(50,50,50,50))
print("Postal Address: ", std.postal_address())
#std2 = Student()
#print(std2.__dict__)

# Variables
# 1. Object/Instance variables
# 2. Class level Variables

# Methods
# 1. instance methods
# 2. class level methods
# 3. static/utility methods

# Accessing Class Level variables inside methods:
#Summary of Access Methods
#Method Type	Primary Access Method	Best Practice / Alternative
#Instance Method	self.VARIABLE_NAME	type(self).VARIABLE_NAME or ClassName.VARIABLE_NAME
#Class Method	cls.VARIABLE_NAME	ClassName.VARIABLE_NAME
#Static Method	ClassName.VARIABLE_NAME	No implicit access; must use class name


# 1. Student Class
# 2. College Details
# 3. Methods: gradeCalc(semi, *marks) => semi, grade, full_name, 
# 2. Bank Account: a/c number, name, balance,
# 2.2 methods: deposit(), withdrawl(), transfer(), curr_bal()


