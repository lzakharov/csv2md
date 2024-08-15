# csv2md  [![codecov](https://codecov.io/gh/lzakharov/csv2md/graph/badge.svg?token=bqqWCT4BNo)](https://codecov.io/gh/lzakharov/csv2md)

Command line tool for converting CSV files into Markdown tables or headings.

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

Generate Markdown table from TSV file:

```commandline
csv2md -d $'\t' table.tsv
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

You can also generate headings instead of a table by including the flag `-O` or `--output-headings`, for example:

```commandline
csv2md table.csv -O
```

will output something like:

```md
## **Col-A Row-1 Label**: Col-A Row-1 Value

- **Col-B Row-1 Label**: Col-B Row-1 Value
- **Col-C Row-1 Label**: Col-C Row-1 Value

## **Col-A Row-2 Label**: Col-A Row 2 Value

...and so on...
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
usage: csv2md [-h] [-d DELIMITER] [-q QUOTECHAR] [-C COLUMNS]
              [-c [CENTER_ALIGNED_COLUMNS ...]]
              [-r [RIGHT_ALIGNED_COLUMNS ...]] [-H]
              [-O] [-t HEADING_COL_INDEX] [-l HEADING_LEVEL]
              [CSV_FILE ...]

Parse CSV files into Markdown tables.

positional arguments:
  CSV_FILE              One or more CSV files to parse

options:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        delimiter character. Default is ','
  -q QUOTECHAR, --quotechar QUOTECHAR
                        quotation character. Default is '"'
  -C COLUMNS, --columns COLUMNS
                        comma-separated list of column indices or ranges (from
                        zero) to be processed, e.g. "0,3-5,7". Indices out of
                        range will be ignored
  -c [CENTER_ALIGNED_COLUMNS ...], --center-aligned-columns [CENTER_ALIGNED_COLUMNS ...]
                        column numbers with center alignment (from zero)
  -r [RIGHT_ALIGNED_COLUMNS ...], --right-aligned-columns [RIGHT_ALIGNED_COLUMNS ...]
                        column numbers with right alignment (from zero)
  -H, --no-header-row   specify that the input CSV file has no header row.
                        Will create default headers in Excel format
                        (a,b,c,...)
  -O, --output-headings
                        specify that the output should be headings
  -t HEADING_COL_INDEX, --heading-column HEADING_COL_INDEX
                        index of the column to use as the top-level heading of each row
  -l HEADING_LEVEL, --heading-level HEADING_LEVEL
                        heading level for the top-level heading of each row
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
