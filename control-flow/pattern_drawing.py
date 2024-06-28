rows = int(input("Enter the size of the pattern:"))
J = 0
while rows > 0:
    for i in range(1, rows + 1):
        print("*", end="")
    print()
    J += 1
    if J == rows : break
    
