def inserion_sort(l):
  for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
      l[j+1]=l[j]
      j-=1
    l[j+1]=key
  return l

l=[4,3,2,10,12,5,6]
print ("Entered array:",l,end='\n')
print(inserion_sort(l))
