# Unreleased

* Migrate from `setup.py` to Poetry (`pyproject.toml`)
* Move tests from the package to the `tests/` directory
* Drop support for Python older than 3.9

# 1.7.1 (June 21, 2026)

* Fix replacing `\r\n` with `<br>` before `\n` in cells

# 1.7.0 (June 21, 2026)

* Replace newlines with `<br>` in cells (#34)

# 1.6.0 (April 25, 2026)

* Fix narrow columns alignment (#32)

# 1.5.0 (November 20, 2025)

* Handle empty lines in CSV files (#29)
* Fix `DeprecationWarning`: invalid escape sequence in tests (#25)
* Switch CI from Travis to GitHub Actions (#27)

# 1.4.0 (November 5, 2024)

* Escape pipes in markdown output (#21)

# 1.3.0 (January 6, 2024)

* Support `--columns` flag for filtering columns (#15)

# 1.2.0 (September 8, 2023)

* Support `--no-header-row` flag (#12)
* Pass delimiter and quotechar from parameters (#9)

# 1.1.1 (December 9, 2019)

* Fix setup configuration (#5)

# 1.1.0 (December 9, 2019)

* Add alignment support and do refactoring (#3)

# 1.0.1 (January 8, 2019)

* Make small fixes

# 1.0.0 (February 5, 2018)

* Add support for custom delimiter and quotechar characters
* Add help information into README
* Add Travis CI and Codecov, publish to PyPI

# 0.1.1 (February 5, 2018)

* Fix `main` function
* Add tests for `main` function with standard input

# 0.1.0 (February 4, 2018)

* Initial release: convert CSV files into Markdown tables
