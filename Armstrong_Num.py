#Check if a number is Amrnstrong Number
def armstrong(n):
  s=str(n)
  a=len(s)
  result=0
  l=[]
  for i in s:
    l.append(i)
  
  for i in l:
    i=int(i)
    result+=pow(i,a)
  if result==n:

    print (result,": is Armstrong number")
  else:
    print (result,": is not Armstrong number")
armstrong(1634)
