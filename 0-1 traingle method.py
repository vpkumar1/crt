def zero_one_triangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
zero_one_triangle(5)

