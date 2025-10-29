import math


def zad1():
    """
    Napisz program, który wczyta z klawiatury liczbę zmiennoprzecinkową
    i używając prostej instrukcji warunkowej wypisze na ekran wartość
    bezwzględną tej liczby. W tym programie nie należy używać funkcji
    wbudowanej abs.
    """
    n = float(input("Wpisz liczbę zmiennoprzecinkową: "))
    if n < 0:
        n = n * (-1)
    return n


def zad2():
    """
    Napisz funkcję sgn(x), która zwraca znak (inaczej: signum) swojego argumentu.
    (Znak liczby dodatniej jest równy 1, znak liczby ujemnej jest równy -1,
    a znak liczby 0 jest równy 0.) W funkcji main wczytaj liczbę zmiennoprzecinkową,
    a następnie wypisz na ekran jej znak.
    """

    number = float(input("Wczytaj liczbę zmiennoprzecinkową: "))

    def sgn(number):
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0

    print(sgn(number))


def zad3():
    """
    Napisz program, który wczyta dwie liczby zmiennoprzecinkowe,
    a następnie wypisze wynik z dzielenia pierwszej przez drugą,
    o ile druga liczba jest różna od zera. Jeżeli dzielenie nie będzie
    możliwe, to należy wypisać na ekran odpowiedni komunikat.
    """
    try:
        liczba1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
        liczba2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))

        if liczba2 != 0:
            wynik = liczba1 / liczba2
            print(wynik)
        else:
            print("Dzielenie przez 0 jest niemożliwe.")
    except ValueError:
        print("Wprowadzono niepoprawne dane.")


def zad4():
    """
     Napisz program znajdujący pierwiastek równania liniowego ax+b = 0.
     W przypadku gdy a = 0, program powinien wypisać odpowiedni komunikat.
    """
    print("Obliczenie pierwiastka z równania liniowego ax+b = 0.")
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    if a == 0:
        if b == 0:
            print("Nieskończenie wiele rozwiązań")
        else:
            print("Równanie sprzeczne, brak rozwiązań.")
    else:
        x = -b / a
        print("Pierwiastek wynosi:", x)


def zad5():
    """
     Napisz program, który wczyta trzy liczby zmiennoprzecinkowe, a następnie
     wypisze najmniejszą i największą liczbę. W tym programie nie należy
     używać funkcji wbudowanych min oraz max.
    """
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    if a > b and a > c:
        if b > c:
            print("Największa liczba z podanych trzech to", a, ", a najmniejsza to", c)
        else:
            print("Największa liczba z podanych trzech to", a, ", a najmniejsza to", b)
    elif b > a and b > c:
        if a > c:
            print("Największa liczba z podanych trzech to", b, ", a najmniejsza to", c)
        else:
            print("Największa liczba z podanych trzech to", b, ", a najmniejsza to", a)
    else:
        if a > b:
            print("Największa liczba z podanych trzech to", c, ", a najmniejsza to", b)
        else:
            print("Największa liczba z podanych trzech to", c, ", a najmniejsza to", a)


def zad6():
    def max3(x, y, z):
        najwieksza_dotychczas = x

        if y > najwieksza_dotychczas:
            najwieksza_dotychczas = y

        if z > najwieksza_dotychczas:
            najwieksza_dotychczas = z

        return najwieksza_dotychczas

    try:
        a = float(input("Podaj pierwszą liczbę (a): "))
        b = float(input("Podaj drugą liczbę (b): "))
        c = float(input("Podaj trzecią liczbę (c): "))

        najwieksza = max3(a, b, c)

        najmniejsza = -max3(-a, -b, -c)

        print("-" * 30)
        print(f"Wprowadzone liczby: {a}, {b}, {c}")
        print(f"Najmniejsza liczba to: {najmniejsza}")
        print(f"Największa liczba to: {najwieksza}")

    except ValueError:
        print("\nBłąd: Wprowadzono niepoprawną wartość.")
        print("Należy podać liczby (np. 12.5, -4 lub 0).")


def zad7():
    try:
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        c = float(input("Podaj długość boku c: "))

        warunek_spelniony = (a + b > c) and (a + c > b) and (b + c > a)

        if warunek_spelniony:

            obwod = a + b + c

            s = obwod / 2

            pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

            print(f"Obwód trójkąta wynosi: {obwod}")
            print(f"Pole trójkąta wynosi: {pole}")

        else:
            print("\nTo nie są boki trójkąta! Kończę program.")

    except ValueError:
        print("\nBłąd: Wprowadzono niepoprawną wartość (np. 'abc').")
        print("Należy podać liczby. Kończę program.")

def main():
    print(zad1())
    #print(zad2())
    #print(zad3())
    #print(zad4())
    #print(zad5())
    #print(zad6())
    #print(zad7())

main()
