#Code to translate list of english words to swedish from a #predefined dictionary of english:swedish

def translate(a,c):
  d=[]
  i=0
  for key,value in a.items():
    for i in range(len(c)):
      if key==c[i]:
        d.append(value)
      else:
        continue
  print(d)


dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
words=["merry","christmasa", "year"]
translate(dict,words)
