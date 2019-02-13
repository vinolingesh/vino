sum=0
n,k=input().split()
n,k=int(n),int(k)
arr=list()
for i in range (0,n):
  h=int(input())
  arr.append(h)
for i in range (0,k):
  sum=sum+arr[i]
print(sum)
