#     0  1  2
#0-> [1, 2, 3]
#1-> [4, 5, 6]
#2-> [7, 8, 9]

# 1 2 3 -> new line
# 4 5 6 -> new line
# 7 8 9 -> new line

#for num in range(1,10):
#    print(num)


num = 1    
for row in range(3):  # 0 # 1 # 2
    for col in range(3): # 0,1,2 # 0,1,2 # 0,1,2
        print(num, end=" ")
        num = num + 1
    print("")
    

# print star 
         