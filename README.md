# Basic of Neural Network

## Here how you use this simple script

```
python3 main.py
or
python main.py
or
py main.py

Fill the inputs or just type enter for default one.
```

**Note**: I haven't handle the exceptions. Please don't use different datatypes while input

## Example
```
Enter x1: default=0 0 1 1

Enter x2: default=0 1 0 1:

Enter 1 for AND
Enter 2 for OR
Enter 3 for XOR
Enter 4 for XNOR
Enter 5 for NOR
Enter 6 for NAND
*********************
Default = AND
Enter y:
****************************
Your input
****************************
x1      x2      yd
0       0       0
0       1       0
1       0       0
1       1       1
Enter threshold [default=1.0]:
Enter learning rate [default=0.4]:
Enter weight 1 [default=0.1]:
Enter weight 2 [default=0.2]:
Select the funtion:
1 for unit step function[DEFAULT]
2 for signum function
Enter value: 2
************************************************************
x1: 0   x2: 0   yd: 0   yo: 0.269
Iteration: 1    w1: 0.1 w2:0.2
fn(val): fn(-1.0)       yo: 0.269               err: -0.269

No need to check ERROR
************************************************************
x1: 0   x2: 1   yd: 0   yo: 0.31
Iteration: 1    w1: 0.1 w2:0.2
fn(val): fn(-0.8)       yo: 0.31                err: -0.31

No need to check ERROR
************************************************************
x1: 1   x2: 0   yd: 0   yo: 0.289
Iteration: 1    w1: 0.1 w2:0.2
fn(val): fn(-0.9)       yo: 0.289               err: -0.289

No need to check ERROR
************************************************************
x1: 1   x2: 1   yd: 1   yo: 0.332
Iteration: 1    w1: 0.1 w2:0.2
fn(val): fn(-0.7)       yo: 0.332               err: 0.668

w1 = 0.1 + 0.4 * 0.668 * 1       = 0.367
w2 = 0.2 + 0.4 * 0.668 * 1       = 0.467

x1: 1   x2: 1   yd: 1   yo: 0.459
Iteration: 2    w1: 0.367       w2:0.467
fn(val): fn(-0.165)     yo: 0.459               err: 0.541

w1 = 0.367 + 0.4 * 0.541 * 1     = 0.584
w2 = 0.467 + 0.4 * 0.541 * 1     = 0.684

x1: 1   x2: 1   yd: 1   yo: 0.566
Iteration: 3    w1: 0.584       w2:0.684
fn(val): fn(0.268)      yo: 0.566               err: 0.434

w1 = 0.584 + 0.4 * 0.434 * 1     = 0.757
w2 = 0.684 + 0.4 * 0.434 * 1     = 0.857

x1: 1   x2: 1   yd: 1   yo: 0.649
Iteration: 4    w1: 0.757       w2:0.857
fn(val): fn(0.614)      yo: 0.649               err: 0.351

w1 = 0.757 + 0.4 * 0.351 * 1     = 0.898
w2 = 0.857 + 0.4 * 0.351 * 1     = 0.998

x1: 1   x2: 1   yd: 1   yo: 0.71
Iteration: 5    w1: 0.898       w2:0.998
fn(val): fn(0.895)      yo: 0.71                err: 0.29

End of iteration
```

### Thank you
