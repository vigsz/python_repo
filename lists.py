import random

types = ['Shirt', 'Dress', 'Jeans', 'Top']
sizes = ['S', 'M', 'L', 'XL', 'XXL']
colors = ['Black', 'Blue', 'Green', 'Purple', 'Grey']
all_products = []
MAX_CAPACITY = 400

def add_new_product(type_, size):
    if types.__contains__(type_) and sizes.__contains__(size):
        all_products.append(random.choice(colors)  + " " + type_ + " " + size)
    else:
        if not types.__contains__(type_):
            print("The product you are trying to add doesn't have a correct type")
        if not sizes.__contains__(size):
            print("The product you are trying to add doesn't have a correct size")

def fill_warehouse(max_quantity):
    if len(all_products) < max_quantity:
        while len(all_products) != max_quantity:
            all_products.append(random.choice(all_products))
    else:
        print("Warehouse is already at full capacity.")

def is_product_in_stock(product):
    for element in all_products:
        if product in element:
            return True
    return False

def sell_product(product):
    if not is_product_in_stock(product):
        print("This product is not in stock.")
    else:
        for article in all_products:
            if product in article:
                all_products.remove(article)
                print("Successfully sold '%s' product." %(article))
                print("After selling it, our hobby shop has %d products left" %(len(all_products)))
                break
    
#Create the base products list
# for type_ in types:
#     for size in sizes:
#         add_new_product(type_, size)

[add_new_product(type_, size) for type_ in types for size in sizes]

#Create the final products list
fill_warehouse(MAX_CAPACITY)
print("Our hobby shop has %d products in stock" %(len(all_products)))
#print(all_products)

#Sell the latest product from the hobby shop
all_products.pop()
print("Sold the latest product. After selling it, our hobby shop has %d products left" %(len(all_products)))

#Sell a specific product from the hobby shop
sell_product("Dress S")

#Add a new specific product
add_new_product('Shirt', 'XXL')

#Fill warehouse to its full capacity
NEW_MAX_CAPACITY = 600
fill_warehouse(NEW_MAX_CAPACITY)
print("Restocked. Our hobby shop has %d products in stock" %(len(all_products)))
#print(all_products)