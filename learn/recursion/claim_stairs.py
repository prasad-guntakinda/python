

def climb_stairs(n):
    if n == 0 or n == 1:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(climb_stairs(6))