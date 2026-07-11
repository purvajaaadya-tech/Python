from num2words import num2words

num = input("Enter a number: ")

words = num2words(num, to = 'cardinal')

kword = num2words(num, lang = 'kn')

print(words)
print(kword)