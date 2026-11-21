import io
from unittest import TestCase

from csv2md.table import Table

normal_csv = (
    "year,make,model,description,price\n"
    '1997,Ford,E350,"ac, abs, moon",3000.00\n'
    '1999,Chevy,"Venture «Extended Edition»","",4900.00\n'
    '1996,Jeep,Grand Cherokee,"MUST SELL! air | moon roof | loaded",4799.00'
)

normal_csv_with_custom_delimiter = (
    "year;make;model;description;price\n"
    '1997;Ford;E350;"ac, abs, moon";3000.00\n'
    '1999;Chevy;"Venture «Extended Edition»";"";4900.00\n'
    '1996;Jeep;Grand Cherokee;"MUST SELL! air | moon roof | loaded";4799.00'
)

csv_with_empty_lines = (
    "year,make,model,description,price\n"
    '1997,Ford,E350,"ac, abs, moon",3000.00\n'
    '1999,Chevy,"Venture «Extended Edition»","",4900.00\n'
    "\n"
    '1996,Jeep,Grand Cherokee,"MUST SELL! air | moon roof | loaded",4799.00\n'
    "\n"
)

normal_cells = [
    ["year", "make", "model", "description", "price"],
    ["1997", "Ford", "E350", "ac, abs, moon", "3000.00"],
    ["1999", "Chevy", "Venture «Extended Edition»", "", "4900.00"],
    [
        "1996",
        "Jeep",
        "Grand Cherokee",
        "MUST SELL! air | moon roof | loaded",
        "4799.00",
    ],
]

normal_widths = [4, 5, 26, 35, 7]

filtered_columns_cells = [
    ["year", "model", "description"],
    ["1997", "E350", "ac, abs, moon"],
    ["1999", "Venture «Extended Edition»", ""],
    ["1996", "Grand Cherokee", "MUST SELL! air | moon roof | loaded"],
]

filtered_columns_widths = [4, 26, 35]

cells_with_empty_rows = [
    ["year", "make", "model", "description", "price"],
    ["1997", "Ford", "E350", "ac, abs, moon", "3000.00"],
    ["1999", "Chevy", "Venture «Extended Edition»", "", "4900.00"],
    [],
    [
        "1996",
        "Jeep",
        "Grand Cherokee",
        "MUST SELL! air | moon roof | loaded",
        "4799.00",
    ],
    [],
]

cells_with_newlines = [
    ["year", "make", "model", "description", "price"],
    ["1997", "Ford", "E350", "ac, abs, moon", "3000.00"],
    ["1999", "Chevy", "Venture «Extended Edition»", "", "4900.00"],
    [
        "1996",
        "Jeep",
        "Grand Cherokee",
        "MUST SELL! air\nmoon roof\nloaded",
        "4799.00",
    ],
]

cells_with_narrow_columns = [
    ["1", "2", "3", "4"],
    ["5", "6", "7", "8"],
]

cells_with_ragged_rows = [
    ["region", "note", "units"],
    ["north", "steady", "10"],
    ["south", "spike", "20", "EXTRA"],
    ["east", "flat"],
]

cells_with_short_row_in_middle = [
    ["abc", "def", "ghi"],
    ["j", "k"],
    ["l", "m", "n"],
]

cells_with_short_header = [
    ["one"],
    ["a", "bb"],
    ["ccc", "dddd"],
]

cells_with_extra_field = [
    ["a", "b"],
    ["1", "2", "EXTRA"],
]

normal_md = (
    "| year | make  | model                      | description                           | price   |\n"
    "| ---- | ----- | -------------------------- | ------------------------------------- | ------- |\n"
    "| 1997 | Ford  | E350                       | ac, abs, moon                         | 3000.00 |\n"
    "| 1999 | Chevy | Venture «Extended Edition» |                                       | 4900.00 |\n"
    "| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air \\| moon roof \\| loaded | 4799.00 |"
)

normal_md_with_alignment = (
    "| year | make  | model                      | description                           | price   |\n"
    "| ---- | :---: | :------------------------: | ------------------------------------- | ------: |\n"
    "| 1997 | Ford  | E350                       | ac, abs, moon                         | 3000.00 |\n"
    "| 1999 | Chevy | Venture «Extended Edition» |                                       | 4900.00 |\n"
    "| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air \\| moon roof \\| loaded | 4799.00 |"
)

normal_md_with_default_columns = (
    "| a    | b     | c                          | d                                     | e       |\n"
    "| ---- | ----- | -------------------------- | ------------------------------------- | ------- |\n"
    "| year | make  | model                      | description                           | price   |\n"
    "| 1997 | Ford  | E350                       | ac, abs, moon                         | 3000.00 |\n"
    "| 1999 | Chevy | Venture «Extended Edition» |                                       | 4900.00 |\n"
    "| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air \\| moon roof \\| loaded | 4799.00 |"
)

md_with_empty_rows = (
    "| year | make  | model                      | description                           | price   |\n"
    "| ---- | ----- | -------------------------- | ------------------------------------- | ------- |\n"
    "| 1997 | Ford  | E350                       | ac, abs, moon                         | 3000.00 |\n"
    "| 1999 | Chevy | Venture «Extended Edition» |                                       | 4900.00 |\n"
    "|  |\n"
    "| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air \\| moon roof \\| loaded | 4799.00 |\n"
    "|  |"
)

