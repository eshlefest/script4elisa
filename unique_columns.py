"""
This script will read through a .csv file and gather the unique combinations of the provided headers.  The flag -c will
also provide the counts of those unique rows

usage:

python unique_columns.py path/to/input.csv -c -l 'column1' 'column2' 'column3'


output will be written to the file output.csv

"""

import argparse
import csv

from collections import defaultdict
from itertools import chain

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("-c", '--with-counts', default=False, action='store_true')
    parser.add_argument('-l', '--list-headers', nargs='+', default=[], required=True,
                        help="<Required> list of quoted column headers like -l 'column1' 'column2' 'column three' ")
    args = parser.parse_args()

    output_file = 'output.csv'

    headers = args.list_headers
    with_counts = args.with_counts

    uniques = defaultdict(int)
    with open(args.input_file) as handle:
        csv_dict = csv.DictReader(handle)
        for row in csv_dict:
            entry = tuple([row[header] for header in headers])
            uniques[entry] += 1

    if with_counts:
        rows = [tuple(chain(key,[str(value)])) for key,value in uniques.items()]
        output_lines= sorted(list(rows), key=lambda x: int(x[0]) if x[0].isdigit() else x[0])
    else:
        output_lines = sorted(list(uniques.keys()), key=lambda x: int(x[0]) if x[0].isdigit() else x[0])

    with open(output_file, 'w') as handle:

        handle.write(','.join(headers) + '\n')

        for unique in output_lines:
            out_line = ','.join(unique) + '\n'
            handle.write(out_line)
