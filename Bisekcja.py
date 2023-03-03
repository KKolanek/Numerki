def bisekcja(fun, mini, maks, itera, dokl):
    x = 0
    if fun(mini) * fun(maks) > 0.0:
        return "Nie znaleziono miejsca zerowego w danym przedziale"

    else:
        for i in range(1, itera):
            x = (maks + mini)/2
            if dokl > abs(maks-mini):
                return x
            else:
                if fun(x) * fun(mini) < 0:
                    maks = x
                else:
                    mini = x
    return x
