import csv

from .utils import column_letter


class Table:
    def __init__(self, cells):
        self.cells = cells
        self.widths = self.__widths(cells)

    def markdown(
        self,
        center_aligned_columns=None,
        right_aligned_columns=None,
        no_header_row=False,
        newline_replacement="<br>",
    ):
        if len(self.cells) == 0:
            return ""

        def format_cell(cell):
            cell = cell.replace("\r\n", newline_replacement)
            cell = cell.replace("\n", newline_replacement)
            return cell.replace("|", r"\|")

        cells = [[format_cell(cell) for cell in row] for row in self.cells]
        widths = self.__widths(cells)
        if right_aligned_columns is not None:
            for column in right_aligned_columns:
                widths[column] = max(widths[column], 2)  # -:
        if center_aligned_columns is not None:
            for column in center_aligned_columns:
                widths[column] = max(widths[column], 3)  # :-:

        def ljust_row(row):
            row = list(row)
            if row:
                row += [""] * (len(widths) - len(row))
            return [cell.ljust(width) for cell, width in zip(row, widths)]

        def format_row(row):
            return "| " + " | ".join(row) + " |"

        rows = [format_row(ljust_row(row)) for row in cells]
        separators = ["-" * width for width in widths]

        if right_aligned_columns is not None:
            for column in right_aligned_columns:
                separators[column] = ("-" * (widths[column] - 1)) + ":"
        if center_aligned_columns is not None:
            for column in center_aligned_columns:
                separators[column] = ":" + ("-" * (widths[column] - 2)) + ":"

        if no_header_row:
            rows.insert(
                0, format_row(ljust_row(self.make_default_headers(len(widths))))
            )

        rows.insert(1, format_row(separators))

        return "\n".join(rows)

    @staticmethod
    def __widths(cells):
        widths = [0] * max(map(len, cells), default=0)
        for row in cells:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(cell))
        return widths

    @staticmethod
    def parse_csv(file, delimiter=",", quotechar='"', columns=None):
        reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)

        if columns is None:
            cells = list(reader)
        else:
            cells = [[row[i] for i in columns if 0 <= i < len(row)] for row in reader]

        return Table(cells)

    @staticmethod
    def make_default_headers(n):
        return tuple(map(column_letter, range(n)))
