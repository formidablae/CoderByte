def FindIntersection(strArr):

  # code goes here
  first = [int(x.strip()) for x in strArr[0].split(',')]
  second = [int(x.strip()) for x in strArr[1].split(',')]

  i = 0
  j = 0
  result = ""
  interection = False
  while i < len(first) and j < len(second):
    if first[i] == second[j]:
      result = result + str(first[i])
      result = result + ","
      interection = True
      i = i + 1
      j = j + 1
    elif first[i] < second[j]:
      i = i + 1
    else:
      j = j + 1

  if interection:
    if result[-1] == ",":
      return result[:-1]
    return result
  return "false"

# keep this function call here 
print(FindIntersection(input()))
