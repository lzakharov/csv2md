import sys
import argparse
import csv


def csv_to_table(file, delimiter=',', quotechar='"'):
    try:
        return list(csv.reader(file, delimiter=delimiter, quotechar=quotechar))
    except csv.Error as e:
        print(e, file=sys.stderr)
        print('Something went wrong...')
        print('Exiting...')
        sys.exit(1)


def get_table_widths(table):
    table_lengths = [[len(cell) for cell in row] for row in table]
    return list(map(max, zip(*table_lengths)))


def table_to_md(table):
    table_widths = get_table_widths(table)

    md_table = ['| ' + ' | '.join([cell.ljust(width) for cell, width in zip(row, table_widths)]) + ' |'
                for row in table]

    md_table.insert(1, '| ' + ' | '.join(['-' * width for width in table_widths]) + ' |')

    return '\n'.join(md_table)


def main():
    parser = argparse.ArgumentParser(description='Parse CSV files into Markdown tables.')
    parser.add_argument('files', metavar='CSV_FILE', type=argparse.FileType('r'), nargs='*',
                        help='One or more CSV files to parse')
    parser.add_argument('-d', '--delimiter', metavar='DELIMITER', type=str, nargs='?', default=',',
                        help='delimiter character. Default is \',\'')
    parser.add_argument('-q', '--quotechar', metavar='QUOTECHAR', type=str, nargs='?', default='"',
                        help='quotation character. Default is \'"\'')
    args = parser.parse_args()

    if not args.files:
        print(table_to_md(csv_to_table(sys.stdin, delimiter=args.delimiter, quotechar=args.quotechar)))
    else:
        for file in args.files:
            print(table_to_md(csv_to_table(file, delimiter=args.delimiter, quotechar=args.quotechar)))


if __name__ == '__main__':
    main()
