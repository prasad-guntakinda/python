import math

def sum(*nums):
    total = 0
    for num in nums:
        total = total+num
    return total

def min(num1, num2):
    return num1 - num2


def power(num1, num2):
    return math.pow(num1,num2)

std = {
    "Id": 1234,
    "Name": "John"
}