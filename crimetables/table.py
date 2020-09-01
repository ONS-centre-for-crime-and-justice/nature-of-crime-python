# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from crimetables.mapping import map_label

def percentages_nonbinary(
        df,
        financial_year_variable,
        variable,
        weight_variable, 
        total_weight_variable, 
        label_map
        ):
    """
    Calculate the percentages each variables response makes as part of the total
    
    Parameters:
    ----------
        df: Pandas DataFrame
            The dataframe contains the data you want to run the function on 
        financial_year_variable: str
            the variable used to group responses by individual years.
        variable: str
            the variable containing where percentages will be calculated for the response catagories
        weight_variable: str
            the variable used to establish the sum of the weights for each response catagory
        total_weight_variable: str
            the name of the variable that will be the total weights for each financial year
    
    Returns:
    --------
        df: pandas Dataframe
            Dataframe returning percentage each reponse to a variable makesup of the total reponse    
    """
    
    weights_df = df.groupby([financial_year_variable]).sum()
    
    weights_df = weights_df[[weight_variable]].rename(columns = {weight_variable: total_weight_variable})
    
    df = df.groupby ([financial_year_variable,variable]).sum()
    df.reset_index(inplace = True)
    
    df = df.merge(weights_df, 
                       on = [financial_year_variable])
    
    df["percentage"] = df[weight_variable] / df[total_weight_variable] * 100
    
    df["variable_name"] = variable
        
    df['value_label'] = df[variable]
    
    df['table_label'] = df.apply(map_label, label_map = label_map, axis=1)
        
    df = df[['financial_year','table_label','percentage']]
    
    if len(df) == 0:
        df.loc[1] = [variable, 0]    
    
    return df


def percentages_binary(
        df,
        financial_year_variable,
        variable,
        weight_variable,
        total_weight_variable,
        label_map
        ):
    """
    Calculate the percentages of case where respondants said 'yes' (repsonded 1, instead of 0)
    
    Parameters:
    ----------
        df: Pandas DataFrame
            The dataframe contains the data you want to run the function on 
        financial_year_variable: str
            the variable used to group responses by individual years.
        variable: str
            the variable containing where percentages will be calculated for the response catagories
        weight_variable: str
            the variable used to establish the sum of the weights for each response catagory
        total_weight_variable: str
            the name of the variable that will be the total weights for each financial year
    
    Returns:
    --------
        df: pandas Dataframe
            Dataframe returning percentage of cases where '1' was selected and for cases where there were no '1's return a dataframe of '0'.
            
    """
    
    weights_df = df.groupby([financial_year_variable]).sum()
    
    years_not_available = weights_df.loc[np.isinf(weights_df[variable]), : ].index
    
    weights_df = weights_df[[weight_variable]].rename(columns = {weight_variable: total_weight_variable})
    
    df = df.groupby ([financial_year_variable,variable]).sum()
    df.reset_index(inplace = True)
    
    df = df.merge(weights_df, 
                       on = [financial_year_variable])
    
    df['percentage'] = df[weight_variable] / df[total_weight_variable] * 100
    
    df= df[(df[variable] == 1)]
    
    df = df[['financial_year', 'percentage']]

    df_2 = pd.DataFrame({'financial_year': years_not_available, 'percentage': np.inf})
    
    df = pd.concat([df, df_2], axis = 0, sort = True)

    df['value_label'] = 1
    
    #Section below applies a variable label and table label and financial year so it appears in the final year if no incidents happen.
    #Argument could be made we shouldnt include catagories where no incidents occured.   

    if len(df) == 0:
        df.loc[1] = 0
        #Setting value for empty row to 1 to enable the dictionary to find the table label
        df.loc[1,'value_label'] = 1
        df.loc[1,'financial_year'] = "Apr '09 to Mar '10"
    
    df['variable_name'] = variable
    
    df['table_label'] = df.apply(map_label, label_map = label_map, axis=1)
    
    df = df[['financial_year','table_label','percentage']]
    
    return df


def apply_percentages_binary(
        df,
        financial_year_variable,
        variable_list,
        weight_variable,
        total_weight_variable,
        label_map):
    """
    Applys the percentage_binary function to all variables in a list.
    
    Parameter:
    ---------
        df: Pandas DataFrame
            The dataframe contains the data you want to run the function on
        variable_list: list
            List of variables which the function will be run on
        weight_variable: str
            variable used in the 'calculate percentage' function to gain sum of each catagories weights

    Returns:
    -------
    pd.concat(list_of_dfs): Pandas Dataframe
        A concatented Dataframe of all variables run through the function
    """
    list_of_dfs =[]
    for variable in variable_list:
       list_of_dfs = list_of_dfs+ [percentages_binary(df, financial_year_variable, variable, weight_variable, total_weight_variable, label_map)] 

    return pd.concat(list_of_dfs)

def median_calculation(df, variable, weight):
    """
    Calculates the median value of a variable in a dataframe.
    
    Parameter:
    ---------
        df: Pandas DataFrame
            The dataframe contains the data you want to run the function on
        variable: str
            Variable the median is calculated for
        weight_variable: str
            variable used in the to establish the mid-point of the data

    Returns:
    -------
    df : Pandas Dataframe
        A Dataframe  containing the median value.
    """
    
    df.sort_values(variable, inplace = True)
    cumsum = df[weight].cumsum()
    cutoff = df[weight].sum()/ 2.0
    median = df[variable][cumsum >= cutoff].iloc[0]
    median = {'median' : [median]}
    df2 = pd.DataFrame(median)
    
    return df2
