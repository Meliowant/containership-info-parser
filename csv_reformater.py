"""
This script takes csv file created by containership_parser and reformat it so
each ship will occupy one row.
"""

import csv
from collections import OrderedDict


def main():
    data = OrderedDict()
    with open('container_table.csv', 'w', newline='') as csvtarget:
        shipwriter = csv.writer(csvtarget, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        with open('container.csv', newline='') as csvfile:
            shipreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            fields = []
            for row in shipreader:
                ship_id = row[0]
                field_name = row[1]
                field_value = row[2]

                if ship_id not in data.keys():
                    data[ship_id] = {}
                data[ship_id][field_name] = field_value
                if field_name not in fields:
                    fields.append(field_name)

            for ship in data.keys():
                row = []
                for field in fields:
                    if field in data[ship].keys():
                        row.append(data[ship][field])
                    else:
                        row.append('')
                shipwriter.writerow(row)

        shipwriter.writerow(fields)


if __name__ == '__main__':
    main()
