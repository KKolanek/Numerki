# Wybór funkcji

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
    stopien = input("Podaj stopień wielomianu: ")
    wspolczynniki = [0 for i in range(int(stopien)+1)]
    for i in range(0,int (stopien)+1):
        wspolczynniki[i] =int (input("Podaj wspołczynnik przy argumencie o potędze " + str(stopien) + ":"))

elif choice == "3":
    podst = input("Podaj podstawe funkcji wykładniczej: ")

else:
    print("Zły wybór!!!")

# Wybór metody

print("Wybierz metodę: \n"
      "1. Metoda bisekcji\n"
      "2. Reguła falsi\n")
choice3 = input("Twój wybór: ")


# Kryterium stopu

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
