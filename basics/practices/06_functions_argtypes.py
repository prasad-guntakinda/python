
print("====================== Postion Only Arguments====================")

def power1(x,y): # x and y are postion only arguments
    return x**y

print(power1(2,3)) # 8
print(power1(x=3,y=2)) # this still works because we are not enforcing postion only arguments

# enforcing postion only arguments
# x and y are postion only arguments and we are enforcing it by adding / at the end of the arguments 
# / is ignored by the interpreter but it tells us that the arguments before / are postion only arguments
def power_2(x,y, /): 
    return x**y

print(power_2(2,3)) # 8
# print(power_2(x=3,y=2)) # this will raise a TypeError because we are enforcing postion only arguments

print("====================== ===================== ====================")

print("====================== Keyword-Only Arguments====================") 

def func_1(a,b,*,c,d):
    print(a,b,c,d)

def func_2(*args,std_name,branch):
    print(args,std_name,branch)
    
# func_1(1,2) # missing required keyword-only arguments: 'c' and 'd'
func_1(1,2,c=10,d=20) # 1 2 10 20

#func_2(1,2,3) # missing required keyword-only arguments: 'std_name' and 'branch')
func_2(1,2,3,std_name="John",branch="CS") # (1, 2, 3) John CS


print("====================== ===================== ====================")

print("====================== Default Arguments====================") 