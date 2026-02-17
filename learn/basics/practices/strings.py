
index0 = "Hello"[0]
indexNeg = "World"[-2]
print(index0)
print(type(index0))
print(indexNeg)

greet = "Hey There!"

print("greet", greet)
print(type(greet))
print(greet[4])

print("greet= ", greet)
print("slice: [0:3] ", greet[0:3])  # 0,1,2
print("slice: [0:7] ", greet[0:7])  # 0,1,2,3,4,5,6
print("slice: [0:7:2] ", greet[0:7:2])  # 0,2,4,6
print("slice: [::] ", greet[::])  # everything
print("slice: [::-1] ", greet[::-1])  # reverse string


# Properties & Methods of Strings
# Strings are immutable
print("greet.upper(): ", greet.upper())  # convert to uppercase
print("greet.lower(): ", greet.lower())  # convert to lowercase
print("greet", greet)  # original string remains unchanged

# split string into list
print("greet.split(): ", greet.split())  # default split by space
print("greet.split(e): ", greet.split('e'))  # split by 'e'


# formatting
name = "John"
age = 30
print("My name is {} and I am {} years old".format(name, age))
print("My name is {1} and I am {0} years old".format(age, name))  # positional arguments
print("My name is {n} and I am {a} years old".format(n=name, a=age))  # keyword arguments
print("My name is {n} and I am {a} years old".format(a=age, n=name))  # order doesn't matter
print("My name is {:s} and I am {:d} years old".format(name, age))  # type specifiers
print("My name is {:10s} and I am {:5d} years old".format(name, age))  # width

print(f"My name is {name} and I am {age} years old")  # f-string (Python 3.6+)
print("My name is %s and I am %d years old" % (name, age))  # old style
# %s - string, %d - integer, %f - float
pi = 3.14159
print("Value of pi: %.2f" % pi)  # 2 decimal places
# width and precision
print("Value of pi: %8.3f" % pi)  # width 8, 3 decimal places
# width 8, 3 decimal places, right aligned
print("Value of pi: % -8.3f!" % pi)  # left aligned
# fill with zeros
