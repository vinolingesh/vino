num=int(input())
order=len(str(num))
s=0
temp=int(num)
while temp>0:
  digit=temp%10
  s+=digit ** order
  temp//=10
if(s==num):
  print("yes")
else:
  print("no")
