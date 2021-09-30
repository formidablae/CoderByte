def QuestionsMarks(strParam):

  # code goes here
  liststr=[]
  liststr[:0]=strParam
  listdigquest = []
  for el in liststr:
    if el.isdigit():
      listdigquest.append(int(el))
    elif el == "?":
      listdigquest.append(el)
    
  i = 0
  j = i + 1
  result = False
  while i < len(listdigquest) - 4:
    if listdigquest[i] != "?":
      for j in range(i + 1, len(listdigquest)):
        if listdigquest[j] != "?" and listdigquest[i] + listdigquest[j] == 10:
          if countquest(listdigquest, i + 1, j) == 3:
            result = True
          else:
            return "false"
    i = i + 1
  if result:
    return "true"
  return "false"

def countquest(arr, st, en):
  cnt = 0
  for i in range(st, en):
    if arr[i] == "?":
      cnt = cnt + 1
  return cnt

# keep this function call here 
print(QuestionsMarks(input()))
