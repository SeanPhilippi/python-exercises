finished = False
todos = []    
while finished == False:
    todo = input('Enter a task for your to-do list. Press <enter> when done: ')
    if len(todo) == 0:
        finished = True
    else:
        todos.append(todo)
        print('Task added.')

print()
print('Your Todo List:')
print('----------------')

for i in todos:
    print(i)

