print("=============================== Question-1: Even or Odd =============================== ")


def printOdd():
    print("Odd")
    print("This is the end of the odd")
    print("Step out before this line")

def printEven():
    print("Even")
    
      
num = 11
print("num: ",num, end=" ")
if num%2 == 0:
    printEven()
else:
    printOdd()
    

print("This is the end of the program")
# break points
# debug options
# continue: |> continue to the next break point
# step over: |> step into the next line of code, if the line of code is a function call, it will step into the function and stop at the first line of the function
# step into: |> step into the next line of code, if the line of code is a function call, it will step into the function and stop at the first line of the function, if the line of code is not a function call, it will step into the next line of code
# step out: |> step out of the current function and stop at the line of code where the function was called  

    