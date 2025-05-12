def nsm(t,p):
    n=len(t)
    m=len(p)
    for i in range(n-m+1):
        match = True
        for j in range(m):
            if t[i+j]!=p[j]:
                match=False
                break
        if match:print(f"pattern found at index {i}")

t="ABSBSBSBDBDBSBBBB"
p="AB"
nsm(t,p)