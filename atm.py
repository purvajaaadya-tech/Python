print("=== ATM CASH DISPENSER ===\n")
t100 = t50 = t20 = t10 = t5 = t1 = 0

cs = 0
td = 0

s = True
while s:
    n = input("Enter customer name: ")
    a = int(input(f"Hello {n}! Enter withdrawal amount: "))

    if a <= 0:
        print("Invalid amount. Please enter a positive number. \n")
        continue

    print(f"\nDispensing {a} units for {n}: ")
    r = a
    idx = 1
    while idx <= 6:

        if idx == 1: v = 100
        elif idx == 2: v = 50
        elif idx == 3: v = 20
        elif idx == 4: v = 10
        elif idx == 5: v = 5
        else: v = 1
        c = r // v
        if c > 0:
            print(f"{c} x {v}-unit note(s) = {c * v}")

            r -= c * v
            if v == 100: t100 += c
            elif v == 50: t50 += c
            elif v == 20: t20 += c
            elif v == 10: t10 += c
            elif v == 5: t5 += c
            else: t1 += c
        idx += 1

    cs += 1
    td += a
    print(f"Transaction complete, {n}!\n ")
    ag = input("Next customer? (yes/no): ").strip().lower()
    if ag != "yes":
        s = False

print("\n=== DAILY DENOMINATION REPORT ===")
for sl in range(1, 7):
    if sl == 1: v, t = 100, t100
    elif sl == 2: v, t = 50, t50
    elif sl == 3: v, t = 20, t20
    elif sl == 4: v, t = 10, t10
    elif sl == 5: v, t = 5, t5
    else: v, t = 1, t1
    if t > 0:
        print(f"{v}-unit notes dispensed: {t}", end="")
        for no in range(t):
            print("=", end="")
        print()

print(f"\nCustomers served: {cs}")
print(f"Total dispensed: {ts} units")
print("===== ATM SESSION CLOSED =====")