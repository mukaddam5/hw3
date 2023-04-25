
#
# def greeting():
#     print("Hi")
# greeting()
#
#
# def greeting(name):
#     print("Hi" + " " + name)
# greeting( "Yasmin")
# greeting( "Usmon")
#

#
# def addition(number, by):
#     return number + by
# print(addition(3, 5))
#
#
#
# #
# def addition(number, by = 1):
#     return number + by
# print(addition(3))
# print(addition(3, 5))

#
# def addition(number, phone, by = 1):
#     return number + phone + by
# print(addition(3,5,4))
# print(addition(3,5))

#
# def mika(*numbers):
#     total = 2
#     for number in numbers:
#         total *= number
#     return total
#
#
# print((mika(1, 2, 3, 4, 5)))

#
#
# def apple(**user):
#     return user
#
# print(apple(id = 1, name = "John", phone = "929-321-2688"))




class ParentClass:

    def school(self, a, b):
        return a, b



class ParentClass2:

    def academy(self, x, y):
        return x + y


class ParentClass3(ParentClass2):

    # child3 = ParentClass2()
    # child3.academy(10, 20)

    def university(self, c, z):
        return c * z












