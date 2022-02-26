print('Программа запущена.')
numb1 = int(input('Введите первое число последовательности:\n'))
numb2 = int(input('Введите последние число пследовательности:\n'))
numb2 += 1

a = list(range(numb1, numb2, 1))
x = 0
count = 0

while True:
	x = x + a[count] ** 2
	count += 1
	if count == a[-1]:
		break

z = sum(a) ** 2
pere = z - x
print('Разность между суммой квадратов и квадратом суммы равна -', pere)
