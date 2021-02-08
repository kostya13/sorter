from setuptools import setup

setup(
    name='sorter',
    version='1.0',
    author='Konstantin Ilyashenko',
    packages=['sorter'],
    description='Simple sorter',
    install_requires=['click'],
    entry_points={'console_scripts': ['sorter = sorter.main:sorter']},
)