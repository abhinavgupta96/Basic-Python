#Python program to Sort the values of first list using second list
#Zip the two lists.
#Create a new, sorted list based on the zip using sorted().

l=[ 0,   1,   1,    0,   1,   2,   2,   0,   1]
l2=["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]

def sort_list(l1,l2):
  l3=list(zip(l1,l2))
  l3=sorted(l3)
  result=[]
  for i,j in l3:
    result.append(j)
  print (result)

sort_list(l,l2)