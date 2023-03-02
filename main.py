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

elif choice == "3":
    podst = input("Podaj podstawe funkcji wykładniczej: ")

else:
    print("Zły wybór!!!")