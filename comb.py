def comb(number):
    len_number = len(number)
    is_swap = True
    gap = len_number

    while gap != 1 or is_swap:
        gap = int(gap/1.3)
        if gap <1:
            gap = 1

        is_swap = False

        for i in range(len_number - gap):
            if number[i]>number[i+gap]:
                number[i],number[i+gap] = number[i+gap],number[i]
                is_swap = True
    
    return number

import random
num = [random.randint(0,1000) for i in range(10)]
print(comb(num))