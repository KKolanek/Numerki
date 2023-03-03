import Falsi
from Wyniki import horner

print("Wybierz rodzaj funkcji: \n"
      "1. funkcja trygometryczna\n"
      "2. fukcja wielomianowa\n"
      "3. funkcja wykładnicza\n")
choice = input("Twój wybór: ")

if choice == "1":
    print("Wybór f. trygometrycznych:\n"
          "1. sin(x)\n"
          "2. cos(x)\n"
          "3. sin(2x)\n"
          "4. cos(2x)")
    choice2 = input("Twój wybór: ")

elif choice == "2":
    stopien = int (input("Podaj stopień wielomianu: "))
    wspolczynniki=[0 for x in range(stopien+1)]

    for i in range(0,stopien+1):
        wspolczynniki[i]= int (input("Podaj wspolczynniki przy potedze"))
    Falsi.znajdz_miejsce_zerowe("dokladnosc",0.000001,-1,10,100)

elif choice == "3":
    podst = input("Podaj podstawe funkcji wykładniczej: ")


else:
    print("Zły wybór!!!")