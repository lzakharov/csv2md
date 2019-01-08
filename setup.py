from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='csv2md',
    version='1.0.1',
    description='Command line tool for converting CSV files into Markdown tables.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Lev Zakharov',
    author_email='l.j.zakharov@gmail.com',
    url='https://github.com/lzakharov/csv2md',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'csv2md = csv2md:main'
        ]
    }
)
