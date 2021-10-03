def get_multi():
    def inner(a, b):
        return a * b

    return inner


print(get_multi()(2, 5))
multiplier = get_multi()
print(multiplier(3, 5))

print(multiplier.__name__)



