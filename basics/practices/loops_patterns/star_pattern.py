# star pattern
#*
#* *
#* * * 
#* * * *

# row -> 0 -> *
# row -> 1 -> * *
# row -> 2 -> * * *
# row -> 3 -> * * * * 

def pattern1():
    for row in range(4): # 0,1,2,3
        for _ in range(row+1): # 1,2,3,4
            print("*",end=" ")
        print("")
    


pattern1()