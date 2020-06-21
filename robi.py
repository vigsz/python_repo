import pycountry
import pprint

pp = pprint.PrettyPrinter(indent=4)

description = ('Country', ['2011', '2012'])
raw_data = [('AL', ['93', '95']), ('RO', ['96', ':'])]

def prepare_dataset(description, raw_data):
  data_dict = {}
  if description and len(description) == 2:
    years_list = description[1]
    if raw_data:    
      for entry in raw_data:
        if len(entry) == 2 and len(entry[1]) == len(years_list):
          country = get_country_name(entry[0])
          data_dict[country] = []                    
          #for i, coverage in enumerate(entry[1]):
          i = 0
          for coverage in entry[1]:
            if coverage and is_int(coverage):
              data_dict[country].append({'year': years_list[i], 'coverage': int(coverage)})
            i += 1
  pp.pprint(data_dict)

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_country_name(code):
  return pycountry.countries.get(alpha_3=code).name if len(code) == 3 else pycountry.countries.get(alpha_2=code).name

prepare_dataset(description, raw_data)
print("-----------------")

def prepare_dataset2(description, raw_data):
  return {entry[0]: [{'year': description[1][i], 'coverage': int(coverage)} for i, coverage in enumerate(entry[1]) if is_int(coverage)] for entry in raw_data}

print(prepare_dataset2(description, raw_data))





