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


def table_to_md(table, center_fields=set(), right_fields=set()):
    table_widths = get_table_widths(table)

    md_table = ['| ' + ' | '.join([cell.ljust(width) for cell, width in zip(row, table_widths)]) + ' |'
                for row in table]

    header_seps = ['-' * width for width in table_widths]
    for sep in range(1, len(header_seps) + 1):
        if sep in center_fields:
            sep_chars = list(header_seps[sep-1])
            sep_chars[0] = ':'
            sep_chars[-1] = ':'
            header_seps[sep-1] = ''.join(sep_chars)
        elif sep in right_fields:
            sep_chars = list(header_seps[sep-1])
            sep_chars[-1] = ':'
            header_seps[sep-1] = ''.join(sep_chars)


    md_table.insert(1, '| ' + ' | '.join(header_seps) + ' |')

    return '\n'.join(md_table)


def main():
    parser = argparse.ArgumentParser(description='Parse CSV files into Markdown tables.')
    parser.add_argument('files', metavar='CSV_FILE', type=argparse.FileType('r'), nargs='*',
                        help='One or more CSV files to parse')
    parser.add_argument('-d', '--delimiter', metavar='DELIMITER', type=str, default=',',
                        help='delimiter character. Default is \',\'')
    parser.add_argument('-q', '--quotechar', metavar='QUOTECHAR', type=str, default='"',
                        help='quotation character. Default is \'"\'')
    parser.add_argument('--center-fields', metavar='CENTER_FIELDS', type=str, default='',
                        help='fields to center aligned')
    parser.add_argument('--right-fields', metavar='RIGHT_FIELDS', type=str, default='',
                        help='fields to right aligned')
    args = parser.parse_args()
    
    center_fields = set()
    if args.center_fields:
        center_fields = set((int(f) for f in args.center_fields.split(',')))
    right_fields = set()
    if args.right_fields:
        right_fields = set((int(f) for f in args.right_fields.split(',')))

    if not args.files:
        print(table_to_md(
            csv_to_table(
                sys.stdin,
                delimiter=args.delimiter,
                quotechar=args.quotechar),
            center_fields=center_fields,
            right_fields=right_fields))

    else:
        for fh in args.files:
            print(table_to_md(
                csv_to_table(
                    fh,
                    delimiter=args.delimiter,
                    quotechar=args.quotechar),
                center_fields=center_fields,
                right_fields=right_fields))


if __name__ == '__main__':
    main()
