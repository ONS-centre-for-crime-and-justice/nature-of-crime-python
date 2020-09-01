# -*- coding: utf-8 -*-

import pandas as pd
import os

def read_csv_data_in_directory(directory_path, variables_to_keep = []):
    """
    Read a directory of .csv files and merges them into a single data frame
    
    Paramters
    ---------
    directory_path : str
        absolute path to directory containing csv files
    variables_to_keep : list (optional)
        variables to keep in `cumulative_df`
    
    Raises
    ------
    ValueError
        when directory contains a file that is not a .csv
    
    Returns
    -------
    cumulative_df : pandas.DataFrame
        data from all csvs in the directory
    """
    files_in_folder = os.listdir(directory_path)
    
    cumulative_df = None
    for file in files_in_folder:
        if not file.endswith(".csv"):
            raise ValueError(f"{file} is not a .csv file")

        absolute_path = os.path.join(directory_path, file)
        data_from_file = pd.read_csv(absolute_path)
        if cumulative_df is None:
            cumulative_df = data_from_file
        else:
            cumulative_df = cumulative_df.append(data_from_file)
        
        filtered_df = cumulative_df[variables_to_keep]
    return filtered_df
    
