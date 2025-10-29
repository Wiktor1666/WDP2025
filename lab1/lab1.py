# Importowanie pakietu os
import os
# Importowanie pakietu Faker
from faker import Faker

# Wyświetlenie bieżącego katalogu roboczego
print(f"Bieżący katalog roboczy: {os.getcwd()}")
# Funkcja getcwd() zwraca ścieżkę do aktualnego katalogu

# Wyświetlenie identyfikatora bieżącego procesu
print(f"Identyfikator bieżącego procesu: {os.getpid()}")
# Funkcja getpid() zwraca ID procesu, w którym uruchomiony jest skrypt

# Ścieżka do nowego katalogu
dir_name = "test"

# Utworzenie katalogu o nazwie "test"
try:
    os.mkdir(dir_name) # Funkcja mkdir() tworzy nowy katalog
    print(f"Utworzono katalog: '{dir_name}'")
    # Usunięcie utworzonego katalogu "test"
    os.rmdir(dir_name) # Funkcja rmdir() usuwa pusty katalog
    print(f"Usunięto katalog: '{dir_name}'")
except FileExistsError:
    print(f"Katalog '{dir_name}' już istnieje. Usuwanie...")
    os.rmdir(dir_name)
    print(f"Usunięto katalog: '{dir_name}'")

print("\n--- Generowanie danych za pomocą biblioteki Faker ---\n")

# Inicjalizacja generatora Faker
fake = Faker('pl_PL')
# Tworzymy instancję klasy Faker dla języka polskiego

# Wyświetlenie losowego imienia i nazwiska
print(f"Losowe imię i nazwisko: {fake.name()}")
# Metoda name() generuje imię i nazwisko

# Wyświetlenie losowego adresu
print(f"Losowy adres: {fake.address()}")
# Metoda address() generuje pełny adres pocztowy

# Wyświetlenie losowego tekstu
print(f"Losowy tekst: {fake.text()}")
# Metoda text() generuje fragment losowego tekstu

print("\n--- Sprawdzenie unikalności generowanych danych ---\n")

# Sprawdzenie, czy kolejne wywołania generują różne wyniki
print("Próba 1:")
print(f"Imię i nazwisko: {fake.name()}")
print(f"Adres: {fake.address()}")

print("\nPróba 2:")
print(f"Imię i nazwisko: {fake.name()}") # Ponowne wywołanie metody name()
print(f"Adres: {fake.address()}") # Ponowne wywołanie metody address()