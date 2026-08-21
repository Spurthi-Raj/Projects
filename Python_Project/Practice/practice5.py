square = [i*i for i in range(5)]
print("squares" , square)

def gen_fun():
    for i in range(1,5):
        yield i
g = gen_fun()
print(next(g))
# print(next(g))


name = 'spoorthi'
print(name[::-1])

a = "12345"
print(a)
b = int(a)
print(b + 2)

print("----------------------------------------------------")

msg = "c is a oopsc programming lng,c is easy"
msg = msg.strip('y')
print(msg,"................")
print(id(msg))
print(msg.replace('c','python'))
print(id(msg))
print(msg)

print("=================================================")

x = 0 
for i in range(3):
    x = x + i
print(x)

print("*******************************************************")
# split
names = "spoo,aabc,xyz,kim"
names1 = names.split(',')
print(names1)