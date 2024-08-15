import csv
from typing import Any

from .utils import column_letter


class Table:
    def __init__(self, cells: list[list[Any]]):
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

    def markdown_headings(self, heading_index=0, heading_lvl: str | int = 2, no_header_row=False):
        if len(self.cells) == 0:
            return ''

        # Retrive the header columns
        if no_header_row:
            header_row = tuple('' for _ in range(len(self.cells[0])))
        else:
            header_row = self.cells[0]

        # Retrieve the value of the heading column to be used for each row
        heading_col = header_row[heading_index]

        # Level for the heading to be used for each row
        if isinstance(heading_lvl, int):
            if heading_lvl > 0:
                heading_lvl = '#' * heading_lvl
            else:
                heading_lvl = '#'
        
        def format_label(s):
            return f'**{s}**: ' if s else ''

        def as_heading(lvl, label, val):
            return f'{lvl} {format_label(label)}{val}\n'

        def as_bullet(label, val):
            return f'\n- {format_label(label)}{val}'

        def row_to_lines(row):
            # Add the heading_col's value as a markdown heading
            lines = [as_heading(heading_lvl, heading_col, row[heading_index])]
            # Add all other column values as a bulletted list
            for col_idx, col_val in enumerate(row):
                if col_idx != heading_index:
                    lines.append(as_bullet(header_row[col_idx], col_val))
            lines.append('\n\n')

            return lines

        # Create the lines for each row
        lines: list[str] = []
        if no_header_row:
            for row in self.cells:
                lines.extend(row_to_lines(row))
        else:
            # Header exists, skip the header row
            for row in self.cells[1:]:
                lines.extend(row_to_lines(row))

        return ''.join(lines)

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
