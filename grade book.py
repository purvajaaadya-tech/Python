gb = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "James": 95,
    "Ethan": 85
}

ts = 0
for s in gb:
    ts +=gb[s]

ca = ts / len(gb)
print(f"class average score: {ca:.2f}\n")

ts = max(gb, key=gb.get)
tsc = gb[ts]

bs = min(gb, key=gb.get)
bsc = gb[bs]

print("top scorer is ", {ts}, "who has gotten", {tsc})
print("bottom scorer is ", {bs}, "who has gotten", {bsc})

ss = input("enter a student's name to see their grade(Alice, Bob, Charlie, James, Ethan): ")

g = gb.get(ss)

if ss in gb:
    print("yay...", {ss}, "'s score is ", {g})
else:
    print("sorry...", {ss}, "could not be found in the grade book!")