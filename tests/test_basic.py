from .context import csv2md
import unittest
import io


normal_csv = (
    'year,make,model,description,price\n'
    '1997,Ford,E350,"ac, abs, moon",3000.00\n'
    '1999,Chevy,"Venture «Extended Edition»","",4900.00\n'
    '1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00\n'
)

normal_table = [
    ['year', 'make', 'model', 'description', 'price'],
    ['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00'],
    ['1999', 'Chevy', 'Venture «Extended Edition»', '', '4900.00'],
    ['1996', 'Jeep', 'Grand Cherokee', 'MUST SELL! air, moon roof, loaded', '4799.00']
]

normal_table_widths = [4, 5, 26, 33, 7]

normal_md = (
    '| year | make  | model                      | description                       | price   |\n'
    '| ---- | ----- | -------------------------- | --------------------------------- | ------- |\n'
    '| 1997 | Ford  | E350                       | ac, abs, moon                     | 3000.00 |\n'
    '| 1999 | Chevy | Venture «Extended Edition» |                                   | 4900.00 |\n'
    '| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air, moon roof, loaded | 4799.00 |'
)


class BasicTestSuit(unittest.TestCase):
    """Basic test cases."""
    def test_csv_to_table_on_normal_csv(self):
        self.assertEqual(csv2md.csv_to_table(io.StringIO(normal_csv)), normal_table)

    def test_get_table_widths_on_normal_table(self):
        self.assertEqual(csv2md.get_table_widths(normal_table), normal_table_widths)

    def test_table_to_md_on_normal_table(self):
        self.assertEqual(csv2md.table_to_md(normal_table), normal_md)


if __name__ == '__main__':
    unittest.main()