a = {1, 2, 3}
b = {3, 4, 5}

# A union B
print('A union B :-')
print(a.union(b))
print(a | b)

# A intersection B
print(''
      '')
print('A intersection B :-')
print(a.intersection(b))
print(a & b)

# A equals to B
print(''
      '')
print('A equals or NOT equals to B :-')
print(a == b)
print(a != b)
b.clear()
print(b)
b.add(1)
b.add(2)
b.add(3)
print(b)
print(a == b)
print(a != b)

# Reforming the values
a = {1, 2, 3}
b = {3, 4, 5}

# Subsets
print(''
      '')
print('A issubset B :-')
print(a.issubset(b))
print(b.issubset(a))

# Supersets
print(''
      '')
print('A issuperset B :-')
print(b.issuperset(a))
print(a.issuperset(b))
