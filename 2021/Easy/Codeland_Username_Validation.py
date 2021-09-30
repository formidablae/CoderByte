def CodelandUsernameValidation(strParam):

  if len(strParam) < 4:
    return "false"
  if len(strParam) > 25:
    return "false"
  if not strParam[0].isalpha():
    return "false"
  if strParam[-1] == "_":
    return "false"
  for char in strParam:
    if not(char.isalpha() or char.isnumeric() or char == "_"):
      return "false"
  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))
