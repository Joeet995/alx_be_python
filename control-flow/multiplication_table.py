number = int(input("Enter a number to see its multiplication table:"))

for i in range(1, 11):
    x = number
    y = i
    z = number * i
    print(f"{x} * {y} = {z}")