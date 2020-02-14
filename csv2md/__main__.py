import argparse
import sys

from .table import Table


def main():
    parser = argparse.ArgumentParser(description='Parse CSV files into Markdown tables.')
    parser.add_argument('files', metavar='CSV_FILE', type=argparse.FileType('r'), nargs='*',
                        help='One or more CSV files to parse')
    parser.add_argument('-d', '--delimiter', metavar='DELIMITER', type=str, default=',',
                        help='delimiter character. Default is \',\'')
    parser.add_argument('-q', '--quotechar', metavar='QUOTECHAR', type=str, default='"',
                        help='quotation character. Default is \'"\'')
    parser.add_argument('-c', '--center-aligned-columns', metavar='CENTER_ALIGNED_COLUMNS', nargs='*',
                        type=int, default=[], help='column numbers with center alignment (from zero)')
    parser.add_argument('-r', '--right-aligned-columns', metavar='RIGHT_ALIGNED_COLUMNS', nargs='*',
                        type=int, default=[], help='column numbers with right alignment (from zero)')
    args = parser.parse_args()

    if not args.files:
        table = Table.parse_csv(sys.stdin, args.delimiter, args.quotechar)
        print(table.markdown(args.center_aligned_columns, args.right_aligned_columns))
        return

    for file in args.files:
        table = Table.parse_csv(file, args.delimiter, args.quotechar)
        print(table.markdown(args.center_aligned_columns, args.right_aligned_columns))


if __name__ == '__main__':
    main()
