def my_prop(func):
    res = func()
    res = str(res).split(" ")[0]
    return res


@my_prop
def get_name():
    return "Hardik Gosai"


print(get_name)
