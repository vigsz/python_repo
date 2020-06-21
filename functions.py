import pycountry

description = (
    "Country",
    ["2011 ", "2012 ", "2013 ", "2014 ", "2015 ", "2016 ", "2017 ", "2018 ", "2019 "],
)

raw_data = [
    ("AL", [": ", ": ", ": ", ": ", ": ", ": ", ": ", "84 ", ": "]),
    ("AT", ["75 ", "79 ", "81 ", "81 ", "82 ", "85 ", "89 ", "89 ", "90 "]),
    ("BA", [": ", ": ", ": ", ": ", ": ", ": ", ": ", "69 ", "72 "]),
    ("BE", ["77 ", "78 ", "80 ", "83 ", "82 ", "85 ", "86 ", "87 ", "90 "]),
    ("BG", ["45 ", "51 ", "54 ", "57 ", "59 ", "64 ", "67 ", "72 ", "75 "]),
    ("CH", [": ", ": ", ": ", "91 ", ": ", ": ", "93 b", ": ", "96 "]),
    ("CY", ["57 ", "62 ", "65 ", "69 ", "71 ", "74 ", "79 ", "86 ", "90 "]),
    ("CZ", ["67 ", "73 ", "73 ", "78 ", "79 ", "82 ", "83 ", "86 ", "87 "]),
    ("DE", ["83 ", "85 ", "88 ", "89 ", "90 ", "92 ", "93 ", "94 ", "95 "]),
    ("DK", ["90 ", "92 ", "93 ", "93 ", "92 ", "94 ", "97 ", "93 ", "95 "]),
    ("EA", ["74 ", "76 ", "79 ", "81 ", "83 ", "85 ", "87 ", "89 ", "90 "]),
    ("EE", ["69 ", "74 ", "79 ", "83 ", "88 ", "86 ", "88 ", "90 ", "90 "]),
    ("EL", ["50 ", "54 ", "56 ", "66 ", "68 ", "69 ", "71 ", "76 ", "79 "]),
    ("ES", ["63 ", "67 ", "70 ", "74 ", "79 ", "82 ", "83 ", "86 ", "91 "]),
    ("FI", ["84 ", "87 ", "89 ", "90 ", "90 ", "92 ", "94 ", "94 ", "94 "]),
    ("FR", ["76 ", "80 ", "82 ", "83 ", "83 ", "86 ", "86 ", "89 ", "90 "]),
    ("HR", ["61 ", "66 ", "65 ", "68 ", "77 ", "77 ", "76 ", "82 ", "81 "]),
    ("HU", ["63 ", "67 ", "70 ", "73 ", "76 ", "79 ", "82 ", "83 ", "86 "]),
    ("IE", ["78 ", "81 ", "82 ", "82 ", "85 ", "87 ", "88 ", "89 ", "91 "]),
    ("IS", ["93 ", "95 ", "96 ", "96 ", ": ", ": ", "98 ", "99 ", "98 "]),
    ("IT", ["62 ", "63 ", "69 ", "73 ", "75 ", "79 ", "81 ", "84 ", "85 "]),
    ("LT", ["60 ", "60 ", "65 ", "66 ", "68 ", "72 ", "75 ", "78 ", "82 "]),
    ("LU", ["91 ", "93 ", "94 ", "96 ", "97 ", "97 ", "97 ", "93 b", "95 "]),
    ("LV", ["64 ", "69 ", "72 ", "73 ", "76 ", "77 b", "79 ", "82 ", "85 "]),
    ("ME", [": ", "55 ", ": ", ": ", ": ", ": ", "71 ", "72 ", "74 "]),
    ("MK", [": ", "58 ", "65 ", "68 ", "69 ", "75 ", "74 ", "79 ", "82 "]),
    ("MT", ["75 ", "77 ", "78 ", "80 ", "81 ", "81 ", "85 ", "84 ", "86 "]),
    ("NL", ["94 ", "94 ", "95 ", "96 ", "96 ", "97 ", "98 ", "98 ", "98 "]),
    ("NO", ["92 ", "93 ", "94 ", "93 ", "97 ", "97 ", "97 ", "96 ", "98 "]),
    ("PL", ["67 ", "70 ", "72 ", "75 ", "76 ", "80 ", "82 ", "84 ", "87 "]),
    ("PT", ["58 ", "61 ", "62 ", "65 ", "70 ", "74 ", "77 ", "79 ", "81 "]),
    ("RO", ["47 ", "54 ", "58 ", "61 b", "68 ", "72 ", "76 ", "81 ", "84 "]),
    ("RS", [": ", ": ", ": ", ": ", "64 ", ": ", "68 ", "73 ", "80 "]),
    ("SE", ["91 ", "92 ", "93 ", "90 ", "91 ", "94 b", "95 ", "93 ", "96 "]),
    ("SI", ["73 ", "74 ", "76 ", "77 ", "78 ", "78 ", "82 ", "87 ", "89 "]),
    ("SK", ["71 ", "75 ", "78 ", "78 ", "79 ", "81 ", "81 ", "81 ", "82 "]),
    ("TR", [": ", "47 ", "49 ", "60 ", "70 ", "76 ", "81 ", "84 ", "88 "]),
    ("UK", ["83 ", "87 ", "88 ", "90 ", "91 ", "93 ", "94 ", "95 ", "96 "]),
    ("XK", [": ", ": ", ": ", ": ", ": ", ": ", "89 ", "93 ", "93 "]),
]

