from math import sin, cos

podstawa = 0
wolny_wykladnicza=0
wspolczynniki = []
stopien = 0
def wykladnicza(x):
    return podstawa**x+wolny_wykladnicza
def oblicz_sin(x):
    return sin(x)
def oblicz_cos(x):
    return cos(x)
def oblicz_sin_2x(x):
    return 2*sin(x)*cos(x)
def oblicz_cos_2x(x):
    return cos(x)**2-sin(x)**2
def horner(x):
    wynik = wspolczynniki[0]
    for i in range(1, stopien+1):
        wynik = wynik * x + wspolczynniki[i]

    return wynik

def wielomian(x):
    wynik = 0.0
    con = int(stopien)
    for i in range(con, -1, -1):
        wynik += wspolczynniki[i] * x**con
    return wynik