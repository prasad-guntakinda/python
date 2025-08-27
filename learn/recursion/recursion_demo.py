

def display(n):
    if (n > 0):
        print(f"Before n: {n}")
        display(n-1)
        print(f"After n: {n}")


num = 3
display(num)

print("Display Ascending Order:==============")


def dis2(n):
    if (n > 0):
        dis2(n-1)
        print(f"n: {n}")


dis2(3)
