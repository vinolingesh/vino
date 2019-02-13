n=int(input())
l=list()
for x in range(1,6):
  l.append(x*n)
print(" ".join(str(c) for c in l))
