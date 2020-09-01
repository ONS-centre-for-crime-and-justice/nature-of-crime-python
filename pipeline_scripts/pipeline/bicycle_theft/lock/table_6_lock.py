# -*- coding: utf-8 -*-
##################################################################################
#READING IN ALL NECESSARY PACKAGES
##################################################################################

import pandas as pd
import crimetables as ct
import numpy as np

##################################################################################
#FUNCTION TO READ IN ALL CSV FILES TO CREATE A 10 YEAR DATASET
##################################################################################

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\bicycle_theft\bicycle_theft_data.csv')

##################################################################################
#READING IN FILE FOR CREATION OF LABEL DICTIONARY
##################################################################################

label_lookup_file= r"D:\Repos\crime-tables-python\mapping\variable_label_map.csv"

label_lookup_data=pd.read_csv(
        label_lookup_file,)

lookup_keys=zip(label_lookup_data['Variable name'],label_lookup_data['Value'])

lookup_dict=dict(zip(lookup_keys, label_lookup_data['Table label']))

##################################################################################
#APPLYING ALL THE FILTERING FOR TABLES
##################################################################################

remove_unweighted_cases = ct.filters.filter_with_weight(
        vf_data,
        "c11weighti"
        )

correct_area= remove_unweighted_cases[(remove_unweighted_cases['victarea'] == 1) | 
        (remove_unweighted_cases['wherhapp'] == 1)]

##############################################################################
#SELECTING THE OFFENCES FOR THE TABLE 
###############################################################################

bicycle_offences = correct_area[
        (correct_area['offence'] == 64)]

bicycle_offences = bicycle_offences[
        (bicycle_offences['vftype'] == 1)]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_1_data = bicycle_offences[
        (bicycle_offences['bikloc'] < 3)]

subtable_1 = ct.table.percentages_nonbinary(subtable_1_data, 'financial_year', 'bikloc', 'c11weighti', 'total_c11weighti', lookup_dict)

##################################################################################
#CREATING BASES
##################################################################################

subtable_base = subtable_1_data.groupby(['financial_year']).sum() 
subtable_base.reset_index(inplace=True)
subtable_base = subtable_base[['financial_year','unweighted_base']]
subtable_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
#CREATING SUBTABLE 2
##################################################################################

subtable_2_data = subtable_1_data[
        (subtable_1_data['ynbiklca'] < 2) |
        (subtable_1_data['ynbiklcb'] < 2) |
        (subtable_1_data['ynbiklcc'] < 2) |
        (subtable_1_data['ynbiklcd'] < 2) |
        (subtable_1_data['ynbiklce'] < 2) |
        (subtable_1_data['ynbiklcf'] < 2) |
        (subtable_1_data['ynbiklcg'] < 2) |
        (subtable_1_data['ynbiklch'] < 2) |
        (subtable_1_data['ynbiklci'] < 2) |
        (subtable_1_data['financial_year'] == "Apr '09 to Mar '10")]


subtable_2_data = subtable_2_data[(subtable_2_data['ynbiklcj'] == 0) |
                                  (subtable_2_data['ynbiklcj'] == np.inf)]

subtable_2_variables = ['ynbiklca',
                        'ynbiklcb',
                        'ynbiklcc',
                        'ynbiklcd',
                        'ynbiklce',
                        'ynbiklcf',
                        'ynbiklcg',
                        'ynbiklch',
                        'ynbiklci']

##################################################################################
#CREATING SUBTABLE_2
##################################################################################

subtable_2 = ct.table.apply_percentages_binary(subtable_2_data,'financial_year',subtable_2_variables,'c11weighti','total_c11weighti',lookup_dict)

subtable_2_base = subtable_2_data.groupby(['financial_year']).sum() 
subtable_2_base.reset_index(inplace=True)
subtable_2_base = subtable_2_base[['financial_year','unweighted_base']]
subtable_2_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_1_base = subtable_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_1_base.reset_index(inplace = True)

subtable_2 = subtable_2.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_2.reset_index(inplace = True)

subtable_2_base = subtable_2_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_2_base.reset_index(inplace = True)

##################################################################################
#SORTING IN DESCENDING ORDER AND KEEPING OTHER SEPERATE
##################################################################################

subtable_1_order = [0]
subtable_1  = subtable_1.reindex(subtable_1_order)

condition = (subtable_2.table_label=='Other')
other = subtable_2[condition]
groups = subtable_2[~condition]

subtable_2 = groups.sort_values(subtable_2.columns[-1], ascending=False)

subtable_2 = pd.concat([
        subtable_2,
        other,
        ], axis = 0)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 10'] = subtable_2.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 19'] = subtable_2.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 


##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

bicycle_lock_table = pd.concat([
        subtable_1,
        subtable_1_base,
        subtable_2,
        subtable_2_base,
        ], axis = 0)

bicycle_lock_table.reset_index(inplace=True)

bicycle_lock_table_6 = bicycle_lock_table.drop(['index'], axis = 1)


##################################################################################
#FILLING IN MISSING DATA
#################################################################################

bicycle_lock_table_6.fillna(0, inplace = True)

bicycle_lock_table_6.replace(np.inf, np.nan, inplace = True)

bicycle_lock_table_6[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = bicycle_lock_table_6[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#ADDING SUBTABLE TITLES
##################################################################################

bicycle_lock_table_6.insert(loc=0, column='table_title', value=['' for i in range(bicycle_lock_table_6.shape[0])])

bicycle_lock_table_6.loc[2, 'table_title'] = 'Reason why bike was not locked'

