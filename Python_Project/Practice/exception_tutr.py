
def exception_test():
    try:
        print("Before exception")
        print(100+'hi')
        print("After excetion")  # will not execute this line

    except Exception as obj:
        print(obj)

    print("Rest of the code")
        

exception_test()


fruits = ("apple",)
print(type(fruits))

print("****************************************************")

my_lst = [3,5,7,8]
rev_lst = my_lst[::-1]
print(rev_lst)

my_list = [1,2,3,4]
my_list.reverse()
print(my_list)


my_list1 = [1,3,4,6]
rev_list = list(reversed(my_list1))
print(rev_list)