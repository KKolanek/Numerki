from math import sin, cos
podstawa = 0
def wykladnicza(x):

    return podstawa**x
def oblicz_sin(x):
    return sin(x)
def oblicz_cos(x):
    return cos(x)
def oblicz_sin_2x(x):
    return 2*sin(x)*cos(x)
def oblicz_cos_2x(x):
    return cos(x)**2-sin(x)**2
def horner(wspolczynniki, stopien, wartosc_x):
    wynik = wspolczynniki[0]
    for i in range(1, stopien+1):
        wynik = wynik * wartosc_x + wspolczynniki[i]

    return wynik