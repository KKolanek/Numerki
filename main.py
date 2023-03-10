# Wybór funkcji

from math import sin, cos
import matplotlib.pyplot as plt
import scipy.interpolate as spi
import Wyniki
from Bisekcja import bisekcja
from Falsi import znajdz_miejsce_zerowe
from Wyniki import oblicz_cos_2x, oblicz_sin_2x


def rysuj():
    plt.plot(tab_indeksy, tab_wartosc)
    if isinstance(miejsce_zerowe, float):
        x_val = miejsce_zerowe
        y_interp = spi.interp1d(tab_indeksy, tab_wartosc)(x_val)
        plt.scatter(x_val, y_interp, color='r', marker='o', s=100)
    plt.xlabel('Indeksy')
    plt.ylabel('Wartości')
    plt.grid('show')
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.title('Wykres funkcji')
    plt.show()


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
        Wyniki.wspolczynniki = [0 for _ in range(int(Wyniki.stopien) + 1)]
        for i in range(0, int(Wyniki.stopien) + 1):
            Wyniki.wspolczynniki[i] = int(
                input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien) - i) + ": "))
        wybrana = Wyniki.horner

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
        zewneczna = input("Podaj wybor: ")
        Wyniki.stopien = input("Wpisz stopien wielomianowej funkcje wewneczna: ")
        Wyniki.wspolczynniki = [0 for _ in range(int(Wyniki.stopien) + 1)]
        for i in range(0, int(Wyniki.stopien) + 1):
            Wyniki.wspolczynniki[i] = int(
                input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien) - i) + ": "))
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

    skok = 0.001
    tab_indeksy[0] = float(mini)
    tab_wartosc[0] = wybrana(float(mini))
    i = 1
    x = round(float(mini), 3)
    while x + 0.001 < float(maks):
        x = round((float(mini) + skok), 3)
        tab_indeksy[i] = x
        tab_wartosc[i] = wybrana(x)
        skok += 0.001
        i += 1
    return wybrana


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

miejsce_zerowe = 0
tab_indeksy = [0] * (int((float(maks) - float(mini)) * 1000) + 1)
tab_wartosc = [0] * (int((float(maks) - float(mini)) * 1000) + 1)


if choice3 == "1":
    miejsce_zerowe = bisekcja(wybor_fun(), float(mini), float(maks), int(itera), float(dokl), choice4)
    print("\nWynik: " + str(miejsce_zerowe))
elif choice3 == "2":
    miejsce_zerowe = znajdz_miejsce_zerowe(wybor_fun(), float(mini), float(maks), choice4, int(itera), float(dokl))
    print("\nWynik: " + str(
        miejsce_zerowe))
    print(tab_indeksy)
rysuj()