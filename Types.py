from collections import namedtuple

Glass = namedtuple('Glass', ['name', 'price'])

class GlassTypes:
    Float4 = Glass('Float 4', 7.3)
    LowE4 = Glass('LowE 4', 9.9)
    Solar4 = Glass('Solar 4', 9.4)
    Float6 = Glass('Float 6', 15.9)
    LowE6 = Glass('LowE 6', 17.89)
    Solar6 = Glass('Solar 6', 19.89)
    D331 = Glass('3.3.1', 26.89)
    D331LowE = Glass('3.3.1 LowE', 28.89)
    DeltaClar4 = Glass('Delta Clar 4', 18.5)
    DeltaBronz4 = Glass('Delta Bronz 4', 20.9)
    DeltaMat4 = Glass('Delta Mat 4', 26.)
    CincillaClar4 = Glass('Cincilla Clar 4', 17.6)
    CincillaBronz4 = Glass('Cincilla Bronz 4', 19.3)
    Screen4 = Glass('Screen  4', 13.1)
    Krizet4 = Glass('Krizet 4', 14.3)
    Crepy4 = Glass('Crepy 4', 18.4)
    CrepyBronz4 = Glass('Crepy Bronz 4', 20.3)
    Crossfield4 = Glass('Crossfield 4', 21.9)
    MaslinClar4 = Glass('Maslin Clar (Bronz) 4', 25.6)
    HasirClar4 = Glass('Hasir Clar (Bronz) 4', 31.1)
    SatinBronz4 = Glass('Mat (Sat) Bronz 4', 24.7)
    Satin4 = Glass('Mat (Satinat) 4', 21.4)
    ParsolBronz4 = Glass('Parsol Bronz 4', 17.4)
    StopsolBronz4 = Glass('Stopsol Bronz 4', 20.6)
    ScoartaClar4 = Glass('Scoarta Clar 4', 19.4)
    ScoartaBronz4 = Glass('Scoarta Bronz 4 ', 21.3)
    FlutesClar4 = Glass('Flutes Clar 4', 19.3)
    FlutesMat4 = Glass('Flutes Mat 4', 30.4)
    Oglinda4 = Glass('Oglinda 4', 21.)
    D442 = Glass('4.4.2', 39.58)
    D442LowE = Glass('4.4.2 LowE', 43.18)

Spacer = namedtuple('Spacer', ['name', 'price'])

class SpacerTypes:
    AL16 = Spacer('AL 16', 1.)
    LowE4 = Spacer('AL 18', 1.1)


# from collections import namedtuple

# Glass = namedtuple('Glass', 'name price')

# print('Type of Glass:', type(Glass))

# F4 = Glass(name='Float 4', price=9.9)
# print('\nRepresentation:', F4)

# L4 = Glass(name='LowE4', price=12)
# print('\nField by name:', L4.name)

# print('\nFields by index:')
# for p in [ F4, L4 ]:
#     print('price for %s is: %d' % p)

# print(Glass._fields)
