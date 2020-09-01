# -*- coding: utf-8 -*-
import pandas as pd

def to_binary(df, variable_names):
    """
    Recode specified variables of dataframe to binary; any positive value is
    set to 1 and all other values are set to 0. This replaces the existing
    column(s).
    
    Parameters
    ----------
    df : pandas DataFrame
        dataframe containing variables to be recoded
    variable_names : dict
        list of variable names to recode to binary

    Returns
    -------
    recoded_df : pandas DataFrame
        dataframe containing new variables with coding reversed
    """
    recoded_df = df.copy()
    recoded_df[variable_names] = (
            recoded_df[variable_names]
            .astype(bool)
            .astype("int64")
            )
    return recoded_df


def reverse_binary(df, target, new, label, label_map):
    """
    Reverse the binary coding of a single variable and stores the reuslt  as a
    new variable. A new label is stored in the global label map, so that the
    variable may be renamed at a lated stage. The original variable remains in
    the dataset, unless the old name is identical to the new name - in this
    case the old variable and label are overwritten.
    
    Parameters
    ----------
    df : pandas DataFrame
        dataframe containing variables to be recoded
    variable_map : dict
        dictionary containing map of previous variable names to new names

    Returns
    -------
    recoded_df : pandas DataFrame
        dataframe containing new variables with the binary coding of the
        original variables reversed
    """
    recoded_df = df.copy()
    recoded_df[new] = 1 - recoded_df[target]
    
    label_map[new] = label
    
    return recoded_df


def recode_conditionally(df, target, condition, when, value):
    """
    Recode a variable to the specified value, when either any or all of the
    conditional variables match their specified value. All other values of the
    target variable remain unchanged.
    
    Parameters
    ----------
    df : pandas DataFrame
        dataframe containing target variable and conditional variables
    target : str
        name of variable to be recoded
    condition : list
        list of dictionaries mapping variables to the value they must match to
        meet the condition
    when : str
        the number of conditions required to be met to assign `value` to the
        `target` variable. Takes "any" or "all"
    value : int or float
        value to be assigned to target variable when conditions are met

    Returns
    -------
    recoded_df : pandas DataFrame
        dataframe containing recoded target variable   
    
    """
    recoded_df = df.copy()
    
    if when.lower() == "all":
    # Create a mask where all conditions are met
        operator = "&"
    elif when.lower() == "any":
        operator = "|"
    else:
        msg = (f"`when` parameter must be either 'all' or 'any'. {when} was "
                "passed.")
        raise ValueError(msg)
    
    # Move key value pairs from each dict into query string
    query = f" {operator} ".join([f"(recoded_df.{key}=={value})" for pair in condition for key, value in pair.items()])
    mask = pd.eval(query)
    
    recoded_df.loc[mask, target] = value
    
    return recoded_df


def create_variable(df, name, label, label_map, default_value=0):
    """
    Create a new variable (column) in the specified dataframe. The label of
    this variable will be appended the global label map.
    
    Parameters
    ----------
    df : pandas DataFrame
        dataframe to add variable/column to
    name : str
        name of column to be created
    label : str
        label to be assigned to this variable in the global label map
    default_value : int or float
        value to be assigned to every case of new variable (0 by default)

    Returns
    -------
    output_df : pandas DataFrame
        dataframe containing new variable
    """
    output_df = df.copy()
    output_df[name] = default_value
    
    label_map[name] = label
    
    return output_df
