n=int(input())
ist = [int(x) for x in input().split()]
m=sorted(ist)
l=len(m)
x=(l+1)//2
print(m[x-1])
