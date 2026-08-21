import copy 

str1 = "codeyug"
print(str1)

name="spooo"
rev_name = ""
for n in name:
    rev_name = n + rev_name
print(rev_name)

names = ['abc','xyz','alpha','beta']

for i,name_list in enumerate(names,start=1):
    print(i,name_list)

print("----------------------------------------------")

def my_decorator(test_func):
    def wrapper_test():
        print("Before....")
        test_func()
        print("After....")
    return wrapper_test()

@my_decorator
def hello():
    print("Say Hello")

hello
print("----------------------------------------------")
lst1 = [1,2,3,4,[10,20,20]]
shallow_copy = copy.copy(lst1)
deep_copy = copy.deepcopy(lst1)
lst1[1]=10
lst1[4][0]=100
print(lst1,"lst1-------")
print(shallow_copy,"shallow_copy--------")
print(deep_copy,"deep_copy-------")

def is_even(num):
    return num%2==0

nums = [2,3,4,5,6,7]
even_num = filter(is_even,nums)
print(list(even_num))


