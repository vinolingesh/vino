g,h=input().split()
g,h=int(g),int(h)
l=list()
for x in range(g+1,h):
  order=len(str(x))
  s=0
  temp=int(x)
  while temp>0:
    digit=temp%10
    s+=digit ** order
    temp//=10
  if(s==x):
    l.append(x)
print(" ".join(str(c) for c in l))
