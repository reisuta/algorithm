def cocktail(number):
    len_number = len(number)
    is_swap = True
    start = 0
    end = len_number -1
    while is_swap:
        is_swap = False
        for i in range(start,end):
            if number[i] > number[i+1]:
                number[i],number[i+1] = number[i+1],number[i]
                is_swap = True

        if not is_swap:
            break
            
        is_swap = False
        end = end -1

        for i in range(end-1,start-1,-1):
            if number[i] > number[i+1]:
                number[i],number[i+1] = number[i+1],number[i]
                is_swap = True

        start = start + 1
 
    return number

import random
num = [random.randint(1,100) for i in range(10)]
print(cocktail(num))
