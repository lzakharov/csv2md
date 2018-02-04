from csv2md import *


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    if not args:
        print(table_to_md(csv_to_table(sys.stdin)))
    else:
        for file in args:
            with open(file) as f:
                print(table_to_md(csv_to_table(sys.stdin)))


if __name__ == '__main__':
    main()
