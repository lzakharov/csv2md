import sys
import csv


def csv_to_table(file, delimiter=',', quotechar='"'):
    return list(csv.reader(file, delimiter=delimiter, quotechar=quotechar))


def table_to_md(table):
    pass


def main(args):
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
