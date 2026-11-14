print("=== CURRENCY DENOMINATION CALCULATOR ===\n")
t500 = t200 = t100 = t50 = t20 = t10 = t5 = t2 = t1 = 0

cs = 0
td = 0

s = True
while s:
    n = input("Enter customer name: ")
    a = int(input(f"Hello {n}! Enter amount: "))

    if a <= 0:
        print("Negative amount. Please enter a positive integer. \n")
        continue

    print(f"\nDispensing {a} ruppees for {n}: ")
    r = a
    idx = 1
    while idx <= 6:

        if idx == 1: v = 500
        elif idx == 2: v = 200
        elif idx == 3: v = 100
        elif idx == 4: v = 50
        elif idx == 5: v = 20
        elif idx == 6: v = 10
        elif idx == 7: v = 5
        elif idx == 8: v = 2
        else: v = 1
        c = r // v
        if c > 0:
            print(f"{c} x {v}-unit note(s) = {c * v}")

            r -= c * v
            if v == 500: t500 += c
            elif v == 200: t200 += c
            elif v == 100: t100 += c
            elif v == 50: t50 += c
            elif v == 20: t20 += c
            elif v == 10: t10 += c
            elif v == 5: t5 += c
            elif v == 2: t2 += c
            else: t1 += c
        idx += 1

    cs += 1
    td += a
    print(f"Transaction complete for {n}!\n ")
    ag = input("Next customer? (yes/no): ").strip().lower()
    if ag != "yes":
        s = False

print("\n=== DENOMINATION REPORT ===")
for sl in range(1, 7):
    if sl == 1: v, t = 500, t500
    elif sl == 2: v, t = 200, t200
    elif sl == 3: v, t = 100, t100
    elif sl == 4: v, t = 50, t50
    elif sl == 5: v, t = 20, t20
    elif sl == 6: v, t = 10, t10
    elif sl == 7: v, t = 5, t5
    elif sl == 8: v, t = 2, t2
    else: v, t = 1, t1
    if t > 0:
        print(f"{v}-unit notes dispensed: {t}", end="")
        for no in range(t):
            print("=", end="")
        print()

print(f"\nCustomers served: {cs}")
print(f"Total dispensed: {td} units")
print("===== DENOMINATION SESSION CLOSED =====")