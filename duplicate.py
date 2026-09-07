sd = {
    "id1": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

r = {}
sk = []

for sid, d in sd.items():
    uk = (d["name"], d["class"], d["subject_integration"])

    if uk not in sk:
        sk.append(uk)
        r[sid] = d

for k, v in r.items():
    print(k, ":", v)