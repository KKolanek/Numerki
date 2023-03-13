def bisekcja(fun, mini, maks, itera, dokl, stop):

    x = 0
    condition = True

    if fun(mini) * fun(maks) > 0.0:
        return "Nie znaleziono miejsca zerowego w danym przedziale"
    else:
        step = 1
        while condition:
            print("iteracja: " + str(step))
            x = (maks + mini)/2
            if dokl > abs(mini - x) and stop == "2":
                condition = False
            if fun(x) == 0:
                return x
            if fun(mini) == 0:
                return mini
            if fun(maks) == 0:
                return maks
            elif fun(x) * fun(mini) < 0:
                maks = x
            else:
                mini = x
            if stop == "1" and itera <= step:
                condition = False
            step += 1
        return x
