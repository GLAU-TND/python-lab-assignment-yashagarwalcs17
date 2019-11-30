a=[2,3]
b=[34,53]
print('====Attribute Error====')
try:
    c=a.union(b)
except AttributeError as e:
    print(e)

print('\n\n\n')
print('====Type Error====')
try:
    "yash"+234
except TypeError as e:
    print(e)

print('\n\n\n')
print('====Value Error====')

try:
    int('xyz')
except ValueError as e:
    print(e)
