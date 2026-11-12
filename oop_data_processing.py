import csv, os


class DataLoader:

    def __init__(self, base_path=None):
        if base_path is None:
            base_path = os.path.dirname(os.path.realpath(__file__))
        self.base_path = base_path

    def load_table(self, filename):
        rows = []
        with open(os.path.join(self.base_path, filename)) as f:
            for r in csv.DictReader(f):
                rows.append(dict(r))
        return Table(filename, rows)


class Table:

    def __init__(self, name, dict_list):
        self.name = name
        self.dict_list = dict_list

    def __len__(self):
        return len(self.dict_list)

    def __str__(self):
        return f"Table '{self.name}' with {len(self.dict_list)} rows"

    def filter(self, condition):
        filtered = []
        for item in self.dict_list:
            if condition(item):
                filtered.append(item)
        return Table(self.name, filtered)

    def aggregate(self, aggregation_key, aggregation_function):
        values = [float(item[aggregation_key]) for item in self.dict_list]
        return aggregation_function(values)

    def column(self, key):
        return [item[key] for item in self.dict_list]


loader = DataLoader()
cities = loader.load_table('Cities.csv')
print(cities)

# Print first 5 cities only
for city in cities.dict_list[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(cities.aggregate('temperature', lambda t: sum(t) / len(t)))
print()

# Print all cities in Germany
print("All cities in Germany:")
germany = cities.filter(lambda x: x['country'] == 'Germany')
print(germany.column('city'))
print()

# Print all cities in Spain with a temperature above 12°C
print("Cities in Spain with a temperature above 12°C:")
spain_warm = cities.filter(
    lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12)
print(spain_warm.column('city'))
print()

# Count the number of unique countries
print("The number of unique countries:")
print(len(set(cities.column('country'))))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature of all the cities in Germany:")
print(germany.aggregate('temperature', lambda t: sum(t) / len(t)))
print()

# Print the max temperature for all the cities in Italy
print("The max temperature of all the cities in Italy:")
italy = cities.filter(lambda x: x['country'] == 'Italy')
print(italy.aggregate('temperature', max))