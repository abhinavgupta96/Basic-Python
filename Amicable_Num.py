#Check if numbers are amicable
def amicable(num1,num2):
  c=[]
  d=[]
  result1=0
  result2=0
  for i in range(1,num1+1):
    if num1%i==0:
      c.append(i)
    else:
      continue
  for i in c:
    result1+=i
  result1=result1-c[len(c)-1]

  for i in range(1,num2+1):
    if num2%i==0:
      d.append(i)
    else:
      continue
  for i in d:
    result2+=i
  result2=result2-d[len(d)-1]
  if result2==num1 and result1==num2:
    print ("The numbers entered are amicable")
  else:
    print("The numbers are not amicable")
  print(c)
  print(d)
  print(result1,result2)

amicable(220,284)