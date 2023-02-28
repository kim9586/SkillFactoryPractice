def list_repeat(list):
    list_values = list.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield  value

for i in list_repeat([1, 2, 3]):
    print(i)