def prepare_dataset(description, raw_data):
  data_dict = {}
  if description and len(description) == 2:
    years_list = description[1]
    if raw_data:    
      for entry in raw_data:
        if len(entry) == 2 and len(entry[1]) == len(years_list):
          country = entry[0]
          data_dict[country] = []                    
          #for i, coverage in enumerate(entry[1]):
          i = 0
          for coverage in entry[1]:
            if coverage and is_int(coverage):
              data_dict[country].append({'year': years_list[i], 'coverage': int(coverage)})
            i += 1
  print(data_dict)

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_country_name(code):
  full_country_name = pycountry.countries.get(alpha_2=code).full_country_name
  return full_country_name
  # return pycountry.countries.get(alpha_3=code).name if len(code) == 3 else pycountry.countries.get(alpha_2=code).name

iso_codes = ("AL", "AT", "BA", "BE", "BG", "CH", "CY", "CZ", "DE", "DK", "EA", "EE", "EL", "ES", "FI", "FR", "HR", "HU", "IE", "IS", "IT", "LT", "LU", "LV", "ME", "MK", "MT", "NL", "NO", "PL", "PT", "RO", "RS", "SE", "SI", "SK", "TR", "UK", "XK")

# for iso_code in iso_codes:
#   country = pycountry.countries.get(alpha_2=iso_code)
#   print(country)

prepare_dataset(description, raw_data)
# data = {'description': description, 'raw_data': raw_data}

# print(data)

# def prepare_dataset(data):
#   data_dict = {}
#   if data:
#     if 'description' in data and 'raw_data' in data:
#       years_list = data['description'][1]
#       # kene csinalni egy csomo data validationt, pl. len(data['description']) == 2 
#       for entry in data['raw_data']:
#         country = entry[0]
#         data_dict[country] = []
        
#         for i, coverage in enumerate(entry[1]):
#           if coverage and ':' not in coverage:
#             data_dict[country].append({'year': years_list[i], 'coverage': int(coverage)})
#           else:
#             data_dict[country].append({'year': years_list[i], 'coverage': None})
#   print(data_dict)

# prepare_dataset(data)



# {
# 'Romania': [
# {'year': '2019',
# 'coverage': 84}, {
# 'year': '2018',
# 'coverage': 67
# },
# ...,
# {
# 'year': '2011',
# 'coverage': 72
# }
# ],
# 'Germany': [
# {
# 'year': '2019',
# 'coverage': 94
# 'year': '2018',
# 'coverage': 87
# },
# ...,
# {
# 'year': '2011',
# 'coverage': 82
# }
# ]
# }