# -*- coding: utf-8 -*-
import pandas as pd

def filter_with_weight(df, weight_variable):
    """
    Filter dataset for rows with a positive int weight. Drops 0 or NA weights.

    Parameters
    ----------
    df : pandas DataFrame
        dataframe to be filtered
    weight_variable : str
        weight variable name

    Returns
    -------
    filtered_df : pandas DataFrame
        dataframe that has been filtered for positive `weight_variable`
    """
    filtered_df = df.loc[df[weight_variable] > 0]
    return filtered_df


def filter_with_values(df, variable, values):
    """
    Filter dataset for rows containing a specific value in a variable column.
    
    Parameters
    ----------
    df : pandas DataFrame
        dataframe to be filtered
    variable : str
        name of variable to be used for filtering
    values : int/float or list
        value, or list of values, to filter for in variable column

    Returns
    -------
    filtered_df : pandas DataFrame
        dataframe that has been filtered for value in variable column
    """
    if isinstance(values, (int, float)):
        values = [values]  # Coerce to list when single value, for isin()
    filtered_df = df.loc[df[variable].isin(values)]
    return filtered_df
