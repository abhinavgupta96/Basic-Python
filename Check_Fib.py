#To check if entered number is fibonacci
def is_fib(n):
  a=0
  b=1
  l=[]
  if n==0:
    l.append(a)
  elif n==1:
    l.append(b)

  else:
    l=[0,1]
    for i in range(2,n//2):
      c=a+b
      a=b
      b=c
      if b<=n:
        l.append(b)
  print (l)
  if n not in l:
    print("Not Fibonacci")
  else:
    print("Fibonaaci")


is_fib(50)