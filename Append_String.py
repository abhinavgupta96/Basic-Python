#Modify the given string such that there are no consecutive #"aaa" substring and return the count of "a" added. If given #string has substring of "aaa" output should be -1
#S -> abab should give output -> aabaabaa and count = 4

def solution(S):
  count=0
  result=""
  middle=""
  if "aaa" in S:
    return -1
  elif "aa"==S :
    return 0
  else :
    for i in range(len(S)):
      for j in range(i+1,len(S)):
        if i==0 and S[i]!="a":
          middle="aa"+S[i]
          count+=2
          result+=middle
        elif i==0 and S[i]=="a":
          if j=="a":
            pass
          else:
            middle="a"+S[i]
            count+=1
            result+=middle
        else:
          if S[i]=="a" and S[j] !="a":
            middle="a"+S[i]
            count+=1
            result+=middle
          elif S[i]=="a" and S[j] =="a":
            pass
          else:
            middle="aa"+S[i]
            count+=2
            result+=middle
    
    return(result,middle,count)


print(solution("da"))
