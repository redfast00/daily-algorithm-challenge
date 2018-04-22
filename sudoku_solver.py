from copy import deepcopy
from itertools import product


SQUARE_SIZE = 3
SIZE = SQUARE_SIZE ** 2


def occupied_info():
    return [False] * SIZE


def color(s):
    return f"\033[1;31m{s}\033[0;0m"


class Sudoku:
    '''Solves a sudoku with backtracking.

    Input format: a 9x9 list of lists constaining numbers 0-8, None on places not
    filled in yet.

    >>> s = Sudoku.from_empty()
    >>> s.solve()
    >>> s.assert_correctness()
    >>> s = Sudoku.from_tuples([(8, 0, 0), (3, 0, 3)])
    >>> s.solve()
    >>> s.assert_correctness()

    # Disabled this test because it takes too long
    # >>> s = Sudoku.from_tuples([(8,0,3),(1,0,5),(4,1,6),(3,1,7),(5,2,0),(7,3,4),(8,3,6),(1,4,6),(2,5,1),(3,5,4),(6,6,0),(7,6,7),(5,6,8),(3,7,2),(4,7,3),(2,8,3),(6,8,6)]) # From https://www.technologyreview.com/s/426554/mathematicians-solve-minimum-sudoku-problem/
    # >>> s.solve()
    # >>> s.assert_correctness()
    '''
    def __init__(self, sudoku):
        self.rows = [occupied_info() for _ in range(SIZE)]
        self.columns = [occupied_info() for _ in range(SIZE)]
        self.squares = [[occupied_info() for _ in range(SQUARE_SIZE)] for _ in range(SQUARE_SIZE)]
        self.changeable = [[(cell is None) for cell in row] for row in sudoku]
        self.state = deepcopy(sudoku)
        for x, row in enumerate(self.state):
            for y, cell in enumerate(row):
                self.place_number(cell, x, y)
        self.x = 0
        self.y = 0
        self.finished = False

    @classmethod
    def from_tuples(cls, tuples):
        s = cls.from_empty()
        for (number, x, y) in tuples:
            assert s.can_place(number, x, y), 'Invalid board'
            s.place_number(number, x, y)
            s.changeable[x][y] = False
        return s

    @classmethod
    def from_empty(cls):
        sudoku = [[None] * SIZE for _ in range(SIZE)]
        return cls(sudoku)

    def solve(self):
        while not self.finished:
            if not self.changeable[self.x][self.y]:
                self.go_to_next_cell()
            elif self.is_stuck(self.x, self.y):
                # We are 'stuck', go back to a previous state
                self.revert()
            else:
                # Add next number
                current = self.state[self.x][self.y]
                start = 0 if current is None else current + 1
                for candidate in range(start, SIZE):
                    if self.can_place(candidate, self.x, self.y):
                        self.place_number(candidate, self.x, self.y)
                        self.go_to_next_cell()
                        break
                else:
                    # We went trough all possiblities, revert to previous state
                    self.place_number(None, self.x, self.y)
                    self.go_to_previous_cell()
                    self.revert()

    def revert(self):
        while True:
            if not self.changeable[self.x][self.y]:
                self.go_to_previous_cell()
            elif self.is_stuck(self.x, self.y):
                self.place_number(None, self.x, self.y)
                self.go_to_previous_cell()
            else:
                # We are now in a state that can be changed
                break

    def assert_correctness(self):
        squares = [[set() for _ in range(SQUARE_SIZE)] for _ in range(SQUARE_SIZE)]
        rows = [set() for _ in range(SIZE)]
        columns = [set() for _ in range(SIZE)]
        for x, y in product(range(SIZE), repeat=2):
            field = self.state[x][y]
            squares[x // SQUARE_SIZE][y // SQUARE_SIZE].add(field)
            rows[x].add(field)
            columns[y].add(field)
        solution = set(range(SIZE))
        for idx, row in enumerate(rows):
            assert set(row) == solution, f'Row {idx} is incorrect'
        for idx, column in enumerate(columns):
            assert set(column) == solution, f'Column {idx} is incorrect'
        for idx, square_row in enumerate(squares):
            for jdx, square in enumerate(square_row):
                assert set(square) == solution, f'Square ({idx}, {jdx}) is incorrect'

    def place_number(self, new, x, y):
        old = self.state[x][y]
        if old is not None:
            self.state[x][y] = None
            self.squares[x // SQUARE_SIZE][y // SQUARE_SIZE][old] = False
            self.rows[x][old] = False
            self.columns[y][old] = False
        self.state[x][y] = new
        if new is not None:
            self.squares[x // SQUARE_SIZE][y // SQUARE_SIZE][new] = True
            self.rows[x][new] = True
            self.columns[y][new] = True

    def is_stuck(self, x, y):
        return self.state[x][y] == SIZE - 1

    def can_place(self, number, x, y):
        return (not self.rows[x][number] and
                not self.columns[y][number] and
                not self.squares[x // SQUARE_SIZE][y // SQUARE_SIZE][number])

    def go_to_next_cell(self):
        if self.x == SIZE - 1 and self.y == SIZE - 1:
            self.finished = True
        else:
            self.x += (self.y == SIZE - 1)
            self.y = (self.y + 1) % SIZE

    def go_to_previous_cell(self):
        if self.x == 0 and self.y == 0:
            print("Unsolvable")
            self.finished = True
        self.x -= (self.y == 0)
        self.y = (self.y - 1) % SIZE

    def __str__(self):
        result = []
        for x, row in enumerate(self.state):
            line = []
            for y, cell in enumerate(row):
                if cell is None:
                    line.append(' ')
                elif self.changeable[x][y]:
                    line.append(str(cell))
                else:
                    line.append(color(str(cell)))
            result.append(''.join(line))
        return '\n'.join(result)
