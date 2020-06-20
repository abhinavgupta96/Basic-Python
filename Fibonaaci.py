def fib(n):
  a=0
  b=1
  if n<0:
    print("incorrect output")
  elif n==0:
    print (a)

  elif n==1:
    print (b)

  else:
    for i in range(2,n):
      c=a+b
      a=b
      b=c
    print(b)

fib(10)