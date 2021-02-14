class Matrix:
    def __init__(self, matrix_string):
        sep_nums = [row.split() for row in matrix_string.splitlines()]
        self.matrix = [[int(i) for i in arr] for arr in sep_nums]

    def row(self, index):
        # return copy of element from matrix, to keep the matrix non-subscriptable
        return matrix[index - 1].copy()

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
