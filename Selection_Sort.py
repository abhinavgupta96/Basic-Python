def selection_sort(l):
  for i in range (len(l)):
    min_indx=i
    for j in range (i+1,len(l)):
      if l[min_indx]>l[j]:
        min_indx=j
    l[i],l[min_indx]=l[min_indx],l[i]

  return l

print (selection_sort([33,21,6,98,1]))

