b1 = {"apple", "banana", "mango", "apple", "grape"}
b2 = {"mango", "kiwi", "banana", "kiwi"}
print("Basket 1: ", b1)
print("Basket 2: ", b2)

b1.add("orange")
print("Basket 1 after adding orange: ", b1)

cf = b1.intersection(b2)
print("Fruits in both baskets: ", cf)

import array as arr
fc = arr.array('i', [3, 5, 2, 4])
print("Fruits counts array: ", fc)

fc.insert(0, 1)
fc.append(6)
print("Fruits counts after adding items: ", fc)

co4 = fc.count(4)
print("Number of times 4 appears: ", co4)

fc.reverse()
print("Reversed fruit counts array: ", fc)

print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1: ", b1)
print("Basket 2: ", b2)
print("Shared fruits: ", cf)
print("Fruit counts: ", fc)
print("========================================")