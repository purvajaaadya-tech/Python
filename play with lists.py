l = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list: ", l)

c = 0

for i in l:
    c += i

avg = c/len(l)

print("Sum = ", c)
print("Average = ", avg)

l.sort()

print("Smallest element is: ", l[0])

print("Largest element is: ", l[-1])