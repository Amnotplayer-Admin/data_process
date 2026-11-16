# OOP Data Processing Lab

## Lab Overview
In this lab I rewrote my data processing code using classes (OOP).
The program reads CSV files (cities and countries) and puts them into tables.
With the tables I can:
- keep only the rows I want (filter)
- calculate things from a column, like the average (aggregate)
- join two tables together using a common column, like `country` (join)
- keep many tables in a small database and search for them by name (DB)

## Project Structure
```
data_process/
│
├── README.md             # This file
├── Cities.csv            # Dataset of cities
├── Countries.csv         # Dataset of countries
└── data_processing.py    # The code (DataLoader, Table, DB, and test code)
```

## Design Overview
There are 3 classes: `DataLoader`, `Table`, and `DB`.

### DataLoader
Reads CSV files.

**Attribute**
- `base_path`: the folder where the CSV files are. If I don't give one, it
  uses the same folder as the Python file.

**Method**
- `load_csv(filename)`: opens a CSV file and returns a list of dictionaries.
  Each dictionary is one row.

### Table
One table of data. A table is a list of dictionaries, and each dictionary
is one row.

**Attributes**
- `table_name`: the name of the table, like `'cities'`
- `table`: the list of dictionaries (all the rows)

**Methods**
- `filter(condition)`: gives a **new** `Table` with only the rows where
  `condition(row)` is True. The old table is not changed.
- `aggregate(aggregation_function, aggregation_key)`: takes all the values
  in one column and gives them to my function (like `sum`, `max`, `len`).
  Values become numbers (float) if they can. If not, they stay as text.
- `join(other_table, common_key)`: joins this table with another table.
  If a row in this table and a row in the other table have the same value
  in `common_key`, the two rows are combined into one dictionary. It gives a
  **new** `Table` named like `cities_countries_joined`. Rows with no match
  in the other table are left out.
- `__str__()`: lets me `print` the table.

### DB
A simple database. It is just a list of `Table` objects.

**Attribute**
- `database`: the list of tables

**Methods**
- `insert(table)`: adds a `Table` to the database.
- `search(table_name)`: finds the table with that name and returns it.
  If there is no such table, it returns `None`.

## How to Test and Run
1. Put `Cities.csv`, `Countries.csv` and `data_processing.py` in the same
   folder.
2. Open a terminal in that folder.
3. Run:
   ```
   python data_processing.py
   ```
4. The test code at the bottom of the file runs. Compare the output with
   the expected result given in the lab. If they are the same, it works.
