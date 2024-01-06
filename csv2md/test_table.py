import io
from unittest import TestCase

from .table import Table

normal_csv = (
    'year,make,model,description,price\n'
    '1997,Ford,E350,"ac, abs, moon",3000.00\n'
    '1999,Chevy,"Venture «Extended Edition»","",4900.00\n'
    '1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00'
)

normal_csv_with_custom_delimiter = (
    'year;make;model;description;price\n'
    '1997;Ford;E350;"ac, abs, moon";3000.00\n'
    '1999;Chevy;"Venture «Extended Edition»";"";4900.00\n'
    '1996;Jeep;Grand Cherokee;"MUST SELL! air, moon roof, loaded";4799.00'
)

normal_cells = [
    ['year', 'make', 'model', 'description', 'price'],
    ['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00'],
    ['1999', 'Chevy', 'Venture «Extended Edition»', '', '4900.00'],
    ['1996', 'Jeep', 'Grand Cherokee', 'MUST SELL! air, moon roof, loaded', '4799.00']
]

normal_widths = [4, 5, 26, 33, 7]

filtered_columns_cells = [
    ['year', 'model', 'description'],
    ['1997', 'E350', 'ac, abs, moon'],
    ['1999', 'Venture «Extended Edition»', ''],
    ['1996', 'Grand Cherokee', 'MUST SELL! air, moon roof, loaded']
]

filtered_columns_widths = [4, 26, 33]

normal_md = (
    '| year | make  | model                      | description                       | price   |\n'
    '| ---- | ----- | -------------------------- | --------------------------------- | ------- |\n'
    '| 1997 | Ford  | E350                       | ac, abs, moon                     | 3000.00 |\n'
    '| 1999 | Chevy | Venture «Extended Edition» |                                   | 4900.00 |\n'
    '| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air, moon roof, loaded | 4799.00 |'
)

normal_md_with_alignment = (
    '| year | make  | model                      | description                       | price   |\n'
    '| ---- | :---: | :------------------------: | --------------------------------- | ------: |\n'
    '| 1997 | Ford  | E350                       | ac, abs, moon                     | 3000.00 |\n'
    '| 1999 | Chevy | Venture «Extended Edition» |                                   | 4900.00 |\n'
    '| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air, moon roof, loaded | 4799.00 |'
)

normal_md_with_default_columns = (
    '| a    | b     | c                          | d                                 | e       |\n'
    '| ---- | ----- | -------------------------- | --------------------------------- | ------- |\n'
    '| year | make  | model                      | description                       | price   |\n'
    '| 1997 | Ford  | E350                       | ac, abs, moon                     | 3000.00 |\n'
    '| 1999 | Chevy | Venture «Extended Edition» |                                   | 4900.00 |\n'
    '| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air, moon roof, loaded | 4799.00 |'
)


class TestTable(TestCase):
    def test_markdown_empty_table(self):
        expected = ''
        table = Table([])
        actual = table.markdown()
        self.assertEqual(expected, actual)

    def test_markdown(self):
        expected = normal_md
        table = Table(normal_cells)
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

    def test_parse_csv(self):
        expected_cells = normal_cells
        expected_widths = normal_widths
        actual = Table.parse_csv(io.StringIO(normal_csv))
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_parse_csv_with_custom_delimiter(self):
        expected_cells = normal_cells
        expected_widths = normal_widths
        actual = Table.parse_csv(io.StringIO(normal_csv_with_custom_delimiter), delimiter=";")
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
        actual = Table.parse_csv(io.StringIO(normal_csv), columns=[-10, -1, 0, 2, 3, 5, 10, 100])
        self.assertEqual(expected_cells, actual.cells)
        self.assertEqual(expected_widths, actual.widths)

    def test_make_default_headers(self):
        expected = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg')
        self.assertEqual(Table.make_default_headers(33), expected)
