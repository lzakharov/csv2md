import csv


class Table:
    def __init__(self, cells):
        self.cells = cells
        self.widths = list(map(max, zip(*[list(map(len, row)) for row in cells])))

    def markdown(self, center_aligned_columns=None, right_aligned_columns=None):
        def format_row(row):
            return '| ' + ' | '.join(row) + ' |'

        rows = [format_row([cell.ljust(width) for cell, width in zip(row, self.widths)]) for row in self.cells]
        separators = ['-' * width for width in self.widths]

        if right_aligned_columns is not None:
            for column in right_aligned_columns:
                separators[column] = ('-' * (self.widths[column] - 1)) + ':'
        if center_aligned_columns is not None:
            for column in center_aligned_columns:
                separators[column] = ':' + ('-' * (self.widths[column] - 2)) + ':'

        rows.insert(1, format_row(separators))

        return '\n'.join(rows)

    @staticmethod
    def parse_csv(file, delimiter=',', quotechar='"'):
        return Table(list(csv.reader(file, delimiter=delimiter, quotechar=quotechar)))
