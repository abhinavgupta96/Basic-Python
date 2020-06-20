#Program to return the run length encoded String
def encode(m):
  i=0
  encoded=""
  while (i<len(m)):
    count=1
    ch=m[i]
    j=i
    while (j<len(m)-1):
      if m[j]==m[j+1]:
        count+=1
        j=j+1
      else:
        break
    encoded=encoded+str(count)+ch
    i=j+1
  return encoded

print(encode('AAAABBBBCCCCCCCD'))