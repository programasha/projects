def plus(num1, num2):
    print(num1 + num2)
def minus(num1, num2):
    print(num1 - num2)
def multiply(num1, num2):
    print(num1 * num2)
def devision(num1, num2):
    if num2 == 0:
        print("DO NOT DIVIDE BY ZERO!!!")
    else:
        print(num1 / num2)
def power(num1, num2):
    print(num1 ** num2)
def mod(num1, num2):
    print(num1 % num2)
def root(num1, num2):
    print(num1 ** (1 / num2))

while True:
    s= input()
    if s== "exit":
        break
    num1, op, num2 = s.split(' ')
    num1= int(num1)
    num2= int(num2)
    if op== '+':
        plus(num1, num2)
    elif op== '-':
        minus(num1, num2)
    elif op== '*':
        multiply(num1, num2)
    elif op== '/':
        devision(num1, num2)
    elif op=='^':
        power(num1, num2)
    elif op=='%':
        mod(num1, num2)
    elif op== 'r':
        root(num1, num2)
