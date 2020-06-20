#Python code which accepts a message and encrypts it based on rules given below and returns the encrypted message.
#Words at odd position -> Reverse It
#Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

def encrypt(msg):
  l=msg.split(' ')
  a=[]
  result=""
  for i in range (0,len(l)):
    if (i+1)%2!=0:
      a.append(rev(l[i]))
    else:
      a.append(const(l[i]))
  for i in a:
    result=result+i+" "
  print (result)

def rev(c):
  s=""
  l=[""]*len(c)
  j=len(c)-1
  for i in range(0,len(c)):
    l[j]=c[i]
    j-=1
  for a in l:
    s+=a
  return s


def const(word):
  s=""
  l=list(word)
  for i in l:
    if i not in ('a','i','e','o','u','A','I','E','O','U'):
      s+=i
  
  for i in l:
    if i in ('a','i','e','o','u','A','I','E','O','U'):
      s+=i
  return s

encrypt("the sun rises in the east")