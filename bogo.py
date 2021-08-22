import random 

def in_order(number):
    return all(number[i] <= number[i+1] for i in range(len(number)-1))
    # for i in range(len(number)-1):
    #     if number[i] > number[i+1]:
    #         return False
    # return True


def bogo(number):
    while not in_order(number):
        random.shuffle(number)
    return number

if __name__ == '__main__':
    num = [random.randint(0,1000) for i in range(10)]
    # print(num)
    print(bogo([5,2,6,2,6,6,7]))