def FirstFactorial(num):

  # code goes here
  if num == 1:
    return 1
  return num * FirstFactorial(num - 1)

# keep this function call here 
print(FirstFactorial(input()))
