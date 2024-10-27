#1
input_number = int(input("Введите положительное число: "))
if input_number > 0:
    print("Молодец")
else:
    print("Это не положительное число.")

#2
checklist_rating = int(input("Введите оценку от 1 до 10: "))
if 7 <= checklist_rating <= 10:
    print("Отлично")
elif 5 <= checklist_rating < 7:
    print("Хорошо")
elif 3 <= checklist_rating < 5:
    print("Удовлетворительно")
elif 1 <= checklist_rating < 3:
    print("Плохо")
else:
    print("Вы не ввели число от 1 до 10, пожалуйста повторите функцию")

#3
password_true = 34586
while True:
    password_input = int(input("Введите пароль: "))
    if password_input == password_true:
        print("Login success")
        break
    else:
        print("Incorrect password, try again!")

#4
favorites = [3, 7, 11, 23, 18, 48, 81]
favorites_number = int(input("Введите любимое число из списка: "))
print(favorites_number)
flag = 0
for i in favorites:
    if i == favorites_number:
        flag = 1
    else:
      pass
if flag == 1:
  print("Мое любимое число!")
else:
  print("Эх, ну почему?")

#5
number_input = int(input("Введите число: "))
if number_input % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

#6
noun = input("Введите существительное: ")
if noun.istitle():
    print("Это имя собственное")
else:
    print("Это имя нарицательное")

