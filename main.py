# Wybór funkcji
import array as arr
from math import sin, cos
import numpy as np
import matplotlib.pyplot as plt

import Wyniki
from Bisekcja import bisekcja
from Falsi import znajdz_miejsce_zerowe
from Wyniki import oblicz_cos_2x, oblicz_sin_2x, oblicz_sin, oblicz_cos, horner

def polynomial_coefficients(xs, coeffs):

    order = len(coeffs)
    print(f'# This is a polynomial of order {order - 1}.')

    ys = np.zeros(len(xs))  # Initialise an array of zeros of the required length.
    for i in range(order):
        ys += coeffs[i] * xs ** i
    return ys

def wybor_fun():
    wybrana = 0
    print("Wybierz rodzaj funkcji: \n"
          "1. funkcja trygometryczna\n"
          "2. fukcja wielomianowa\n"
          "3. funkcja wykładnicza\n"
          "4. funkcja zlozona\n")
    choice = input("Twój wybór: ")

    if choice == "1":
        print("Wybór f. trygometrycznych:\n"
              "1. sin(x)\n"
              "2. cos(x)\n"
              "3. sin(2x)\n"
              "4. cos(2x)")
        choice2 = input("Twój wybór: ")
        if choice2 == "1":
            wybrana = sin
        elif choice2 == "2":
            wybrana = cos
        elif choice2 == "3":
            wybrana = oblicz_sin_2x
        elif choice2 == "4":
            wybrana = oblicz_cos_2x

    elif choice == "2":
        Wyniki.stopien = input("Podaj stopień wielomianu: ")
        Wyniki.wspolczynniki = [0 for i in range(int(Wyniki.stopien) + 1)]
        for i in range(0,int(Wyniki.stopien) + 1):
            Wyniki.wspolczynniki[i] = int(input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien)-i) + ": "))
        wybrana = Wyniki.horner
        #size = (int(Wyniki.stopien))
        #Wyniki.wspolczynniki = [0]*(size+1)
        #for i in range(size, -1, -1):2
            #Wyniki.wspolczynniki[i] = int(input("Podaj wspołczynnik przy argumencie o potędze " + str(i) + ": "))
        #wybrana = Wyniki.wielomian

    elif choice == "3":
        Wyniki.podstawa = int(input("Podaj podstawe funkcji wykładniczej: "))
        Wyniki.wolny_wykladnicza = int(input("Podaj wyraz wolny do funkcji wykladniczej: "))
        wybrana = Wyniki.wykladnicza

    elif choice == "4":
        print("Wybierz funkcje zewneczna\n"
              "1. sin(x)\n"
              "2. cos(x)\n"
              "3. sin(2x)\n"
              "4. cos(2x)"
              )
        zewneczna = input("Podaj wybor")
        Wyniki.stopien = input("Wpisz stopien wielomianowej funkcje wewneczna ")
        Wyniki.wspolczynniki = [0 for _ in range(int(Wyniki.stopien) + 1)]
        for i in range(0, int(Wyniki.stopien) + 1):
            Wyniki.wspolczynniki[i] = int(input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien) - i) + ": "))
        if zewneczna == "1":
            wybrana = Wyniki.zlozenie_sin
        elif zewneczna == "2":
            wybrana = Wyniki.zlozenie_cos
        elif zewneczna == "3":
            wybrana = Wyniki.zlozenie_sin_2x
        elif zewneczna == "4":
            wybrana = Wyniki.zlozenie_cos_2x

    else:
        print("Zły wybór!!!")

    return wybrana

#xs = np.linspace(0, 9, 10)  # Change this range according to your needs. Start, stop, number of steps.
#a = arr.array(Wyniki.wspolczynniki)
#arr=a.reverse()
#coeffs = [0, 0, 1]  # x^2
#plt.plot(xs, polynomial_coefficients(xs, coeffs))
#plt.axhline(y=0, color='r')  # Show xs axis
#plt.axvline(x=0, color='r')  # Show y axis
#plt.show()
# Wybór metody
print("Wybierz metodę: \n"
      "1. Metoda bisekcji\n"
      "2. Reguła falsi\n")
choice3 = input("Twój wybór: ")
if choice3 != "1" and choice3 != "2":
    print("Zły wybór")

# Kryterium stopu
itera = 0
dokl = 0
print("Wybierz kryterium stopu: \n"
      "1. Ilość iteracji\n"
      "2. Zadana dokładność\n")
choice4 = input("Twój wybór: ")
if choice4 == "1":
    itera = input("Podaj ilość iteracji: ")
elif choice4 == "2":
    dokl = input("Podaj dokładność: ")
else:
    print("Zły wybór")

# Przedział

print("Podaj przedział na którym chcesz znależć miejsce zerowe")
mini = input("Wartość minimalna: ")
maks = input("Watrość maksymalna: ")

# Wynik
if choice3 == "1":
    print("\nWynik: " + str(bisekcja(wybor_fun(), float(mini), float(maks), int(itera), float(dokl), choice4)))
elif choice3 == "2":
    print("\nWynik: " + str(znajdz_miejsce_zerowe(wybor_fun(), float(mini), float(maks), choice4, int(itera), float(dokl))))

