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


class TestTable(TestCase):
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

