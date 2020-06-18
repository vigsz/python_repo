brands = ('Esprit', 'Levi\'s', 'Guess', 'Tommy Hilfiger', 'Lacoste')
styles = ('Urban', 'Classic', 'Casual', 'Business')
types = ('Pants', 'Dress', 'Jacket', 'Top')
sizes = ('S', 'M', 'L', 'XL', 'XXL')

# brands_and_styles = []
# for brand in brands:
#     for style in styles:
#         brands_and_styles.append(brand + ' ' + style)

brands_and_styles = [brand + ' ' + style for brand in brands for style in styles]

# types_and_sizes = []
# for type_ in types:
#     for size in sizes:
#         types_and_sizes.append(type_ + ' ' + size)

types_and_sizes = [type_ + ' ' + size for type_ in types for size in sizes]

# all_products = []
# for brand_and_style in brands_and_styles:
#     for type_and_size in types_and_sizes:
#         all_products.append(brand_and_style + ' ' + type_and_size)

all_products = [brand_and_style + ' ' + type_and_size for brand_and_style in brands_and_styles for type_and_size in types_and_sizes]

print('The shop has %d products in stock' %(len(all_products)))

def sell_product_by_index(index):
    if abs(index) < len(all_products):
        sold_product = all_products.pop(index)
        if sold_product not in all_products:
            print('Successfully sold: ' + sold_product)
    else:
        print('Provided index is out of bounds')

def sell_product_by_name(name):
    if all_products.__contains__(name):
        all_products.remove(name)
        if name not in all_products:
            print('Successfully sold: ' + name)
    else:
        print("Product was not found")

def add_new_products_in_stock(index, name):
    if abs(index) < len(all_products) and not all_products.__contains__(name):
        all_products.insert(index, name)
        if name in all_products:
            print(name + ' was successfully added')
    elif all_products.__contains__(name):
        print('Product is already in stock')
    else:
        print('Provided index is out of bounds')

#Sell the latest product that was added to the shop
sell_product_by_index(-1)

#Sell any product from the shop
sell_product_by_name('Guess Casual Dress XL')

#Restock the shop with new items
add_new_products_in_stock(0, 'New Product')