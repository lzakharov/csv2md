import csv

from .utils import column_letter


class Table:
    def __init__(self, cells):
        self.cells = cells
        self.widths = list(map(max, zip(*[list(map(len, row)) for row in cells])))

    def markdown(self, center_aligned_columns=None, right_aligned_columns=None, no_header_row=False):
        if len(self.cells) == 0:
            return ''

        def ljust_row(row):
            return [cell.ljust(width) for cell, width in zip(row, self.widths)]

        def format_row(row):
            return '| ' + ' | '.join(row) + ' |'

        rows = [format_row(ljust_row(row)) for row in self.cells]
        separators = ['-' * width for width in self.widths]

        if right_aligned_columns is not None:
            for column in right_aligned_columns:
                separators[column] = ('-' * (self.widths[column] - 1)) + ':'
        if center_aligned_columns is not None:
            for column in center_aligned_columns:
                separators[column] = ':' + ('-' * (self.widths[column] - 2)) + ':'

        if no_header_row:
            width = len(self.cells[0])
            rows.insert(0, format_row(ljust_row(self.make_default_headers(width))))

        rows.insert(1, format_row(separators))

        return '\n'.join(rows)

    @staticmethod
    def parse_csv(file, delimiter=',', quotechar='"', columns=None):
        reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)

        if columns is None:
            cells = list(reader)
        else:
            cells = [[row[i] for i in columns if 0 <= i < len(row)] for row in reader]

        return Table(cells)

    @staticmethod
    def make_default_headers(n):
        return tuple(map(column_letter, range(n)))
