class pe:
    def ts(self, n, t):
        l = {}

        for i, n in enumerate(n):
            if t - n in l:
                return (l[t - n], i)
            l[n] = i

v = int(input("enter the sum for which you want to make this search: "))
print("index1=%d, index2=%d" % pe().ts((10,20,30,40,50,60,70),v))