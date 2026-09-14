i = ["pencil", "eraser", "notebook", "sharpener", "glue"]
sc = [12, 0, 8, 5, 3]

iy = {item: count for item, count in zip(i, sc)}
print("full inventory: ", iy)

isc = [item for item in i if iy[item] > 0]
print("fitems in stock: ", isc)

ci = input("which item do you want to buy: ")

if ci not in iy or iy[ci] == 0:
    print(ci, "is out of stock! stopping the checker.")
    exit()

p = [10, 5, 40, 15, 20]
m = int(input("enter the markup amount to add to every price: "))

mup = list(map(lambda p: p + m, p))
print("marked up prices: ", mup)

ii = i.index(ci)
cp = mup[ii]
print("price of ", ci, "after markup: ", cp)

iy[ci] = iy[ci] - 1
print(ci, "purchased! remaining stock: ", iy[ci])

print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print("item bought: ", ci)
print("price paid: ", cp)
print("updated inventory: ", iy)
print("==========================================")