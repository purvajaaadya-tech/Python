stud = ["Alice", "Sam", "Peter", "Bob", "Charles"]
subjects = ["Math", "English", "History", "L2", "Coding"]

alice = [82, 97, 36, 42, 69]
sam = [76, 95, 16, 35, 99]
peter = [32, 81, 17, 43, 98]
bob = [47, 37, 18, 56, 93]
charles = [0, 1, 2, 3, 4]

tot = [0,0,0,0,0]
avg = [0,0,0,0,0]

total = 0
position = 0
for mark in range(0, len(alice)):
  total += alice[mark]

  tot[position] = total
  avge = total / len(subjects)
  avg[position] = avge

total = 0
position = 1
for mark in range(0, len(sam)):
  total += sam[mark]

  tot[position] = total
  avge = total / len(subjects)
  avg[position] = avge

total = 0
position = 2
for mark in range(0, len(peter)):
  total += peter[mark]

  tot[position] = total
  avge = total / len(subjects)
  avg[position] = avge

total = 0
position = 3
for mark in range(0, len(bob)):
  total += bob[mark]

  tot[position] = total
  avge = total / len(subjects)
  avg[position] = avge

total = 0
position = 4
for mark in range(0, len(charles)):
  total += charles[mark]

  tot[position] = total
  avge = total / len(subjects)
  avg[position] = avge

for mark in range(0, len(stud)):
  print("Sum of marks for", stud[mark], ":", tot[mark])
  print("Average marks for", stud[mark], ":", avg[mark])

for i in range(0, len(avg)):
  if avg[i] >= 91 and 100:
    grade = "S + pass"
  elif avg[i] >= 81 and 90:
    grade = "A + pass"
  elif avg[i] >= 71 and 80:
    grade = "B + pass"
  elif avg[i] >= 61 and 70:
    grade = "C + pass"
  elif avg[i] >= 51 and 60:
    grade = "D + pass"
  elif avg[i] >= 41 and 50:
    grade = "E + pass"
  elif avg[i] >= 0 and 40:
    grade = "Fail"
  else:
    print("Error!")

  print("The grade for", stud[i], "is", grade)

max_val = max(tot)
max_pos = tot.index(max_val)
max_val_pos_name = stud[max_pos]
print("Class topper:", max_val_pos_name, "scoring", max_val, "marks!")

for i in range(0, len(subjects)):
  print(subjects[i], ":")
  print("Alice =", alice[i])
  print("Sam =", sam[i])
  print("Peter =", peter[i])
  print("Bob =", bob[i])
  print("Charles =", charles[i])
