import pycountry
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)

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
    dataset = {}
    years_list = [year.rstrip() for year in description[1]]
    absent_data = ': '
    for entry in raw_data:
        country = get_country_name(entry[0])
        dataset[country] = []
        i = 0
        for coverage in entry[1]:
            if coverage is not absent_data:
                dataset[country].append(dict(year = years_list[i], coverage= get_numeric_value(coverage)))
                i += 1
    return(dataset)

def get_country_name(country_iso):
    country_details = pycountry.countries.get(alpha_2=country_iso)
    if country_details != None:
        return(country_details.name)
    else:
        return(country_iso)

def get_numeric_value(string):
    numeric_value = re.findall('\d+', string)
    return(int(numeric_value[0]))

def get_country_data(dataset, country_iso):
    country = get_country_name(country_iso)
    data = []
    for entry in dataset.get(country):
        data.append((entry.get('year'), entry.get('coverage')))
    country_data = {country: data}
    return(country_data)

#Prepare and print dataset (used PrettyPrinter for more user-friendly interpretation)
dataset = prepare_dataset(description,raw_data)
pp.pprint(dataset)

#Retrieve data for a specific country
print(get_country_data(dataset, 'ME'))

