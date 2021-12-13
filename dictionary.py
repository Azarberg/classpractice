#Проблема 10
menu = {'lagman': 120,'plov':120,'borsh':100}
menu['drinks'] = ('Coca-Cola', 'Sprite', 'Fanta') 
print(menu)

#Проблема 020
s = {'pop','difference','add','update','remove','clear','discard','intersection','intersection_update','pop'}
d = {'clear','get','keys','values','items','update'}
#Проблема 031
d = {}

for x in range(3):
	log = input('Введите логин:')
	passwd = input('Введите пароль:')
	d[log] = passwd
print(d)

#Проблема 027
d = {'Ivan': 'doctor','Mickey':'actress','Jack':'teacher','Elena':'cooker','Ana':'seller'}
for x in d:
	print(f"Здравствуйте {x} прекрасная профессия {d[x]}")

#Проблема 022 Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
#Сделайте так чтобы эти данные уже никто не смог поменять позже.
s = set()
for x in range(10):
	n = input('Введите число:')
	s.add(n)
print(s)
#Проблема 099 Из Dictionary №1:Добавьте в меню  'besh_barmak' который стоит  130 сом.Оказалось лагман слишком дешевый. Обновите цену на 135
#Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.

Удалить borsh
menu = {'lagman': 120,'plov':120,'borsh':100}
menu['besh-barmak'] = 130
menu['lagman'] = 135
del menu['borsh']
print(menu)
#Проблема 11
south_a_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
print(list(set(south_a_countries)))
#Проблема 101
suitcase = []
suitcase.append('shirt')
suitcase.append('shoes')
suitcase.append('sneakers')
suitcase.append('tie')
suitcase.append('dress')
suitcase.pop()
print(suitcase)

#Проблема 001
farm_1 = {'dog','pig','duck','sheep'}
farm_2 = {'cow','horse','donkey','cat','duck'}
s = farm_1.difference(farm_2)
z = farm_1.intersection(farm_2)
print(s)
print(z)
