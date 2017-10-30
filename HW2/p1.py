#### ALGORITHMS HW2 - p1 ####

numInput = int(input())
digits = [9,8,7,6,5,4,3,2]
Inputs = []

for _ in range(numInput):
    Inputs.append(int(input()))

for Input in Inputs:
    res = Input
    entries = []
    while res != 1:
        for d in digits:
            if res % d == 0:
                entries.append(d)
                res = res / d
                break
    if len(entries) == 1:
        entries = [1] + entries
    elif len(entries) == 0:
        entries = [1,1]
    entries.sort()
    print(*entries,sep='')
