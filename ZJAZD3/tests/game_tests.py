import unittest
from io import StringIO
from unittest.mock import patch

from ZJAZD3.src.game import generuj_plansze, rows, cols, wyswietl_plansze, wykonaj_ruch, ilosc_przeszkod


class TestMyGameFunctions(unittest.TestCase):

    def test_generate_board_size(self):

        plansza, start, stop = generuj_plansze(rows, cols)
        self.assertEqual(rows, len(plansza))
        self.assertEqual(cols, len(plansza[0]))

    def test_start_on_boarder(self):

        plansza, start, stop = generuj_plansze(rows, cols)
        start_row, start_col = start
        self.assertTrue(start_row == 0 or start_row == rows - 1 or
                        start_col == 0 or start_col == cols - 1)

    def test_stop_on_boarder(self):

        plansza, start, stop = generuj_plansze(rows, cols)
        end_row, end_col = stop
        self.assertTrue(end_row == 0 or end_row == rows - 1 or
                        end_col == 0 or end_col == cols - 1)

    def test_amount_of_obstacles(self):

        plansza, start, stop = generuj_plansze(rows, cols)
        obstacles_count = sum(row.count('X') for row in plansza)
        self.assertEqual(obstacles_count, ilosc_przeszkod)

    def test_print_board(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        aktualna_pozycja = start
        with patch('sys.stdout', new=StringIO()) as fake_output:
            wyswietl_plansze(plansza, aktualna_pozycja)
            printed_board = fake_output.getvalue().strip()
        self.assertIsInstance(printed_board, str)
        self.assertEqual(len(printed_board.split('\n')), 5)

    def test_movement_up(self):
        while True:
            plansza, start, _ = generuj_plansze(rows, cols)
            plansza[start[0]][start[1]] = '_'

            if start[0] > 0 and plansza[start[0] - 1][start[1]] != 'X':
                new_row, new_col = wykonaj_ruch(plansza, start, 'W')
                self.assertEqual(new_row, start[0] - 1)
                self.assertEqual(new_col, start[1])
                break

    def test_movement_down(self):
        while True:

            plansza, start, _ = generuj_plansze(rows, cols)
            plansza[start[0]][start[1]] = '_'

            if start[0] < rows - 1 and plansza[start[0] + 1][start[1]] != 'X':
                new_row, new_col = wykonaj_ruch(plansza, start, 'S')
                self.assertEqual(new_row, start[0] + 1)
                self.assertEqual(new_col, start[1])
                break
    def test_movement_left(self):
        while True:

            plansza, start, _ = generuj_plansze(rows, cols)
            plansza[start[0]][start[1]] = '_'

            if start[1] > 0 and plansza[start[0]][start[1] - 1] != 'X':
                new_row, new_col = wykonaj_ruch(plansza, start, 'A')
                self.assertEqual(new_row, start[0])
                self.assertEqual(new_col, start[1] - 1)
                break

    def test_movement_right(self):
        while True:

            plansza, start, _ = generuj_plansze(rows, cols)
            plansza[start[0]][start[1]] = '_'

            if start[1] < cols - 1 and plansza[start[0]][start[1] + 1] != 'X':
                new_row, new_col = wykonaj_ruch(plansza, start, 'D')
                self.assertEqual(new_row, start[0])
                self.assertEqual(new_col, start[1] + 1)
                break

    def test_obstacle_detection(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        player_row, player_col = start
        plansza[player_row][player_col] = '_'
        plansza[player_row - 1][player_col] = 'X'
        new_row, new_col = wykonaj_ruch(plansza, start, 'W')
        self.assertEqual(new_row, player_row)
        self.assertEqual(new_col, player_col)

    def test_invalid_movement(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        player_row, player_col = start
        plansza[player_row][player_col] = '_'
        new_row, new_col = wykonaj_ruch(plansza, start, 'Z')
        self.assertEqual(new_row, player_row)
        self.assertEqual(new_col, player_col)
