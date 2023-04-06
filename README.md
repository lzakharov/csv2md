# csv2md  [![Build Status](https://app.travis-ci.com/lzakharov/csv2md.svg?branch=master)](https://app.travis-ci.com/lzakharov/csv2md) [![Coverage Status](https://codecov.io/gh/lzakharov/csv2md/branch/dev/graph/badge.svg)](https://codecov.io/gh/lzakharov/csv2md)

Command line tool for converting CSV files into Markdown tables.

## Installation

csv2md can be installed from source:

```commandline
# type in project directory
python setup.py install
```

Or with `pip` from PyPI:
```commandline
pip install csv2md
```

### Requirements

- Python 3.6 or later. See https://www.python.org/getit/

## Usage

Generate Markdown table from CSV file:

```commandline
csv2md table.csv
```

Generate Markdown tables from list of CSV files:

```commandline
csv2md table1.csv table2.csv table3.csv
```

Generate Markdown table from standard input:

```commandline
csv2md
```

You can also use it right inside your code, for example:

```python
from csv2md.table import Table

with open("input.csv") as f:
    table = Table.parse_csv(f)

print(table.markdown())
```

### Examples

Input file: `simple.csv`

```
year,make,model,description,price
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture «Extended Edition»","",4900.00
1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00
```

Output: `csv2md simple.csv`

```
| year | make  | model                      | description                       | price   |
| ---- | ----- | -------------------------- | --------------------------------- | ------- |
| 1997 | Ford  | E350                       | ac, abs, moon                     | 3000.00 |
| 1999 | Chevy | Venture «Extended Edition» |                                   | 4900.00 |
| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air, moon roof, loaded | 4799.00 |
```

Markdown table:

| year | make  | model                      | description                       | price   |
| ---- | ----- | -------------------------- | --------------------------------- | ------- |
| 1997 | Ford  | E350                       | ac, abs, moon                     | 3000.00 |
| 1999 | Chevy | Venture «Extended Edition» |                                   | 4900.00 |
| 1996 | Jeep  | Grand Cherokee             | MUST SELL! air, moon roof, loaded | 4799.00 |

You can also specify delimiter, quotation characters and alignment (see [Help](https://github.com/lzakharov/csv2md#help)). 

## Help

To view help run `csv2md -h`:

```commandline
usage: csv2md [-h] [-d DELIMITER] [-q QUOTECHAR]
              [-c [CENTER_ALIGNED_COLUMNS [CENTER_ALIGNED_COLUMNS ...]]]
              [-r [RIGHT_ALIGNED_COLUMNS [RIGHT_ALIGNED_COLUMNS ...]]]
              [CSV_FILE [CSV_FILE ...]]

Parse CSV files into Markdown tables.

positional arguments:
  CSV_FILE              One or more CSV files to parse

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        delimiter character. Default is ','
  -q QUOTECHAR, --quotechar QUOTECHAR
                        quotation character. Default is '"'
  -c [CENTER_ALIGNED_COLUMNS [CENTER_ALIGNED_COLUMNS ...]], --center-aligned-columns [CENTER_ALIGNED_COLUMNS [CENTER_ALIGNED_COLUMNS ...]]
                        column numbers with center alignment (from zero)
  -r [RIGHT_ALIGNED_COLUMNS [RIGHT_ALIGNED_COLUMNS ...]], --right-aligned-columns [RIGHT_ALIGNED_COLUMNS [RIGHT_ALIGNED_COLUMNS ...]]
                        column numbers with right alignment (from zero)
```

## Running Tests

To run the tests, enter:

```commandline
nosetest
```

## Issue tracker
Please report any bugs and enhancement ideas using the csv2md issue tracker:

https://github.com/lzakharov/csv2md/issues

Feel free to also ask questions on the tracker.

## License

Copyright (c) 2018 Lev Zakharov. Licensed under [the MIT License](https://raw.githubusercontent.com/lzakharov/csv2md/master/LICENSE).
