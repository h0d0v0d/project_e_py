def obr(x,y):
	c = str(x)
	b = c[y]
	return b 

a = list(range(1,1000))
b = list(range(1,1000))
p = []
p1 = []
p2 = []

for i in a:
	for i1 in b:
		c = i1 *i
		if obr(c,0) == obr(c,-1):
			p.append(c)

for i2 in p:
	if len(str(i2)) >= 4 :
		if obr(i2,1) == obr(i2,-2):
			p1.append(i2)

for i3 in p1:
	if len(str(i3)) >=6 :
		if obr(i3,2) == obr(i3,-3):
			p2.append(i3)
			
print(max(p2))		

# знаю, код сильно усложнен, но свою функцию он выполнят и работает моментально
# вроде))






#if obr(v,0) == obr(v,2):
#	print(v)
















#a = 'rip'
#print(list(a))