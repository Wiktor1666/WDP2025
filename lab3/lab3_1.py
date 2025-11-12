import math

def zad1a():
    suma = 0
    for i in range(2,101,2):
        suma += i
    print("Zadanie 1a:", suma)


def zad1b():
    suma = 0
    for i in range(1,101):
        suma += i**2
    print("Zadanie 1b:", suma)


def zad1c():
    suma = 0
    for i in range(1, 64):
        suma += (2 ** i)
    print("Zadanie 1c:", suma)


def zad1d():
    try:
        a = int(input("Podaj pierwszą liczbę (a): "))
        b = int(input("Podaj drugą liczbę (b): "))

        suma = 0
        if a <= b:
            for liczba in range(a, b + 1):
                if liczba % 2 != 0:
                    suma += liczba
        print(f"Suma liczb nieparzystych w zakresie [{a}, {b}] wynosi: {suma}")
    except ValueError:
        print("Błąd: Wprowadzono niepoprawną liczbę. Proszę podać liczby całkowite.")


def zad2a():
    suma = 0
    n = input("Podaj liczbę naturalną: ")
    for i in range(int(n)):
        suma += i
    print("Zadanie 2a:", suma)


def zad2b():
    iloczyn = 1
    n = input("Podaj liczbę naturalną: ")
    for j in range(1, int(n)):
        iloczyn *= j
    print("Zadanie 2b:", iloczyn)


def zad2c():
    n = int(input("Podaj liczbę naturalną: "))
    suma = 0
    for i in range(0, n):
        a = float(input("Podaj liczbę rzeczywistą: "))
        suma = suma + abs(a)
    print("Zadanie 2c:", suma)


def zad2d():
    n = int(input("Podaj liczbę naturalną: "))
    suma = 0
    for i in range(0, n):
        a = float(input("Podaj liczbę rzeczywistą: "))
        suma = suma + math.sqrt(a)
    print("Zadanie 2d:", suma)


def zad2e():
    n = int(input("Podaj liczbę naturalną: "))
    suma = 0
    for i in range(0, n):
        a = float(input("Podaj liczbę rzeczywistą: "))
        suma = suma * abs(a)
    print("Zadanie 2e:", suma)


def zad2f():
    n = int(input("Podaj liczbę naturalną: "))
    suma = 0
    for i in range(0, n):
        a = float(input("Podaj liczbę rzeczywistą: "))
        suma = suma + pow((a), 2)
    print("Zadanie 2f:", suma)


def zad2g():
    return


def zad2h():
    n = int(input("Podaj liczbę naturalną: "))
    suma = 0
    for i in range(1, n + 1):
        a = float(input("Wpisz liczbę rzeczywistą: "))
        suma += math.pow((-1), i + 1) * a
        print(suma)
    print("Zadanie 2h:", suma)

def main():
    #zad1a()
    #zad1b()
    #zad1c()
    #zad1d()
    zad2a()
    #zad2b()
    #zad2c()
    #zad2d()
    #zad2e()
    #zad2f()
    #zad2g()
    #zad2h()
    #zad2i()
main()