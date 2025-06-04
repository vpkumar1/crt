rows=int(input("Enter the number of the rows:"))
for i in range(1,rows+1):
    print("*"*i,end=" ")
    print(" "*(2*(rows-i)),end="")
    print("*"*i)
for i in range(rows,0,-1):
    print()    