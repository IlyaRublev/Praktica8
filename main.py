print('Задание 1')
from collections import Counter
q = str(input('Введите слово:'))
w = len(q)
if w < 1:
    print('Ошибка!')
else:
    e = Counter(q)
    print('Символ, наиболее встречающийся в данной строке:',e.most_common(1)[0][0])

print('Задание 3')
q = int(input('Количество чисел:'))
w = []
e = []
for r in range(q):
    t = int(input('Число:'))
    e.append(t)
y = int(input('Степень числа:'))
for t in e:
    w.append(t**y)
for u in w:
    print(u)
