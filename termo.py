import math
import Types

b = Types.SpacerTypes.AL16
# b2 = 1

x_values = (.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5)
y_values = (.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95,2,2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5)
surfaces = []
prices = []
pricessqm = []

def averagePriceCalcForDouble (glass1, glass2, spacer):
    for x_value in x_values:
        for y_value in y_values:
            surface = x_value * y_value
            length = 2 * x_value  + 2 * y_value
            surfaces.append(surface)
            price = surface * glass1.price + surface * glass2.price + length * b.price
            prices.append(price)
            pricesqm = price / surface
            pricessqm.append(pricesqm)
    # average_surface = sum(surfaces) / len(surfaces)
    average_pricesqm = sum(pricessqm) / len(pricessqm)
    rounded_average_pricesqm = round(average_pricesqm, 2)
    print('Average price for %s + %s + %s is: %.2f' %(glass1.name, b.name, glass2.name, rounded_average_pricesqm))

averagePriceCalcForDouble(Types.GlassTypes.Float4, Types.GlassTypes.LowE4, b)

# for surface in surfaces:
#     print(surface)

# def createXandYvalues():
#     x = min
#     while x <= max:
#         x_values.append(x)
#         x += inc
#     y = min
#     while y <= max:
#         y_values.append(y)
#         y += inc

# createXandYvalues()

# for x_value in x_values:
#     print(x_value)

# for y_value in y_values:
#     print(y_value)
