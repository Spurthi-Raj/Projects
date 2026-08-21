# import copy 



# # lst1 = [10,[20,25,26],30,40]
# # shallow_copy = copy.copy(lst1)
# # print(lst1,"lst111111111111111")
# # print(shallow_copy,"shallow_copy---------------")
# # print("-----------------------------------------------------")
# # shallow_copy[1][1] = 300
# # print(lst1,"lst111111111111111")
# # print(shallow_copy,"shallow_copy---------------")

# # name = "spoorthi"
# # print(name[2:])

# class Example:
#     company = "TCS"

#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal

#     def view(self):
#         return f"name{self.name} and salary is {self.sal}"

# o1 = Example("abc",12333)
# print(o1.view())


# def find_duplicate(lst):
     
#     return list[set(x for x in lst if lst.count(x)>1)]
# #
# print(find_duplicate([1,3,3,10,6]))

# def example(*args, **kwargs):
#     print(args)
#     print(kwargs)

# example(1, 2, name="John", age=30)

# with open('test.txt','r') as f:
#     print(f.read())





# ------decorator-----------

def my_decor(func):
    def wrapper():
        print("Before decor")
        func()
        print("After decor")
    return wrapper


@my_decor
def greet():
    print("Hello")

greet()