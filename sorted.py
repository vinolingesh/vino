n=int(input())
ist = [int(x) for x in input().split()]
m=sorted(ist)
print(" ".join(str(x) for x in m))
