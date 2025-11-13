import math


def niepodzielne():
    n = int(input("Wpisz liczbę naturalną: "))
    wynik = 0
    if n >= 0:
        for i in range(1, n+1):
            if i % 3 != 0 and i % 5 != 0:
                wynik += 1
        print(wynik)
    else:
        print("Wpisana liczba nie jest naturalna.")

def nieparzyste(n):
    wynik = 0
    for i in range(1, n+1):
        liczba = abs(int(input("Wpisz liczbę naturalną: ")))
        if liczba % 2 != 0:
            wynik += 1
    return wynik

def obliczenie(n):
    wynik = 0
    mianownik = 0
    for i in range(1, n+1):
        mianownik += math.cos(i)
        wynik += 1 / mianownik
    print(wynik)

def main():
    #print("Zadanie 1.")
    #niepodzielne()
    #print("Zadanie 2.")
    #n = abs(int(input("Wpisz liczbę naturalną: ")))
    #print(nieparzyste(n))
    #print("Zadanie 3.")
    #n = abs(int(input("Wpisz liczbę naturalną: ")))
    #obliczenie(n)
main()