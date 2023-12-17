# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_csv(csv_file):
    persons = []
    with open(os.path.join(__location__, f'{csv_file}')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            persons.append(dict(r))
    return persons


# add in code for a Database class


# add in code for a Table class
import copy


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(
            self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for i in self.table:
            if condition(i):
                filtered_table.table.append(i)
        return filtered_table

    def aggregate(self, function, keys):
        just_list1 = []
        for item1 in self.table:
            just_list1.append(float(item1[keys]))
        return function(just_list1)

    def select(self, attribute_list):
        just_list_again = []
        for i in self.table:
            for attribute in attribute_list:
                just_list_again.append(i[attribute])
        return just_list_again

    def print(self):
        for i in self.table:
            print(i)
        return self

    def __str__(self):
        return self.table_name + ':' + str(self.table)


class DB:
    def __init__(self):
        self.database = []
        self.csv_filename = []

    def insert(self, table, file_name):
        self.database.append(table)
        self.csv_filename.append(file_name)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

    def read_csv(self, table_name, file_name):
        data_list = []
        with open(os.path.join(__location__, f'{file_name}')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data_list.append(dict(r))
        tb = Table(table_name, data_list)
        self.insert(tb, file_name)
        return self

    def write_csv(self, name, list_dict):
        if not list_dict:
            with open(name, 'w', newline='', encoding='utf-8') as myFile:
                return
        with open(name, 'w', newline='', encoding='utf-8') as myFile:
            writer = csv.writer(myFile)
            row = [x for x in list_dict[0].keys()]
            writer.writerow(row)
            for dictionary in list_dict:
                writer.writerow(dictionary.values())