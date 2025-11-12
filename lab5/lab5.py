"""
Do każdego z poniższych punktów napisać odpowiedni program.
W każdym z tych programów wczytać liczbę naturalną n,
a następnie wczytując kolejno n liczb naturalnych obliczyć
ile wśród wczytanych liczb jest takich, które:
"""


def zad1a():
    """
    są liczbami nieparzystymi
    """
    n = abs(int(input("Podaj n: ")))
    count = 0
    for i in range(n):
        num = int(input("Podaj liczbe: "))
        if num % 2 == 1:
            count += 1
    print("Ilość liczb nieparzystych: ", count)

def zad1b():
    """
    są podzielne przez 3 i niepodzielne przez 5
    """
    n = int(input("Podaj n: "))
    count = 0
    for i in range(n):
        num = int(input("Podaj liczbe: "))
        if num % 3 == 0 and num % 5 != 0:
            count += 1
    print("Ilość liczb podzielnych przez 3 i niepodzielnych przez 5: ", count)

def zad1c():
    """
    są kwadratami liczby parzystej
    """
    import math
    n = int(input("Podaj n: "))
    count = 0
    for i in range(n):
        num = int(input("Podaj liczbe: "))
        root = int(math.sqrt(num))
        if root * root == num and root % 2 == 0:
            count += 1
    print("Ilość kwadratów liczb parzystych: ", count)

def zad1d():
    """
    spełniają warunek a_k < (a_(k-1)+a_(k+n))/2 dla 1<k<n
    """
    n = int(input("Podaj n: "))
    if n < 0:
        print("n musi być naturalne")
        return

    count = 0
    first = int(input("Podaj liczbe 1: "))
    second = int(input("Podaj liczbe 2: "))
    for i in range(3, n + 1):
        last = int(input(f"Podaj liczbe {i}: "))
        if second < (first + last) / 2 :
            count += 1
        first = second
        second = last
    print(count)

def zad1e():
    """
    spełniają warunek 2^k <a_k < k! dla 1 <= k <= n
    """
    import math
    n = int(input("Podaj n: "))
    a = []
    for i in range(n):
        a.append(int(input("Podaj liczbe: ")))
    count = 0
    for k in range(1, n):
        left = 2 ** k
        right = math.factorial(k)
        if left < a[k] < right:
            count += 1

    print("Ilość liczb spełniających warunek: ", count)

def zad1f():
    """
    mają nieparzysty numer (numerujemy od 1 do n)
    i sa liczbami parzystymi
    """

def zad1g():
    """
    są nieparzyste i nieujemne
    """

def zad1h():
    """
    spełniają warunek |a_k| < k^2
    """


def main():
#    zad1a()
#    zad1b()
#    zad1c()
#    zad1d()
#    zad1e()
#    zad1f()
#    zad1g()
#    zad1h()

main()

