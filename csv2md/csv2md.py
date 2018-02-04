import sys
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
    args = sys.argv[1:]

    if not args:
        print(table_to_md(csv_to_table(sys.stdin)))
    else:
        for file in args:
            with open(file) as f:
                print(table_to_md(csv_to_table(f)))


if __name__ == '__main__':
    main()
