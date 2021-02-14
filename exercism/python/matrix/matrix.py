from operator import methodcaller

class Matrix:
    def __init__(self, matrix_string):
        rows_arr = matrix_string.splitlines()
        sep_nums = list(map(methodcaller('split', ' '), rows_arr))
        matrix = []
        for arr in sep_nums:
            digits = list(map(int, arr))
            matrix.append(digits)
        self.matrix = matrix

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col = []
        for row in self.matrix:
            col.append(row[index - 1])
        return col
