
#Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
#А затем записывает это всё в файл на рабочем столе menu.tx

path = "/home/azamat/Desktop/papka"
a = input('Выберите еду:')
b = input( 'Выберите выпить:')
def menu_create(a: object, b: object) -> object:
    with open(path+f'/menu.txt', 'w') as f:
        r = f.write(f'{a},{b}')
m = menu_create(a,b)

