# #1
# capacity_swim_pool = lambda x, y, z: f'Обьем бассейна {x*y*z}'
# print(capacity_swim_pool(5,4,3))
#2
# x = int(input('Количество прошдших дней в этом году:'))
# y = lambda x: f'Сколько дней прошло с начало года {365-x}'
# print(y(x))
#3
# def odd_numbers(n):
#     if n > 0:
#         if n%2 == 1:
#             print(n)
#         odd_numbers(n-1)
#
# print(odd_numbers(100))
#4
# s = {123,'a','sdasdasd',(12,33)}
#
# def delete_set(s):
#     if len(s) > 0:
#         s.pop()
#         print(s)
#         delete_set(s)
#
# print(delete_set(s))

#2.3
#l = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
#y = list(map(lambda x:x*1.85, l))
#print(y)
#2.2

# def decor_log_pass():
#     log = input('Введите login:')
#     ord_log = []
#     ord_password = []
#     password = input('Введите pasword:')
#     for i in log:
#         ord_log.append(ord(i))
#     print(ord_log)
#     for i in password:
#         ord_password.append(ord(i))
#     print(ord_password)
#
# log_pass()
#2.1
import random

def list_erase_decor(func):
    def wrapper():
            result = func()
            result.clear()
            return result
    return wrapper

@list_erase_decor
def r_number():
    l = []
    for i in range(100):
        l.append(random.randint(10,51))
    return l
print(r_number())
