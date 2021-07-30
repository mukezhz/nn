from math import ceil
from utility import take_input, display, init, calc, step, signum, err_calc, update_weight, activation

"""
x1  x2  yd
0   0   0
0   1   0
1   0   0
1   1   1
"""
x1, x2, yd = take_input()
display(x1, x2, yd)

def nn(x1, x2, yd):
    w1, w2, th, lr = init()
    err = 0
    fn = activation()
    for (i, v) in enumerate(x1):
        it = 1
        print("**********"*6)
        while True:
            val = calc(x1[i], w1, x2[i], w2, th)
            yo = float(fn(val))
            err = err_calc(yo, yd[i])
            print(f"x1: {x1[i]}\tx2: {x2[i]}\tyd: {yd[i]}\tyo: {yo:.3}")
            print(f"Iteration: {it}\tw1: {w1:.3}\tw2:{w2:.3}")
            print(f"fn(val): fn({val:.3})\tyo: {yo:.3}\t\terr: {err:.3}")
            print()
            if ceil(err) == 0 or it==5:
                if it == 5:
                    print("End of iteration")
                else:
                    print(f"No need to check ERROR")
                break
            else:
                it += 1
                w1, w2 = update_weight(x1[i], w1, x2[i], w2, err, lr)


nn(x1, x2, yd)
