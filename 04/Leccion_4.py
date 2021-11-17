from functools import reduce
import pdb

list1 = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
list2 = [3, 4, 8, 5, 5, 22, 13]


def activity_1():
    result = [reduce(lambda n1, n2: n1 if n1 > n2 else n2, auxList)
              for auxList in list1]
    print(result)


def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime


def activity_2():
    result = list(filter(is_prime, list2))
    print(result)


if __name__ == '__main__':
    pdb.set_trace()
    activity_1()
    activity_2()
