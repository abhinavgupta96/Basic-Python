##program to return fibonacci series of n-number
def fib(n): ##using recusrion
  if n<=1:
    return n
  else:
    return (fib(n-1) + fib(n-2))
  
def fib_series(n):
  output_list = []
  for i in range(n):
    fib_number = fib(i)
    output_list.append(fib_number)
  return output_list

def fib_iterative(n):
  if n == 0:
    return [0]
  if n == 1:
    return [0,1]
  output_list = [0,1]
  if n>=2:
    for i in range(2, n): ##since we already have first 2 numbers in the list
      temp = output_list[i-1] + output_list[i-2]
      output_list.append(temp)
  return output_list

print(fib_series(15))
print(fib_iterative(15))