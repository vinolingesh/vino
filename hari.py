given =input()
large=0
# print(type(given),len(given))
for i in range(0,len(given)):
  if(given[i]==' '):
    continue
  
  elif(int(given[i])>large):
    large=int(given[i])
print(large)
