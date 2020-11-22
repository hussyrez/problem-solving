def shortenString(input):
  result = ""
  current = input[0]
  size = 1
  for i in range(1, len(input)):
    if(current != input[i]):
      result += str(size)+current
      current=input[i]
      size=0
    size+=1
    if(i==len(input)-1):
      result += str(size)+current
      break

  print(result)

shortenString("AAAAAAABBBBBCCABSDDDDCCCCCC")