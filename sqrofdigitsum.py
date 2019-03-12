num=int(input())
sum=0
while(num>0):
  num1=num%10
  sum=(num1*num1)+sum
  num=num//10
print(sum)

