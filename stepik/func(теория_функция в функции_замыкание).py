# inner принимает число и умножает его на одно и то же число переданное в multiplier
# в нашем случае на 5 - концепция "замыкания"
#
def multiplier(num):
    def inner(a):
        return num * a

    return inner


print(multiplier(3)(10))
n = multiplier(5)
print(n(8))
print(n.__name__)