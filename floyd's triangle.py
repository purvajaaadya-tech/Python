print("Half Pyramid Pattern of numbers (0123...)")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print(j , end="")
    print()