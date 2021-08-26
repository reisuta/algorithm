def insertion(number):
  len_number = len(number)
  for i in range(1,len_number):
    temp = number[i]
    j = i -1
    while j>=0 and number[j]> temp:
      number[j+1] = number[j]
      j -= 1
    number[j+1] = temp

  return number

import random
num = [random.randint(1,100) for i in range(10)]
print(insertion(num))