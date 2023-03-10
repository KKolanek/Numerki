def bisekcja(fun, mini, maks, itera, dokl, stop):

    x = 0
    condition = True

    if fun(mini) * fun(maks) > 0.0:
        return "Nie znaleziono miejsca zerowego w danym przedziale"
    else:
        step = 1
        while condition:
            x = (maks + mini)/2
            if dokl > abs(mini - x) and stop == "2":
                condition = False
            if fun(x) * fun(mini) < 0:
                maks = x
            elif fun(x) == 0:
                return x
            else:
                mini = x
            if stop == "1" and itera <= step:
                condition = False
            step += 1
        return x
