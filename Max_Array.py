#Code to find the maximum value not present in the array passed 

def solution (A):
  B =[x for x in A if x < 0] + [x for x in A if x > 1]
  num = max(B)
  ans = 0
  for i in range(num-1,-1,-1):
    if i not in B:
      ans = i
      break
  return ans

print(solution([-4,10,-2,20,12,13]))