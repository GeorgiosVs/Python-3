#Version 1 13/11/2024
name = 'Mariza'

def sayHello():
    print('Hello, ' + name)

def changeName(newName):
    global name
    name = newName

sayHello()
changeName('Juan')
sayHello()
changeName('George')
sayHello()