md_with_newlines_in_cells = (
    "| year | make  | model                      | description                           | price   |\n"
    "| ---- | ----- | -------------------------- | ------------------------------------- | ------- |\n"
    "| 1997 | Ford  | E350                       | ac, abs, moon                         | 3000.00 |\n"
    "| 1999 | Chevy | Venture «Extended Edition» |                                       | 4900.00 |\n"
    "| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air<br>moon roof<br>loaded | 4799.00 |"
)

md_with_flatten_newlines_in_cells = (
    "| year | make  | model                      | description                     | price   |\n"
    "| ---- | ----- | -------------------------- | ------------------------------- | ------- |\n"
    "| 1997 | Ford  | E350                       | ac, abs, moon                   | 3000.00 |\n"
    "| 1999 | Chevy | Venture «Extended Edition» |                                 | 4900.00 |\n"
    "| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air moon roof loaded | 4799.00 |"
)

md_with_narrow_columns_and_alignment = (
    "| 1   | 2 | 3  | 4 |\n| :-: | - | -: | - |\n| 5   | 6 | 7  | 8 |"
)

md_with_ragged_rows = (
    "| region | note   | units |       |\n"
    "| ------ | ------ | ----- | ----- |\n"
    "| north  | steady | 10    |       |\n"
    "| south  | spike  | 20    | EXTRA |\n"
    "| east   | flat   |       |       |"
)

md_with_short_row_in_middle = (
    "| abc | def | ghi |\n| --- | --- | --- |\n| j   | k   |     |\n| l   | m   | n   |"
)

md_with_short_header = "| one |      |\n| --- | ---- |\n| a   | bb   |\n| ccc | dddd |"

md_with_extra_field = "| a | b |       |\n| - | - | ----- |\n| 1 | 2 | EXTRA |"

md_with_default_columns_and_extra_field = (
    "| a | b | c     |\n| - | - | ----- |\n| a | b |       |\n| 1 | 2 | EXTRA |"
)


class TestTable(TestCase):
    def test_markdown_empty_table(self):
        expected = ""
        table = Table([])
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown(self):
        expected = normal_md
        table = Table(normal_cells)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown_with_empty_rows(self):
        expected = md_with_empty_rows
        table = Table(cells_with_empty_rows)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown_with_alignment(self):
        expected = normal_md_with_alignment
        table = Table(normal_cells)
        actual = table.markdown([1, 2], [4])
        self.assertEqual(expected, actual)

    def test_markdown_with_default_columns(self):
        expected = normal_md_with_default_columns
        table = Table(normal_cells)
        actual = table.markdown(no_header_row=True)
        self.assertEqual(expected, actual)

    def test_markdown_with_narrow_columns_and_alignment(self):
        expected = md_with_narrow_columns_and_alignment
        table = Table(cells_with_narrow_columns)
        actual = table.markdown(center_aligned_columns=[0], right_aligned_columns=[2])
        self.assertEqual(expected, actual)

    def test_markdown_with_newlines_in_cells(self):
        expected = md_with_newlines_in_cells
        table = Table(cells_with_newlines)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown_with_newlines_in_cells_custom_replacement(self):
        expected = md_with_flatten_newlines_in_cells
        table = Table(cells_with_newlines)
        actual = table.markdown(newline_replacement=" ")
        self.assertEqual(expected, actual)

    def test_markdown_with_ragged_rows(self):
        expected = md_with_ragged_rows
        table = Table(cells_with_ragged_rows)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_widths_with_ragged_rows(self):
        expected = [6, 6, 5, 5]
        table = Table(cells_with_ragged_rows)
        self.assertEqual(expected, table.widths)

    def test_markdown_with_short_row_in_middle(self):
        expected = md_with_short_row_in_middle
        table = Table(cells_with_short_row_in_middle)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown_with_short_header(self):
        expected = md_with_short_header
        table = Table(cells_with_short_header)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown_with_extra_field(self):
        expected = md_with_extra_field
        table = Table(cells_with_extra_field)
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown_with_default_columns_and_extra_field(self):
        expected = md_with_default_columns_and_extra_field
        table = Table(cells_with_extra_field)
        actual = table.markdown(no_header_row=True)
        self.assertEqual(expected, actual)

    def test_parse_csv(self):
        expected_cells = normal_cells
        expected_widths = normal_widths
        actual = Table.parse_csv(io.StringIO(normal_csv))
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_parse_csv_with_custom_delimiter(self):
        expected_cells = normal_cells
        expected_widths = normal_widths
        actual = Table.parse_csv(
            io.StringIO(normal_csv_with_custom_delimiter), delimiter=";"
        )
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_parse_csv_with_columns(self):
        expected_cells = filtered_columns_cells
        expected_widths = filtered_columns_widths
        actual = Table.parse_csv(io.StringIO(normal_csv), columns=[0, 2, 3])
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_parse_csv_with_invalid_columns(self):
        expected_cells = filtered_columns_cells
        expected_widths = filtered_columns_widths
        actual = Table.parse_csv(
            io.StringIO(normal_csv), columns=[-10, -1, 0, 2, 3, 5, 10, 100]
        )
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_parse_csv_with_empty_lines(self):
        expected_cells = cells_with_empty_rows
        expected_widths = normal_widths
        actual = Table.parse_csv(io.StringIO(csv_with_empty_lines))
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_make_default_headers(self):
        expected = (
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "aa",
            "bb",
            "cc",
            "dd",
            "ee",
            "ff",
            "gg",
        )
        self.assertEqual(Table.make_default_headers(33), expected)
