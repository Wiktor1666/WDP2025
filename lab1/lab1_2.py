# Importowanie pakietu wikipedia
import wikipedia

# --- Praca z biblioteką wikipedia ---

# Ustawienie języka polskiego dla zapytań
wikipedia.set_lang("pl") # Funkcja set_lang() zmienia domyślny język
print("Ustawiono język na polski.\n")

# Wyświetlenie podsumowania artykułu o Pythonie
try:
    print("--- Podsumowanie artykułu: Python ---\n")
    # Funkcja summary() zwraca krótkie podsumowanie artykułu
    python_summary = wikipedia.summary("Python", sentences=5) # Ograniczamy podsumowanie do 5 zdań
    print(python_summary)
except wikipedia.exceptions.PageError:
    print("Nie znaleziono artykułu 'Python'.")
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Strona 'Python' jest niejednoznaczna. Wybierz jedną z opcji: {e.options}")


# Wyświetlenie adresu URL artykułu o Mauritiusie
try:
    print("\n--- Adres URL artykułu: Mauritius ---\n")
    # Funkcja page() zwraca obiekt strony, z którego można odczytać różne atrybuty
    mauritius_page = wikipedia.page("Mauritius", auto_suggest=False)
    print(f"URL: {mauritius_page.url}") # Atrybut .url zawiera link do strony
except wikipedia.exceptions.PageError:
    print("Nie znaleziono artykułu 'Mauritius'.")


# Wyświetlenie pełnej treści artykułu o Galapagos
try:
    print("\n--- Pełna treść artykułu: Galapagos ---\n")
    # Atrybut .content zawiera całą treść strony w formacie tekstowym
    galapagos_page = wikipedia.page("Galapagos", auto_suggest=False)
    # Wyświetlamy tylko pierwsze 500 znaków dla zwięzłości
    print(galapagos_page.content[:500] + "...")
except wikipedia.exceptions.PageError:
    print("Nie znaleziono artykułu 'Galapagos'.")