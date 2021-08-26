def gnome(number):
  len_number = len(number)
  index = 0
  while index < len_number:
    if index==0:
      index += 1
    if number[index] >= number[index-1]:
      index += 1
    else:
      number[index],number[index-1] = number[index-1],number[index]
      index -= 1

  return number

import random
num = [random.randint(1,1000) for i in range(10)]
print(gnome(num))