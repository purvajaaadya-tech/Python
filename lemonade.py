def gc():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you.")

gc()

ppc = float(input("Enter the price per cup in dollars: "))
cs = int(input("Enter the number of cups sold: "))

def ct(price, cups):
    total = price * cups
    return total

tc = ct(ppc, cs)

rt = round(tc, 2)
print("Total cost: ", rt)

ap = float(input("Enter the amount paid by the customer: "))

def cc(paid, total):
    change = paid - total
    return change

cd = cc(ap, rt)
rc = round(cd, 2)

def tym(cups):
    if cups >= 5:
        return "Wow, big order! Thanks so much for your support!"
    else:
        return "Thanks for stopping by the stand!"

cm = tym(cs)

print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price Per Cup: ", ppc)
print("Cups Sold: ", cs)
print("Total Cost: ", rt)
print("Amount Paid: ", ap)
print("Change Due: ", rc)
print(cm)
print("==================================")