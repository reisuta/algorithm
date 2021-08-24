def bubble(number):
    len_number = len(number)
    for i in range(len_number):
        for j in range(len_number-1 -i):
            if number[j] > number[j+1]:
                number[j],number[j+1] = number[j+1],number[j]

    return number

import random
num = [random.randint(0,1000) for i in range(10)]
print(bubble(num))