import argparse
import sys

from .table import Table
from .exceptions import BaseError, ColumnIdentifierError


def main():
    parser = argparse.ArgumentParser(
        description='Parse CSV files into Markdown tables.')
    parser.add_argument('files', metavar='CSV_FILE', type=argparse.FileType('r'), nargs='*',
                        help='One or more CSV files to parse')
    parser.add_argument('-d', '--delimiter', metavar='DELIMITER', type=str, default=',',
                        help='delimiter character. Default is \',\'')
    parser.add_argument('-q', '--quotechar', metavar='QUOTECHAR', type=str, default='"',
                        help='quotation character. Default is \'"\'')
    parser.add_argument('-C', '--columns', dest='columns', type=str, default=None,
                        help='comma-separated list of column indices or ranges (from zero) to be processed, e.g. "0,3-5,7". Indices out of range will be ignored')
    parser.add_argument('-c', '--center-aligned-columns', metavar='CENTER_ALIGNED_COLUMNS', nargs='*',
                        type=int, default=[], help='column numbers with center alignment (from zero)')
    parser.add_argument('-r', '--right-aligned-columns', metavar='RIGHT_ALIGNED_COLUMNS', nargs='*',
                        type=int, default=[], help='column numbers with right alignment (from zero)')
    parser.add_argument('-H', '--no-header-row', dest='no_header_row', action='store_true',
                        help='specify that the input CSV file has no header row. Will create default headers in Excel format (a,b,c,...)')
    parser.add_argument('-O', '--output-headings', dest='output_headings', action='store_true',
                        help='specify that the output should be headings')
    parser.add_argument('-t', '--heading-column', dest='heading_col_index', type=str, default=0,
                        help='index of the column to use as the top-level heading of each row')
    parser.add_argument('-l', '--heading-level', dest='heading_level', type=int, default=2,
                        help='heading level for the top-level heading of each row')
    args = parser.parse_args()

    try:
        columns = parse_columns(args.columns)
    except BaseError as e:
        parser.error(e)

    for file in [sys.stdin] if not args.files else args.files:
        table = Table.parse_csv(file, args.delimiter, args.quotechar, columns)
        if args.output_headings:
            print(table.markdown_headings(args.heading_col_index, args.heading_level, args.no_header_row))
        else:
            print(table.markdown(args.center_aligned_columns, args.right_aligned_columns, args.no_header_row))


def parse_columns(columns):
    if not columns:
        return None

    result = []

    for c in columns.split(','):
        if '-' in c:
            try:
                a, b = map(int, c.split('-', 1))
            except ValueError:
                raise ColumnIdentifierError(c)

            result.extend(range(a, b + 1))
        else:
            if not c.isdecimal():
                raise ColumnIdentifierError(c)

            column = int(c)
            result.append(column)

    return result


if __name__ == '__main__':
    main()
