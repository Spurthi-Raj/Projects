import copy



a = 10
b = 10

print(id(a))
print(id(b))
print(a is b)
print( a == b)

lst1 = [10,[20,25,26],30,40]
shallow_copy = copy.copy(lst1)
print(lst1,"lst111111111111111")
print(shallow_copy,"shallow_copy---------------")
print("-----------------------------------------------------")
shallow_copy[1][1] = 300
shallow_copy[2] = 36

print(lst1,"lst111111111111111")
print(shallow_copy,"shallow_copy---------------")

print("****************************************************")

lst2 = [15,[20,30,35,38],40,50]

deep_copy = copy.deepcopy(lst2)
print(lst2,"lst2-------------------------")
print(deep_copy,"deep_copy------------------------------")
deep_copy[1][2] = 60
print(lst2,"lst2----------------after---------")
print(deep_copy,"deep_copy-------------------after-----")


def decorator_test(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@decorator_test
def hello():
    print("Hello----")


hello()

