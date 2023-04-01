def hello1():
    return 'hello 1'


def hello2():
    print("browser launch")
    yield 'hello2 launch'
    print("browser close")
    yield 'hello2 close'


print(hello1())
print(hello2())

for cur in hello2():
    print(cur)
