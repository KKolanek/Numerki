def znajdz_miejsce_zerowe(f, x0, x1, warunek_stopu, liczba_iteracji, epsilon):
    if f()[0] == "wielomian":

        if f(x0) * f(x1) > 0.0:
            return "Nie znaleziono miejsca zerowego w danym przedziale"
        condition = True
        step = 1
        while condition:
            x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
            print("step", step, "x2", x2, )

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            step += 1
            if warunek_stopu == 2:
                condition = abs(f(x2)) > epsilon
            elif step > liczba_iteracji:
                condition = False

        print('\nRequired root is: %0.8f' % x2)
