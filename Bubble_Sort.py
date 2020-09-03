def bubble_sort(l):
  print ("Given array:", l, end='\n')
  for i in range (len(l)):
    #Last i elements are already in order
    for j in range (0,len(l)-i-1):
      if l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
        print (l)
  print ("Final Sorted : ", l)
  

print (bubble_sort([33,2,63,20,5,31,54,1]))