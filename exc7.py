""" Version 2 updated through
def func(a, b=1, c=2):
    print('a =', a, 'και b =', b, 'και c =', c)

func(5, 10)
func(2, c = 20)
func(c = 50, a = 100)"""

import exc8

myNumber1 = 30
myNumber2 = 20

print("Your first number is ", myNumber1)
print("Your second number is ", myNumber2)

print("Append ", exc8.append(myNumber1, myNumber2))

print("Division ", exc8.division(myNumber1, myNumber2))

print("Multiply ",exc8.multiply(myNumber1, myNumber2))