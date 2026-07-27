tc = 4
oc = tc
print(f"You have {oc} chores to finish today!\n")

cc = 0
cn = 1

while cn <= tc:
    if cn == 1: nc = "Make your bed!"
    elif cn == 2: nc = "Feed the pet!"
    elif cn == 3: nc = "Take out the trash!"
    else: nc = "Wash the dishes"

    answer = input(f"Have you finished: {nc}? (yes/no): ")

    if answer == "yes":
        cc += 1
        cn += 1
        print("Great job! Chore completed.")

    else:
        print("Okay, finish it and check again!")

    print("Chores remaining: ", tc - cc)
    print()

print("====== ALL CHORES COMPLETE! ======")
print("Great work finishing your entire checklist today!\n")

x = 1
help = 1
while(x==1):
    print(x)
    help = help+1
    if (help == 5):
        break