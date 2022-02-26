a = [1,2]
c = [1]
while True:

	b = a[0] + a[1]
	a[0] = a[1]
	a[1] = b
	c.append(a[0])
	
	if b > 4000000:
		break

print(c)		

e = 0
for i in c:
	if i % 2 == 0:
		e += i

print(e)		