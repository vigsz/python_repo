print('Hello')

one_variable = '5'
some_string = 'Some other string'

third_variable = one_variable + some_string

some_number = 5
some_other_number = 6

result = some_number + some_other_number

items = ['1', '2', '3', '5']

tuple = (1, 2 , 3 , 4)

for item in items:
    print(item)

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)

print('Stuff')


multi = ''' line 1 
line 2
line 3'''

print(multi)

def get_running_sum():
    total_sum = 0 
    total_items = 0 
    def compute_sum(new_number):
        nonlocal total_items, total_sum
        total_items += 1 
        total_sum += new_number
        print("Total:{}. Items:{}".format(total_sum, total_items))
        return total_sum
    return compute_sum

compute_sum = get_running_sum()

compute_sum(5)
compute_sum(15)
compute_sum(25)
compute_sum(35)
