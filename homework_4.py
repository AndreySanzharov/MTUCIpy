#  1
rept = {"python": "питон", "anaconda": "анаконда", "tortoize": "черепаха"}

# Исправляем ключ и добавляем новый
rept["tortoise"] = rept.pop("tortoize")  # Исправляем ключ
rept["snake"] = "змея"  # Добавляем новую пару

# Выводим сообщения
for english, russian in rept.items():
    print(f"{russian.capitalize()} по-английски будет {english}.")


# 2
cnt = ["Andorra", "Belarus", "Denmark",
       "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.5, 4.0, 2.5, 2.0]

cnt_fn = dict(zip(cnt, fh))
for i in cnt_fn.items():
  print(i)
print(cnt_fn)

# 3
pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
a = 0
calc_temp = []
for i in pairs:
    c = pairs[a][0] * pairs[a][1]
    a += 1
    calc_temp.append(c)
calc = dict(zip(pairs, calc_temp))
print(calc)




#4
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
         'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
         'Ursula': 4, 'Viktor': 5}
excel = []
good = []
satisf = []
bad = []

for key, value in grades.items():
    print(key,value)
    if value == 5:
        excel.append(key)
    elif value == 4:
        good.append(key)
    elif value == 3:
        satisf.append(key)
    else:
        bad.append(key)

print(excel)
print(good)
print(satisf)
print(bad)

