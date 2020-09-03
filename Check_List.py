##code to check numbers which occer more than 1 in a list
def check_list(c):
  i=0
  count=0
  d =[]
  for i in range(len(c)):
    for j in range(i+1,len(c)):
      if c[i]==c[j]:
        
        if c[i] not in d:
          d.append(c[i])
          count+=1
      else:
        continue
  print(count)

a = [1,2,3,4,6,4,5,1,4,10,8,7]
check_list(a) 
