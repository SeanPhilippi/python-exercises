class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.arr = matrix_string.splitlines()

    def row(self, index):
        # split on \n characters
        # use index, return list[index]
        return list(map(int, self.arr[index - 1].split()))

    def column(self, index):
        col_list = []
        for i in range(len(self.arr)):
            print('i', i)
            # print('col val', self.arr[i][index - 1])
            col_list.append(self.arr[i].split()[index - 1])
        return list(map(int, col_list))

matrix = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
print(matrix.column(4))
