num=int(input())
name=input()
list=[name,]
rev=list[0][0:num][::-1]
ist=[]
for i in rev:
  if i=="a" or i=="e" or i=="o" or i=="i" or i=="u":
    continue
  else:
    ist.append(i)    
print("".join(str(x)for x in ist))

