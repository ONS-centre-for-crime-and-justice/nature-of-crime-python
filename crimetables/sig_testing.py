# -*- coding: utf-8 -*-
import math  
import numbers
import pandas as pd
import crimetables as ct
import numpy as np
import statistics

def sig_test_crime(estimate_1, estimate_2, base_1, base_2, design_1 = 1.2,
                 design_2 = 1.2, threshold = 1.96):
    """
    Calculates significance testing between two estimates (populations) using a z-test. 
    Result from test will indicaite if estimates from populations are significantly different.
    Function also handles significance for missing data by setting significance to ':'
    
    Parameters
    ----------
    estimate_1 : int, float
        estimated proportion of a population.
    estimate_2 : int, float
        a different estimated proportion of a population.
    base_1 : int
        sample size for estimate 1.
    base_2 : int
        sample size for estimate 2.
    design_1 : int, float
        the model design effect associated with estimate_1. Defaults to 1.2 for crime survey data.
    design_1 : int, float
        the model design effect associated with estimate_1. Defaults to 1.2 for crime survey data.
    threshold : int, float
        threshold threshold for determining significance Defaults to 1.96 for the 5% level.
    Returns
    -------
    int
        a Boolean value indicating whether the populations significantly differ.
    Raises
    -------
    
    Notes
    -----
    This significance test will not work for testing differences between numbers of incidents/victims on the CSEW.
    This test is only for testing proportions.
    """
    if not (isinstance(estimate_1, (numbers.Integral, float)) and isinstance(estimate_2, (numbers.Integral, float))):
      raise TypeError("Function expects numbers for estimate_1 and estimate_2 which need to be input as integers not strings")
      
    if not (isinstance(base_1, (numbers.Integral)) and isinstance(base_2, (numbers.Integral))):
      raise TypeError("Function expects whole numbers for base_1 and base_2 which need to be input as integers not strings") 
      
    if (estimate_1 == np.inf) or (estimate_2 == np.inf):
        is_significant = ':'
        
    else:

        est_1_proportion = estimate_1 / 100
    
        est_2_proportion = estimate_2 / 100
    
        est_1_std_dev = math.sqrt(est_1_proportion * (1 - est_1_proportion))
        est_2_std_dev = math.sqrt(est_2_proportion * (1 - est_2_proportion))
    
        est_1_std_err = est_1_std_dev / math.sqrt(base_1)
        est_2_std_err = est_2_std_dev / math.sqrt(base_2)
    
        design_effect_1 = est_1_std_err * design_1
        design_effect_2 = est_2_std_err * design_2
    
        est_est = est_1_proportion - est_2_proportion
    
        z_score = est_est / math.sqrt((design_effect_1 * design_effect_1) + (design_effect_2 * design_effect_2))
        
        if ((threshold <= z_score) | ((threshold * - 1) >= z_score)):
            is_significant = '*'
        else :
            is_significant = ' '
  
    return(is_significant)


def previous_year_sig_test(row, bases):
    
    """
    Function to apply the significance testing function to every row in a dataframe.
    This test is specifically for comparing current year to previous year.
    
    Parameters
    ----------
    row : row in a pd.DataFrame
        a row where we want to sig test the last two estimates.
    bases : series
        the unweighted bases for the estimates being picked up in the row.

    Returns
    -------
    int : 
        the result of the significance test for each row in a pd.DataFrame.
    
    """
    
    if isinstance(bases, pd.DataFrame):
        bases = bases.iloc[0]
    
    return ct.sig_testing.sig_test_crime(row.iloc[-3], row.iloc[-2], bases.iloc[-3], bases.iloc[-2])
   
    
def ten_year_sig_test(row, bases):
    
    """
    Function to apply the significance testing function to every row in a dataframe.
    This test is specifically for comparing current year to first year in the series.
    
    Parameters
    ----------
    row : row in a pd.DataFrame
        a row where we want to sig test the last two estimates.
    bases : series
        the unweighted bases for the estimates being picked up in the row.

    Returns
    -------
    int : 
        the result of the significance test for each row in a pd.DataFrame.
    
    """
    
    if isinstance(bases, pd.DataFrame):
        bases = bases.iloc[0]
    
    return ct.sig_testing.sig_test_crime(row.iloc[1], row.iloc[-1], bases.iloc[1], bases.iloc[-1])



def standard_deviation(df, variable, year, mean):
    
     """
    Function to apply calculate the standard deviation of a specific
    variables mean.
    
    Uses the stqatistics package function to return the sample standard deviation
    (the square root of the sample variance).
    
    Parameters
    ----------
    df : pd.DataFrame
        dataframe containing all relevant cases.
        
    variable : str
        the variable needed to calculate its standard deviation.
        
    year : str
        specific year standard deviation wants to be calculated for.
        
    mean : int/flt
        mean used within the caluclation for standard deviation

    Returns
    -------
    sd : float 
        the result of the standard deviation calculation
    
    """
     df1 = df[(df['financial_year'] == year)]

     df1 = df1[[variable]]

     sample = (df1[variable])

     sd = statistics.stdev(sample, mean) 
    
     return sd



