def znajdz_miejsce_zerowe(f, xmin, xmax, warunek_stopu, liczba_iteracji, epsilon):
    x0 = 0
    if f(xmin) * f(xmax) > 0.0:
        return "Nie znaleziono miejsca zerowego w danym przedziale"
    condition = True
    step = 1
    while condition:
        x0 = xmin - (xmax - xmin) * f(xmin) / (f(xmax) - f(xmin))
        print("step", step, "x2", x0, )
        if warunek_stopu == "2":
            condition = (abs(xmin - x0) > epsilon)

        if f(xmin) * f(x0) < 0:
            xmax = x0
        else:
            xmin = x0

        step += 1
        if step > liczba_iteracji and warunek_stopu == "1":
            condition = False

    return x0
