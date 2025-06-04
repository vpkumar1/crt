def floyds_triangle(rows):
    number = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()
rows = int(input("Enter the number of rows: "))
floyds_triangle(rows)
