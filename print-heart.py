grid = [
  ['.', '.', '.', '.', '.', '.'], 
  ['.', '0', '0', '.', '.', '.'], 
  ['0', '0', '0', '0', '.', '.'], 
  ['0', '0', '0', '0', '0', '.'], 
  ['.', '0', '0', '0', '0', '0'], 
  ['0', '0', '0', '0', '0', '.'], 
  ['0', '0', '0', '0', '.', '.'], 
  ['.', '0', '0', '.', '.', '.'], 
  ['.', '.', '.', '.', '.', '.'],  
]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        # print('len of grid', len(grid))
        if j == len(grid) - 1:
            print(grid[j][i])
            # print(range(len(grid)))
        else:
            # print('i', i)
            # print('j', j)
            print(grid[j][i], end='')

