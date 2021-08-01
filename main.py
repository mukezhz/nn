from math import ceil
from utility import take_input, display, init, sum_weight, step, signum, err_calc, update_weight, activation

"""
x1  x2  yd
0   0   0
0   1   0
1   0   0
1   1   1
"""
x1, x2, yd = take_input()
display(x1, x2, yd)

def final_test(x1, x2, yd, w1, w2, th, fn):
    for (i, v) in enumerate(x1):
        print("**********"*6)
        print(f"Checking with w1: {w1:.3} w2: {w2:.3}")
        val = sum_weight(x1[i], w1, x2[i], w2, th)
        yo = float(fn(val))
        err = err_calc(yo, yd[i])
        print(f"x1: {x1[i]}\tx2: {x2[i]}\tyd: {yd[i]}\tyo: {yo:.3}")
        print(f"{fn.__name__}(val): {fn.__name__}({val:.3})\tyo: {yo:.3}\t\terr: {err:.3}")
        print()


def nn(x1, x2, yd):
    w1, w2, th, lr = init()
    err = 0
    fn = activation()
    for (i, v) in enumerate(x1):
        it = 1
        print("**********"*6)
        while True:
            val = sum_weight(x1[i], w1, x2[i], w2, th)
            yo = float(fn(val))
            err = err_calc(yo, yd[i])
            print(f"x1: {x1[i]}\tx2: {x2[i]}\tyd: {yd[i]}\tyo: {yo:.3}")
            print(f"Iteration: {it}\tw1: {w1:.3}\tw2:{w2:.3}")
            print(f"{fn.__name__}(val): {fn.__name__}({val:.3})\tyo: {yo:.3}\t\terr: {err:.3}")
            print()
            if ceil(err) == 0 or it==5:
                print("End of iteration") if it == 5 else print(f"No need to check ERROR")
                break
            else:
                it += 1
                w1, w2 = update_weight(x1[i], w1, x2[i], w2, err, lr)
    last = input("Want to check with final weights?([y]/n)")
    if last == 'n':
        print("You didn't type y.")
    else:
        final_test(x1, x2, yd, w1, w2, th, fn)
    print("Thank you!!!")

nn(x1, x2, yd)
