# membership and identity

a = [1,2,3]
b = [1,2,3]

c =a

print(a is b)   #fasle
print(a ==b)     #true
print(a is c)   #true
print(id(a))
print(id(b))
print(id(c))