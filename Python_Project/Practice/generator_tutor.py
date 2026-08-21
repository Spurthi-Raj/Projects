
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()
print(next(g))
print(next(g))
print(next(g))



def square_numbers(n):
    for i in range(n,n+1):
        yield i*i

gen = square_numbers(5)
for i in gen:
    print(i)


for _ in range(3):
    print("Hello")