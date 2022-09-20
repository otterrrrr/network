N = input()
for i in range(int(N)):
    a, b = map(int, input().split(" "))
    c = list(map(int, input().split(" ")))

    d = [float("inf")] * (b+1)
    d[0] = 0

    for j in range(1, b+1, 1):
        for k in range(len(c)):
            if j >= c[k]:
                d[j] = min(d[j], 1+d[j-c[k]])
    
    print(d[b])