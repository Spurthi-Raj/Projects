from collections.abc import Iterable

class MyCollection:
    def __init__(self) :
        self.data = [1,3,5]

    def __iter__(self):
        return iter(self.data)

obj = MyCollection()
for i in obj:
    print(i)


# *************************************************
def check_iterable(obj):
    try:
        iter(obj)
        print("Object is iterable")
    except TypeError:
        print("Object is not iterable")

check_iterable([1,3,5])
check_iterable("python")
check_iterable(20)


def check_iterable2(obj):
    if isinstance(obj,Iterable):
        print("Object is iterable")
    else:
        print("Object is not iterable")

check_iterable2((2,3,4))
check_iterable2({'a':5})
check_iterable2(100)

# *************************************************

numbers = [10,20,30,40]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# *************************************************

class EvenNumbers:
    def __init__(self,num):
        self.num = num
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.num:
            value = self.current
            self.current += 2
            return value
        else:
            raise StopIteration

even = EvenNumbers(10)
for n in even:
    print(n)


