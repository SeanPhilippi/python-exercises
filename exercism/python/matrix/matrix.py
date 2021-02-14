class Matrix:
    def __init__(self, matrix_string):
        sep_nums = [row.split() for row in matrix_string.splitlines()]
        # self.matrix = [list(map(int, arr)) for arr in sep_nums]
        self.matrix = [[int(i) for i in arr] for arr in sep_nums]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
