from operator import methodcaller

class Matrix:
    def __init__(self, matrix_string):
        rows_arr = matrix_string.splitlines()
        sep_nums = list(map(methodcaller('split', ' '), rows_arr))
        self.matrix = [list(map(int, arr)) for arr in sep_nums]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
