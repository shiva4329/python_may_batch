#working with dictionary addresses

x={"a":10,"b":20}
print(x,id(x))

y={"a":10,"b":20}
print(y,id(y))

print(x is y)
print(x == y)

print(x["a"],type(x["a"]),id(x["a"]))
print(y["a"],type(y["a"]),id(y["a"]))

print(x["a"] is y["a"])

p=10

print(p is x["a"])
print(p == x["a"])

