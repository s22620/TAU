import random

rows = 5
cols = 5

ilosc_przeszkod = random.randint(5, rows * cols // 4)
def generuj_plansze(rows, cols):

    plansza = [['-' for _ in range(cols)] for _ in range(rows)]

    start_row = random.choice([0, rows - 1])
    start_col = random.randint(0, cols - 1)
    start = (start_row, start_col)

    stop_row = random.choice([row for row in [0, rows - 1] if row != start_row])
    stop_col = random.randint(0, cols - 1)
    stop = (stop_row, stop_col)

    plansza[start[0]][start[1]] = 'A'
    plansza[stop[0]][stop[1]] = 'B'

    for _ in range(ilosc_przeszkod):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while plansza[row][col] in ['A', 'B', 'X']:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

        plansza[row][col] = 'X'

    return plansza, start, stop

def wyswietl_plansze(plansza, aktualna_pozycja):
    for i, row in enumerate(plansza):
        for j, cell in enumerate(row):
            if (i, j) == aktualna_pozycja:
                print('#', end=' ')
            else:
                print(cell, end=' ')
        print()

def wykonaj_ruch(plansza, aktualna_pozycja, ruch):
    nowa_pozycja = aktualna_pozycja

    if ruch == 'W' and aktualna_pozycja[0] > 0:
        if plansza[aktualna_pozycja[0] - 1][aktualna_pozycja[1]] != 'X':
            nowa_pozycja = (aktualna_pozycja[0] - 1, aktualna_pozycja[1])
    elif ruch == 'S' and aktualna_pozycja[0] < len(plansza) - 1:
        if plansza[aktualna_pozycja[0] + 1][aktualna_pozycja[1]] != 'X':
            nowa_pozycja = (aktualna_pozycja[0] + 1, aktualna_pozycja[1])
    elif ruch == 'A' and aktualna_pozycja[1] > 0:
        if plansza[aktualna_pozycja[0]][aktualna_pozycja[1] - 1] != 'X':
            nowa_pozycja = (aktualna_pozycja[0], aktualna_pozycja[1] - 1)
    elif ruch == 'D' and aktualna_pozycja[1] < len(plansza[0]) - 1:
        if plansza[aktualna_pozycja[0]][aktualna_pozycja[1] + 1] != 'X':
            nowa_pozycja = (aktualna_pozycja[0], aktualna_pozycja[1] + 1)

    if nowa_pozycja == aktualna_pozycja:
        print("Nieprawidłowy ruch! Spróbuj ponownie.")

    return nowa_pozycja

def poruszanie(plansza, start, stop):
    aktualna_pozycja = start

    while True:
        wyswietl_plansze(plansza, aktualna_pozycja)
        ruch = input("Dokąd chcesz się przemieścić? (W, A, S, D): ").upper()
        nowa_pozycja = wykonaj_ruch(plansza, aktualna_pozycja, ruch)

        if nowa_pozycja == aktualna_pozycja:
            print("Nieprawidłowy ruch! Spróbuj ponownie.")
        elif nowa_pozycja == stop:
            print("Gratulacje! Dotarłeś do celu!")
            break
        else:
            aktualna_pozycja = nowa_pozycja

def start_game(rows, cols):
    plansza, start, stop = generuj_plansze(rows, cols)

    # Rozpoczęcie gry
    print("Witaj w grze! Oznaczenia: A - Start, B - Stop, X - Przeszkoda")
    poruszanie(plansza, start, stop)

if __name__ == "__main__":
    start_game(rows, cols)

