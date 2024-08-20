size = 7

for col in range(size):
    for row in range(size):
        if col == row or row == size - col - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
