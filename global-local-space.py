x = 200
print(x)


def my():
    global x
    x = 200


my()
print(x)