def sig_test_mean(mean_1, mean_2, base_1, base_2, sd1, sd2, design_effect = 1.2, threshold = 1.96):
    """
    Calculates significance testing between two means using a z-test. 
    Result from test will indicaite if estimates from populations are significantly different.
    
    Parameters
    ----------
    mean_1 : int, float
        estimated mean of a population.
    mean_2 : int, float
        a different estimated mean of a population.
    base_1 : int
        sample size for mean 1.
    base_2 : int
        sample size for mean 2.
    sd1 : float
        standard deviation for mean_1
    sd2 : float
        standard deviation for mean_2
    design_1 : int, float
        the model design effect associated with mean_1. Defaults to 1.2 for crime survey data.
    design_1 : int, float
        the model design effect associated with mean_1. Defaults to 1.2 for crime survey data.
    threshold : int, float
        threshold threshold for determining significance Defaults to 1.96 for the 5% level.
    Returns
    -------
    int
        a Boolean value indicating whether the populations significantly differ.
    Raises
    -------
    
    Notes
    -----
    This significance test will not work for testing differences between numbers of incidents/victims on the CSEW.
    This test is only for testing means.
    """
        
    sd1_sqr = sd1 * sd1
    
    sd2_sqr = sd2 * sd2
    
    sd1_sqr_over_base = sd1_sqr / base_1

    sd2_sqr_over_base = sd2_sqr / base_2
    
    var_diff = sd1_sqr_over_base + sd2_sqr_over_base
    
    SE_diff = math.sqrt(var_diff)
    
    mean_diff = mean_1 - mean_2
    
    mean_diff_over_SE_diff = mean_diff / SE_diff
    
    divide_by_DE = mean_diff_over_SE_diff / design_effect
    
    z_score = divide_by_DE
    
    if ((threshold <= z_score) | ((threshold * - 1) >= z_score)):
            is_significant = '*'
    else :
            is_significant = ' '
  
    return is_significant

def ten_year_sig_test_means(subtable, subtable_data, variable, bases):
    """
    Function to pull all necesarry values for the mean significance testing function together
    and run the mean sig testing.
    
    This function runs the standard_deviation within it and uses the numbers from that to populate the sig_test_mean function.
    You will not need to run the standard deviation function seperately to this function.
    
    Ten year sig test will need to be run before the previous year sig test.
    
    Parameters
    ----------
    subtable : Series
        a row where we want to sig test to pick up the means. 
    subtable_data : pd.DataFrame
        full pd dataframe to calculate the standard deviation of the mean.
    variable : str
        variable for calcultaing the standard deviation
    bases : series
        the unweighted bases for the means being picked up in the subtable.

    Returns
    -------
    int : 
        the result of the significance test for each row in a pd.DataFrame.
    
    """
    
    if isinstance(bases, pd.DataFrame):
        bases = bases.iloc[0]
    
    if isinstance(subtable, pd.DataFrame):
        subtable = subtable.iloc[0]
    
    earliest_mean = subtable.iloc[1]
    latest_mean = subtable.iloc[-1]
    
    earliest_year = subtable.index[1]
    latest_year = subtable.index[-1]

    earliest_sd = standard_deviation(subtable_data, variable, earliest_year, earliest_mean)

    latest_sd = standard_deviation(subtable_data, variable, latest_year, latest_mean)
    
    earliest_base = bases.iloc[1]
    latest_base =  bases.iloc[-1]
    
    return sig_test_mean(earliest_mean, latest_mean, earliest_base, latest_base, earliest_sd, latest_sd)


def previous_year_sig_test_means(subtable, subtable_data, variable, bases):
     """
    Function to pull all necesarry values for the mean significance testing function together
    and run the mean sig testing.
    
    This function runs the standard_deviation within it and uses the numbers from that to populate the sig_test_mean function.
    You will not need to run the standard deviation function seperately to this function.
    
    Ten year sig test will need to be run before the previous year sig test.
    
    Parameters
    ----------
    subtable : Series
        a row where we want to sig test to pick up the means .
    subtable_data : pd.DataFrame
        full pd dataframe to calculate the standard deviation of the mean.
    variable : str
        variable for calcultaing the standard deviation.
    bases : series
        the unweighted bases for the means being picked up in the subtable.

    Returns
    -------
    int : 
        the result of the significance test for each row in a pd.DataFrame.
    
    """
    
     if isinstance(bases, pd.DataFrame):
        bases = bases.iloc[0]
    
     if isinstance(subtable, pd.DataFrame):
        subtable = subtable.iloc[0]
    
     earliest_mean = subtable.iloc[-3]
     latest_mean = subtable.iloc[-2]
    
     earliest_year = subtable.index[-3]
     latest_year = subtable.index[-2]

     earliest_sd = standard_deviation(subtable_data, variable, earliest_year, earliest_mean)

     latest_sd = standard_deviation(subtable_data, variable, latest_year, latest_mean)
    
     earliest_base = bases.iloc[-3]
     latest_base =  bases.iloc[-2]
    
     return sig_test_mean(earliest_mean, latest_mean, earliest_base, latest_base, earliest_sd, latest_sd)
