# -*- coding: utf-8 -*-
def map_label(row, label_map):
    """
    Creating a touple using two pre-existing columns, then using this touple as the key to look up table label in the dictionary
    
    Parameters:
        row: row
            this function will apply to every row in the dataframe
        label_map: dictionary
            where the label will be identified
            
    Raises: 
    -------
    
    Returns:
    -------
    table_label:str
        the label to be applied to that variable in the output table
    
    """
    key  = (row["variable_name"], row["value_label"])
    table_label = label_map[key]
    return table_label 


def to_financial_year(date_code):
    """
    Caluclate a financial year the individual case occured in
    
    Parameters:
    ----------
    date_code: int
        input code where the first two numbers refer to year and the last two refer to month
    
    Raises: 
    ------
    AssertError
        when datecode does not have a length of 4
        when the last two digits are greater than '12'
        
    Returns:
    -------
    financial year: str 
        four digit code giving the financial year.  
        
    Example:
    -------
    df['financial_year'] = df['date_code'].apply(calculate_financial_year)
    
    """
    
    if (len(str(date_code)) == 3):
        date_code = '0' + str(date_code)
    
    #split date code into year (first 2 numbers) and month (second 2 numbers))
    month = str(date_code)[2: 4]
    year = str(date_code)[: 2]
    
    assert(len(str(date_code)) == 4)
    assert(int(month) < 13)
        
    #if 01, 02, 03 then year - the first 2 numbers.
    if int(month) < 4: 
        financial_year = str(int(year) - 1) + year
    
    #if 04-12 year equals the first 2 number
    if int(month) > 3:
        financial_year= year + str(int(year) + 1)
    
    if (len(str(financial_year)) == 3):
        financial_year = '0' + str(financial_year)
    
    return financial_year
