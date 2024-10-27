#1
def square(number):
    number_square = number**2
    print(number_square)
    print(f"Квадрат числа {number} равен: n")
    return f"Квадрат числа {number} равен: {number_square}"

n = 13
print(square(n))


#2
def nums(number):
    mylist = [number - 1, number + 1]
    return mylist

nums(3)

#3
massive_word = []

def str_lower(word):
    for i in word.split():
        massive_word.append(i.lower())
    print(massive_word)

str_lower("В лесу родилась ёлочка В лесу она росла")

#4
import math


def my_log(some_list):
    for i in some_list:
        if i <= 0:
            print(None)
        else:
            print(math.log(i))


my_log([1, 3, 2.5, -1, 9, 0, 2.71])


#5
def my_dict(name,age):
    if len(name) == len(age):
        print(dict(zip(name,age)))
    else:
        print("Списки имеют разную длину")

my_dict(["Ann", "Tim", "Sam"],[12, 23, 17])


#6
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

def binom_prob(p, n ,k):
    return (factorial(n) // (factorial(k) * factorial(n - k))) * (p ** k) * ((1 - p) ** (n - k))

binom_prob(5,5,5)


#7
def all_sort(*args):
    return sorted(args)

all_sort(7, 6, 1, 3, 8, 0, -2)

