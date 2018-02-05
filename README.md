# csv2md [![Build Status](https://travis-ci.org/lzakharov/csv2md.svg?branch=dev)](https://travis-ci.org/lzakharov/csv2md)

Command line tool for converting CSV files into Markdown tables.

## Installation

csv2md can be installed using pip:

```commandline
# type in project directory
python3 -m pip install .
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

## Help

To view help run `csv2md -h`:

```commandline
usage: csv2md.py [-h] [-d [delimiter]] [-q [quotechar]]
                 [CSV_FILES [CSV_FILES ...]].

Parse CSV files into Markdown tables

positional arguments:
  CSV_FILES             CSV files to parse

optional arguments:
  -h, --help            show this help message and exit
  -d [delimiter], --delimiter [delimiter]
                        delimiter character
  -q [quotechar], --quotechar [quotechar]
                        quotation character
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
