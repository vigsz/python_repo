from collections import namedtuple

Glass = namedtuple('Glass', ['name', 'price'])

class GlassTypes:
    F4 = Glass('Float 4', 7.3)
    L4 = Glass('LowE', 9.9)

# from collections import namedtuple

# Glass = namedtuple('Glass', 'name price sex')

# print('Type of Glass:', type(Glass))

# F4 = Glass(name='Float 4', price=9.9)
# print('\nRepresentation:', F4)

# L4 = Glass(name='LowE4', price=12)
# print('\nField by name:', L4.name)

# print('\nFields by index:')
# for p in [ F4, L4 ]:
#     print('price for %s is: %d' % p)

# print(Glass._fields)
