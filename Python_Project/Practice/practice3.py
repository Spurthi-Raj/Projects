

# a=24
# b=25
# print(id(a))
# print(id(b))
# print(a is b)




# def decor_func(func):
#     def wrapper():
#         print("before")
#         func()
#         print("After")
#     return wrapper()

# @decor_func
# def say_hello():
#     print("Hello")


# square = [x*x for x in range(5)]
# print(square)


# stu_details = {
#     'id':1000,
#     'name':'xyz',
# }
# print(stu_details['name'])


# a = [10,20]
# b = [10,20]
# print(id(a),"---------------",id(b))
# print(a is b)


# class Car:
#     category = "Sedan"
#     def __init__(self,model_name):
#         self.model_name = model_name
        
# c1 = Car("Toyoto")
# c2 = Car("Honda")
# c2.category = "BMW"
# print(f"c1--->{c1.category},c2----->{c2.category}")


# if (0.1 + 0.2 == 0.3):
#     print('True')
# else:
#     print('False')


# result = lambda x,y : x+y
# print(result(2,4))

# def outter(func):
#     def wrapper():
#         print("before")
#         func()
#         print("SAfter")
#     return wrapper

# @outter
# def say_hello():
#     print("hiiiii")

# say_hello()


def largest(num):
    result = list(set(num))
    result.sort()
    return result[-1]

print(largest([10,15,30,5,15]))