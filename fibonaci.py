def recur(n):
    if n <= 1:
        return n
    else:
        return recur(n - 1) + recur(n - 2)

n = 10

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci sequence:")

    for i in range(n):
        print(recur(i))