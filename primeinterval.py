i,j=input().split()
i,j=int(i),int(j)
h=list()
for x in range (i+1,j):
  for k in range(2,x):
    if (x%k==0):
      break
  else:
    h.append(x)
print(" ".join(str(z) for z in h))
