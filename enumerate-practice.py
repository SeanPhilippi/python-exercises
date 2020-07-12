example = ['left', 'right', 'up', 'down']

# for i, s in enumerate(example):
    # print(i, s)

new_dict = dict(enumerate(example))

print(new_dict)

[print(i, j, new_dict[j]) for i, j in enumerate(new_dict)]
