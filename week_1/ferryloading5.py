import sys
sys.setrecursionlimit(100000)
n=int(input())
def calc(s,i,u):
    if s > t:
        return False,[]
    if i>=len(w):
        if s>=b:
            return True,u
        else:
            return False,[]
    r,l=calc(s+w[i], i+1, u+[i+1])
    if r:
        return r,l
    r,l = calc(s,i+1,u)
    if r:
        return r,l
    return False,[]
while n:
    w=[]
    for _ in range(n):
        w.append(float(input()))
    t=(sum(w)/2)*1.02
    b=(sum(w)/2)*.98
    r,l=calc(0,0,[])
    print(*l)

    n=int(input())