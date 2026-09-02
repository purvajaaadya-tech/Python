w = (1, 0, 0, 0, 1, 1, 0)
s = 0
r = 0
for i in range(0,7):
    if(w[i]==0):
        r+=1
    else:
        s+=1

if(s>r):
    print("Good weather")
else:
    print("Bad weather")