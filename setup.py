from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='csv2md',
    version='0.1.0',
    description='Command line tool for converting CSV files into Markdown tables.',
    long_description=readme,
    author='Lev Zakharov',
    author_email='l.j.zakharov@gmail.com',
    url='https://github.com/lzakharov/csv2md',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)