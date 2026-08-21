
import time
# class Animal:
#     def __init__(self,name,age,specien):
#         self.name = name
#         self.age = age
#         self.specien = specien

# class Zoo(Animal):
#     def add_animal(self,animal_added):
#         print(f"{animal_added.name} is added")

# zoo = Zoo()
# animal1 = Animal('ella',25,'elephant')
# animal2 = Animal('mea',40,'Tiger')
# zoo.add_animal(animal2)


tup = (10,20,40,55,25,12)
# res = tup.append(1)
# print(res)


# def fibonacci(n):
#     a,b = 0,1
#     for _ in range(n):
#         print(a,end = " ")
#         a , b = b , a + b
# fibonacci(7)


def log_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f" executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@log_time
def slow_func():
    time.sleep(2)
    return "Finished!"

print(slow_func())
