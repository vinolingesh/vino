i,j=input().split()
i,j=int(i),int(j)
h=list()
for x in range (i+1,j):
  if(x%2==0):
    h.append(x)
print(" ".join(str(x) for x in h))




