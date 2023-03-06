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
    result = 0
    for i in range(len(wspolczynniki)):
        result = x*result + wspolczynniki[i]
    return result

def wielomian(x):
    wynik = 0.0
    con = int(stopien)
    for i in range(con, -1, -1):
        wynik = wynik + wspolczynniki[i] * (x**i)
    return wynik
def zlozenie_sin(x):
    return sin(horner(x))

def zlozenie_cos(x):
    return cos(horner(x))

def zlozenie_sin_2x(x):
    return oblicz_sin_2x(horner(x))

def zlozenie_cos_2x(x):
    return oblicz_cos_2x(horner(x))
