b1 = {"chips", "juice", "cookies", "sandwich"}
b2 = {"juice", "cookies", "chocolate", "fruit"}
b3 = {"chips", "chocolate", "fruit", "juice"}

print("box 1: ", b1)
print("box 2: ", b2)
print("box 3: ", b3)

b1.add("popcorn")
print("after adding popcorn to box 1: ", b1)

ss = b1.intersection(b2)
print("snacks shared by box 1 and box 2: ", ss)

sc = [5, 8, 3, 6]

print("snack counts: ", sc)

sc.append(10)
sc.append(4)

print("after adding new counts: ", sc)

print("count of 8: ", sc.count(8))

sc.reverse()
print("reversed snack counts: ", sc)