
#Проблема 12
x = ['Barcelona',1,(4.2,'rt'),'fd',('toy',500),("all",1.5),('lif',8),('xr',5,3.44)]
print(x)
#Проблема 32
i = ('priora','avensis','land_rover')
print(i[0])
print(i[1])
print(i[2])
#Проблема 11
y = [1,'ffffff',3.2,(3,'xxx'),['hi',6],888]
print(y)
#Проблема 0
x = ['ddd','hhh','rtrt','sas','adaad']
y = '  '.join(x)
print(y)
#Проблема 17
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',].count('Jack')
print(names)
#Проблема 12
t = ('ee','ftt',('dsda','1'),'g','m','lo','cv','baajj','akba','folow','dd','zz','iii''kfhd','uu','aa')
print(t[0:3])
print(t[3:6])
print(t[6:9])
print(t[9:12])
print(t[12:15])
#Проблема 1
a = []
a.append('Azamat')
a.append(1988)
a.append('python')
print(a)
#Проблема 72
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
for  x in range(10):
	print(names[x])
	if x%2==0:
		print(names.pop(x))
