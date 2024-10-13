#1
full_name = input("Введите ФИО:")
word_Full_name = full_name.split()
print("Ваша фамилия: " + word_Full_name[0])
print("Ваша имя: " + word_Full_name[1])
print("Ваша отчество: " + word_Full_name[2])

#2
numbers = '1; 2; 3; 100'
number_massive = numbers.split("; ")
print(number_massive)
list_number_massive = []
list_number_massive_float = []
for i in number_massive:
    list_number_massive.append(int(i))
print(list_number_massive)
for j in list_number_massive:
    list_number_massive_float.append(float(j))
print(list_number_massive_float)

#3
phone_number = input("Введите номер телефона через дефис: ")
cleaned_number = phone_number.replace("-", "").replace(" ", "")
print("Номер телефона без дефисов и пробелов:", cleaned_number)

#4
import math
L = [5000,3400,2100,3250,9000]
for i in L:
    print(math.log(i))

#5
words = [" Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the", "Renaissance"]
words_clean = []
for i in words:
    words_clean.append(i.lower().replace(" ", ""))
print(words_clean)

