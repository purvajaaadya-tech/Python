secret = 32

print("=== NUMBER GUESSING GAME ===")
print("Guess the secret number! (1 - 50)")
print("You have 5 attemps to guess the number!(attemps will show like this - *)")

firstguess = int(input("1st guess: "))

if firstguess == secret:
    print("\nYou won the game! Good job.")

else:
    print("Wrong! Here is a clue - i am an even number")
    print("Attempts left: * * * *")

secondguess = int(input("2nd guess: "))

if secondguess == secret:
    print("\nYou won the game! Good job.")
else:
    print("Wrong! Here is a clue - i am below 40")
    print("Attempts left: * * *")


thirdguess = int(input("3rd guess: "))

if thirdguess == secret:
    print("\nYou won the game! Good job.")
else:
    print("Wrong! Here is a clue - i am above 30")
    print("Attempts left: * *")

fourthguess = int(input("4th guess: "))

if fourthguess == secret:
    print("\nYou won the game! Good job.")
else:
    print("Wrong! Here is a clue - i am divisible by 8")
    print("Attempts left: *")

fifthguess = int(input("5th(last) guess: "))

if fifthguess == secret:
    print("\nYou won the game! Good job.")
else:
    print("You lost! - the secret number was 32")

print("\n=== COMPLETED ===")