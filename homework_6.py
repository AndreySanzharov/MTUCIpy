#1
numbers = [12, 24, 36, 48, 109, 187]
multiplier = 26  # Номер варианта + 7

def multiply_by_variant(num):
    return num * multiplier

result_a = list(map(multiply_by_variant, numbers))
print(result_a)

result_b = list(map(lambda x: x * multiplier, numbers))
print(result_b)
print("===============")


#2
first_number = [7, 977, 352, 41, 50]
second_number = [8, 985, 943, 21, 56]

product_number = list(map(lambda x , y: x * y, first_number, second_number ))
print(product_number)
print("===============")

#3
my_number = [8, 66, 189, 39, 44]
my_product_number= list(map(lambda x: x * 20, my_number))
even = list(filter(lambda x: (x % 2 == 0), my_product_number))
uneven = list(filter(lambda x: (x % 2 != 0), my_product_number))
print("четные числа", even)
print("нечетные числа", uneven)
print("=============")

#4
my_number = ['8', '966', '189', '39', '44']

my_number_int = list(map(lambda x: int(x), my_number))
my_number_int_divisor_20 = list(map(lambda x: int(x) // 20, my_number_int))
my_number_float_divisor_20  = list(map(lambda x: float(x) // 20, my_number_int))


print(my_number)
print(my_number_int)
print(my_number_int_divisor_20)
print(my_number_float_divisor_20)