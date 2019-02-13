sum=0
n,k=input().split()
n,k=int(n),int(k)
arr=list(map(int,input().split(" ")))
for i in range (0,k):
  sum=sum+arr[i]
print(sum)
