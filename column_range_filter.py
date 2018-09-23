"""
this script will read in a .csv file and filter out all records where the value in the column 'column_name'
does not fall within the range of min - max (inclusinve)

usage:

python column_range_filter.py path/to/dataset.csv column_name min max

example:

python column_range_filter.py ./LA-Juvenile_arrests.csv Age 0 26

this command above will write a file called output.csv that contains all records in LA-Juvenile_arrests that have a 
valie in the column labeled 'Age' that falls between 0 and 26


"""

import argparse

if __name__== "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("column_name", type=str)
    parser.add_argument("min", type=int)
    parser.add_argument("max", type=int)
    args = parser.parse_args()

    output_file = 'output.csv'

    with open(args.input_file) as input_handle, open(output_file,'w') as output_handle:

        header_string = next(input_handle)
        headers = header_string.split(',')

        output_handle.write(header_string)

        column_idx = headers.index(args.column_name)

        for line in input_handle:
            parts = line.split(',')
            if args.min <= int(parts[column_idx]) <= args.max:
                output_handle.write(line)

