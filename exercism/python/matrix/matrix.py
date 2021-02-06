class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.arr = matrix_string.splitlines()

    def row(self, index):
        return list(map(int, self.arr[index - 1].split()))

    def column(self, index):
        col_list = []
        for i in range(len(self.arr)):
            col_list.append(self.arr[i].split()[index - 1])
        return list(map(int, col_list))
