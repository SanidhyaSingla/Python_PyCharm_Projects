# create 2 sets
a = {1, 2, 3}
b = {3, 4, 5}

# print elements
print(a)
print(b)

# iterate through sets
for somethin in a:
    print(somethin)

for t in b:
    print(t)

# add elements
a.add(4)
print(a)

# remove items from sets in 3 different ways
a.discard(10000)
a.remove(4)
print(a.pop())
print(a)
