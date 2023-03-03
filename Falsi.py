def f(x):
    return x**2
def znajdz_miejsce_zerowe(warunek_stopu,epsilon,x0,x1,liczba_iteracji):

    condition = True
    step = 1
    while condition:
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print("step",step,"x2",x2,)

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step+=1
        if warunek_stopu=="dokladnosc":
            condition = abs(f(x2)) > epsilon
        elif(step>liczba_iteracji):
            condition=False

    print('\nRequired root is: %0.8f' % x2)
