def cc(p, pr):
    c = p - pr
    return c

sp = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This snack cost {sp} units.")
print("Accepted coins: 1, 5, 10, 25\n")

ti = 0
ci = 0

while True:
    co = int(input("Insert a coin(1, 5, 10 or 25): "))

    if co != 1 and co != 5 and co != 10 and co != 25:
        print("Invalid coin, try again!\n")
        continue
    ti += co
    ci += 1
    print(f"Inserted {co}. Total so far: {ti}\n")

    if ti >= sp:
        print("Enough money inserted!\n")
        break

cd = cc(ti, sp)

print("Dispensing your snack...")

if cd == 0:
    pass
else:
    print(f"Here is your change: {cd} units")

print("\n===== PURCHASE SUMMARY =====")
print("Snack Price: ", sp)
print("Coins Inserted: ", ci)
print("Total Paid: ", ti)
print("Change Given: ", cd)
print("=============================")
print("Thanks for your purchase!")