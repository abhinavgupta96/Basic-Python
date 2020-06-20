#Megre the Tools problem from hackerrank
s="AABCDAAADD"
n=int(input())
l=[]
i=0
a=len(s)
while i< a:
  l.append(s[i:i+n])
  i=i+n
print (l)
result=[]

for i in l:
  merge=""
  for a in i:
    if a not in merge:
      merge+=a
  result.append(merge)
print(*result, sep='\n')
      