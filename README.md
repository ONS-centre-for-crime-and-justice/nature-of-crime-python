# The crimetables package for Python

crime-tables-python is a python package for producing the Nature of Crime tables from the Crime Survey England and Wales. 

It produces .xlsx files by runnning the pandas dataframes through the gptables package. You define the mapping from your data to elements of the table. It does the rest.

crime-tables-python uses gptables and uses the official guidance on good practice spreadsheets. It advocates a strong adherence to the guidance by restricting the range of operations possible. 

crime-tables-python uses a custom 'crimetheme' built upon the default gptheme theme.

crime-tables-python is developed and maintained by the Centre for Crime and Justice in the Office for National Statistics, UK.

For more information on this code please contact crimestatistics@ons.gov.uk

## Installation and use:

For development, install the package from a local repo using:

```
pip install -e crime-tables-python
```

To uninstall, use:

```
pip uninstall crimetables
```


## Testing

To run unit tests, go to `crimetables\docs` and use:

```
make tests
```

## Documentation

To build docs, install sphinx and then go to `crimetables\docs` and use:

```
make html
```