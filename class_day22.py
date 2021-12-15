
# #1
# class Factory:
#
#     def create_engine(self):
#         return "Двигатель создан"
#
#     def create_amort(self):
#         return "Ходовая часть создана"
#
#
# f = Factory()
# print(f.create_amort(), f.create_engine())
# #2
# class Toyota(Factory):
#     def wheels(self):
#         return "Колёса готовы"
#
#     def window(self):
#         return "Стёкла готовы"
#
# t = Toyota()
# lst = [t.wheels(), t.window(),t.create_amort(),t.create_engine()]
# print(lst)

##3
# class Zoo:
#     pass
# z = Zoo()
#
# animal1 = 'tiger'
# animal2 = 'begemot'
# animal3 = 'Jiraff'
# z.animal1 = animal1
# z.animal2 = animal2
# z.animal3 = animal3
# z.animal4 = [animal2, animal3]
# z.animal1 = 'lion'
# z.animal = ' snake'
# print(z.animal1,z.animal3)
