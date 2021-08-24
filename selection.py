def selection(number):
    len_number = len(number)
    for i in range(len_number):
        min_idx = i
        for j in range(i+1,len_number):
            if number[min_idx]>number[j]:
                min_idx = j

        number[i],number[min_idx] = number[min_idx],number[i]

    return number


import random
num = [random.randint(1,1000) for i in range(10)]
print(selection(num))