#Check if number entered are Strong

def strong(num):
  result=0
  original=num
  c=[]
  i=0
  while(num!=0):
    i=int(num%10)
    num=int(num/10)
    c.append(i)
  print(c)
  for i in c:
    result+=factorial(i)
  print(result)
  if result==original:
    print("Entered number is a Strong Number")
  else :
    print("Entered number is a NOT Strong Number")

def factorial(n):
  result=1
  for i in range(1,n+1):
    result=result*i
  return result

strong(2000)
