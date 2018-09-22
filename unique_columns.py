"""
This script will read through a .csv file and gather the unique values for the provided headers.

usage:

python unique_columns.py path/to/input.csv -l 'column1' 'column2' 'column3'


output will be written to the file output.csv

"""

import argparse
import csv

if __name__== "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument('-l', '--list-headers', nargs='+', default=[], required=True,help= "<Required> list of quoted column headers like -l 'column1' 'column2' 'column three' ")
    args = parser.parse_args()

    output_file = 'output.csv'

    headers = args.list_headers

    uniques = set()
    with open(args.input_file) as handle:
        csv_dict = csv.DictReader(handle)
        for row in csv_dict:
            entry = tuple([row[header] for header in headers])
            uniques.add(entry)

    output_lines = sorted(list(uniques), key=lambda x:int(x[0]) if x[0].isdigit() else x[0])
    with open(output_file,'w') as handle:

        handle.write(','.join(headers)+'\n')

        for unique in output_lines:
            out_line = ','.join(unique) + '\n'
            handle.write(out_line)




