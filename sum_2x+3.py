#1. a simple python program to find the value of 2x+3 when x is given bythe user

def f(num):
    total=2*num+3
    print("2 *{} +3 = {}".format(num,total))
    
num= int(input("enter a number: "))
f(num)


