def nat(number=1, step=1):
    counter = number
    while True:
        yield counter
        counter += step

for i in nat():
    print(i)