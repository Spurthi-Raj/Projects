import copy

a=10
b=10
print(id(a))
print(id(b))

print("**********************************************")

x = [10,20,30]
y = x
print(id(x))
print(id(y))
print(id(x) == id(y))

print("**********************************************")

a = 30
b = 30
print(id(a),id(b))
print(a is b)

print("**********************************************")

a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b)

print("*****************string*****************************")

a = "hello"
b = "hello"
print(id(a),id(b))
print(a is b)

print("_______________________del________________")

a = [1,8]
b = a
del a
print(b)

print("************ append ***************")

a = [1,2,3]
b = a
b.append(4)
print(a)

print("************ -- ***************")

a = (1,2,3)
b = a
print(a is b)

print("************* shallow copy ********")

a = [[1,2], [3,4]]
b = copy.copy(a)
b[0][0] = 99
print(a)

print("**************** deep copy ***************")

a = [[1,2], [3,4]]
b = copy.deepcopy(a)
b[0][0] = 99
print(a)


print("************ Why is this dangerous? ******************")

def func(a=[]):
    a.append(1)
    return a

print(func([]))
print(func([]))

print("++++++++++++++++++++++++++++")

a = [1,2,3]
b = a[:]
b.append(4)
print(a)
print(b)

print("++++++++++++++++++++++++++++")

a = 256
b = 256
print(a is b)