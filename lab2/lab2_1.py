def zad1():
    """
    Napisz program, który obliczy i wydrukuje wynik równania (512-282)/(47*48+5)
    """
    print((512-282)/(47*48+5))


def zad2():
    """
     Napisz program, który pobiera od użytkownika wartość, a następnie przypisuje ją do zmiennej x.
     Następnie program wypisuje ciąg x, 2x, 3x, 4x, 5x oddzielony trzema myślnikami.
    """
    x = int(input("Wprowadź liczbę całkowitą x: "))
    print(x,'---', 2*x,'---', 3*x,'---', 4*x,'---', 5*x)


def zad3():
    """
    Napisz program, który pobiera od użytkownika dwie liczby zmiennoprzecinkowe i mnoży je przez siebie.
    Wynik wyświetl na ekranie.
    """
    y1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
    y2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))
    print(y1 * y2)


def zad4():
    """
    Napisz program, który poprosi użytkownika o wpisanie wagi w kilogramach
    i przekonwertuje podaną wartość na funty (kilogram ma około 2,2 funta).
    """
    kg = float(input("Podaj wagę w kilogramach: "))
    funt = 2.2
    print('Podana waga wynosi ', kg * funt)


def zad5():
    """
    Napisz program, który wypisuje sumę pierwszych dziesięciu liczb całkowitych dodatnich, 1 + 2 + ... + 10
    """
    print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)


def zad6():
    """
    Napisz program, który wypisuje iloczyn pierwszych dziesięciu liczb całkowitych dodatnich, 1 + 2 + ... + 10
    """
    print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)


def zad7():
    """
    Napisz program, który wypisuje sumę dni pierwszych trzech miesięcy dowolnego roku przestępnego.
    """
    print(31 + 29 + 31)


def zad8():
    """
    Pozostawiamy pieniądze na lokacie. Kapitał początkowy wynosi 1000 zł, oprocentowanie wynosi 6%,
    a liczba kapitalizacji w ciągu roku k=1. Napisz program, który obliczy kapitalizację odsetek po pierwszym,
    po drugim i po trzecim roku na lokacie.
    """
    lokata = 1000
    oprocentowanie = 0.06
    pierwszy = lokata + (lokata * oprocentowanie)
    drugi = pierwszy + (pierwszy * oprocentowanie)
    trzeci = drugi + (drugi * oprocentowanie)
    print('Po pierwszym roku kapitalizacja odsetek będzie wymosić', pierwszy,
          'zł, po drugim roku', drugi, 'zł, a po trzecim roku', trzeci, 'zł')


def main():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()
    zad8()
main()
