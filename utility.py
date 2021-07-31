#!/usr/bin/python
from math import exp

def take_input():
    print("Enter x1: default=0 0 1 1")
    temp = input()
    x1 = [0,0,1,1] if len(temp) != 4 else [int(x) for x in temp.split()]
    print("Enter x2: default=0 1 0 1: ")
    temp = input()
    x2 = [0,1,0,1] if len(temp) != 4 else [int(x) for x in temp.split()]
    print("Enter 1 for AND", "Enter 2 for OR", "Enter 3 for XOR", "Enter 4 for XNOR", "Enter 5 for NOR", "Enter 6 for NAND", "*********************","Default = AND", sep="\n")
    print("Enter y: ", end='')
    temp = input()
    options = {
            "1": [0,0,0,1],
            "2": [0,1,1,1],
            "3": [0,1,1,0],
            "4": [1,0,0,1],
            "5": [1,0,0,0],
            "6": [1,1,1,0]
            }
    yd = options[temp] if temp in options and len(temp) == 1 else [0,0,0,1]
    return (x1[:], x2[:], yd[:])

def display(x1, x2, yd):
    print("****************************")
    print("Your input")
    print("****************************")
    print("x1\tx2\tyd")      
    for i, v in enumerate(yd):
        print(f"{x1[i]}\t{x2[i]}\t{yd[i]}")

# initialization
def init():
    while True:
        th = input("Enter threshold [default=1.0]:  ")
        lr = input("Enter learning rate [default=0.4]: ")
        w1 = input("Enter weight 1 [default=0.1]: ")
        w2 = input("Enter weight 2 [default=0.2]: ")
        try:
            th = 1.0 if th == '' else float(th)
            lr = 0.4 if lr == '' else float(lr) 
            w1 = 0.1 if w1 == '' else float(w1)
            w2 = 0.2 if w2 == '' else float(w2)
        except:
            print("Please enter the number only")
        else: 
            break
    return w1, w2, th, lr

# activation
def calc(x1, w1, x2, w2, th):
    return x1*w1 + x2*w2 - th
# Depending upon function

# Unit step
def step(v):
    if v >= 0:
        return 1
    return 0
# Signum
def signum(v):
    return 1 / ( 1 + exp(-v) )

def activation():
    print("Select the funtion:","1 for unit step function[DEFAULT]", "2 for signum function", sep="\n")
    fn = input("Enter value: ")
    if fn == '' or fn=='1':
        return step
    if fn == '2':
        return signum

# compare with desired output
def err_calc(yo, yd):
    return yd - yo

# weight update
def update_weight(x1, w1, x2, w2, err, lr):
    print(f"w1 = {w1:.3} + {lr} * {err:.3} * {x1}", end='\t ')
    w1 = w1 + lr * err * x1
    print(f"= {w1:.3}")

    print(f"w2 = {w2:.3} + {lr} * {err:.3} * {x2}", end='\t ')
    w2 = w2 + lr * err * x2
    print(f"= {w2:.3}")
    print()
    return w1, w2
