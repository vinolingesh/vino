n,a,d=input().split()
n,a,d=int(n),int(a),int(d)
sum=0
while n>0:
  sum=sum+(a+((n-1)*d))
  n-=1
print(sum)
