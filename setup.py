import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setup(
    name='crimetables',
    version='0.0.0',
    author='David Foster',
    description='A pipeline to calculate and produce Crime Survey tables, for publication.',
    packages=find_packages(),    
    install_requires=required
)