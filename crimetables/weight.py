# -*- coding: utf-8 -*-
def apply_weight(df, weight_variable, variable_names):
    """
    Apply weight column to the specified variables of a dataframe, by
    multiplication. Both the weight variable and variables to be weighted
    should be in the provided dataframe.
    
    Parameters
    ----------
    df : pandas DataFrame
        dataframe containing columns to be weighted
    weight_variable : str
        weight variable name
    variable_names : list
        list of variables that should be weighted

    Returns
    -------
    weighted_df : pandas DataFrame
        dataframe containing weighted variables
    """
    weighted_df = df.copy()
    weighted_df.loc[:, variable_names] = (
        weighted_df.loc[:, variable_names]
        .multiply(weighted_df.loc[:, weight_variable], axis = 0)
        )
    return weighted_df
