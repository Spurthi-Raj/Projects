
import cProfile
# ------- Decorators -------------

def my_decorators(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorators
def greet():
    print("Hello")

greet()

cProfile.run("greet()")



#--------------- String reverse -------------

name = "spoorthi"
rev = ""
for ch in name:
    rev = ch + rev
print("Reversed string is : ",rev)

# --------------- Duplicate element in list

lst = [1,5,10,15,5,20]
for i in lst:
    if lst.count(i) > 1:
        duplicate = i
print(duplicate)

duplicates = set([i for i in lst if lst.count(i) > 1])
print(duplicates)

#----------------------------------------
print(None==False)

int1 = 10.80
print(int1)
print(id(int1))
int1=20.60
print(int1)
print(id(int1))

a = [1,2]
print("id-----",id(a))
a.append(3)
print("id---",id(a))
print(a)

print("--------------------------")

a = 10
a = 10
print( a == a)
print(a is a)