

print("====================== Print 1-10 =====================")

for i in range(1,11):
    print(i, end=" ") 

print("\n ================== Printing asteriks triangle for 5 rows:====================")
# 0,0 -> *
# (1,0) (1,1) -> * *
# (2,0) (2,1) (2,2) -> * * *
# (3,0) (3,1) (3,2) (3,3) -> * * * *
for row in range(5):
    for col in range(row):
        print("*", end=" ")
    print() # this will print a new line after each row of asteriks
    



# division operator : %
# remainder equality: == 0
for i in range(1,51): 
    print(i," ", end=" ")
    if i%3 == 0:
        print(i, " divisible by 3")
    else:
        pass
        #print(i, " Not divisible by 3")
        
        
# collect all the 3 divisibles to the list and print the list.

#. [3, 6,9,12,15,]





    
#while condition:
    #body
    
print("=============== While Loop ================")
num = 1
while num<=10: # num=1,2
    print(num, end=" ") # 1,2
    num = num+1 # num = 2,3
    
    
    
print("================== Factorial of a Number ====================")

# fact = 5 => 5x4x3x2x1 = 120

num = 5
num2 = num
fact = 1
while num>=1: # num=5,4,3,2
    fact=fact*num # fact = 1*5,
    num = num-1 # num=4,

print("factorial of ",num2," = ", fact)


# variable initialization
# while condition
# increment/decrement/status update


name = input("enter your name: ") 

while name != "exit": # name= " ", "hello", "Hi"
    print("Welcome ", name)
    name = input("enter your name: ") # name = hello,HI
    

isEngineOn = False

while isEngineOn :
    print("Horn & Lights ok.............")
    
    



    


     
    


