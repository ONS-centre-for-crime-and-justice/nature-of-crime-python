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

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\other_household_theft\other_household_theft_data.csv')

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

#REMOVING THOSE WITH NO WEIGHT (select if weighti gt 0)
remove_unweighted_cases = ct.filters.filter_with_weight(
        vf_data,
        "c11weighti"
        )

#FILTERING CASES THAT HAPPENED IN ENGLAND AND WALES
correct_area= remove_unweighted_cases[(remove_unweighted_cases['victarea'] == 1) | 
        (remove_unweighted_cases['wherhapp'] == 1)]

##############################################################################
#SELECTING THE OFFENCES FOR THE TABLE 
###############################################################################

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 65)
household_theft_offences = correct_area[
        (correct_area['offence'] == 65)]

household_theft_offences.reset_index(inplace = True)

##################################################################################
#CREATING SUBTABLES
##################################################################################


##################################################################################
#IDENTIFYING THE VARIABLES NEEDED FOR THIS TABLE IN A LIST
##################################################################################

subtable_1_variables = ['whast_h1',
                        'whast_h2',
                        'whast_h3',
                        'whast_h4',
                        'whast_h5',
                        'whast_h6',
                        'whast_h7',
                        'whast_h8',
                        'whast_h9',
                        'whast_h10',
                        'whast_h11',
                        'whast_h12',
                        'whast_h13',
                        'whast_h14',
                        'whast_h15',
                        'whast_h16',
                        'whast_h17',
                        'whast_h18',
                        'whast_h19',
                        'whast_h20',
                        'whast_h21',
                        'whast_h22',
                        'whast_h23'
                        ]

##################################################################################
#APPLYING ADDITIONAL FILTERING NEEDED FOR SUBTABLE_2
##################################################################################

household_theft_offences = household_theft_offences[
                           (household_theft_offences['whast_h1'] == 0) |
                           (household_theft_offences['whast_h1'] == 1) ]
                           

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 2
##################################################################################

subtable_base = household_theft_offences.groupby(['financial_year']).sum()
subtable_base.reset_index(inplace = True)

subtable_base = subtable_base[['financial_year','unweighted_base']]
subtable_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
#cREATING SUBTABLE 2
##################################################################################

subtable_1 = ct.table.apply_percentages_binary(household_theft_offences,'financial_year',subtable_1_variables,'c11weighti','Total_C11weighti',lookup_dict)


##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_base = subtable_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_base.reset_index(inplace = True)

##################################################################################
#SORTING IN DESCENDING ORDER AND KEEPING OTHER SEPERATE
##################################################################################

condition = (subtable_1.table_label=='Other')
other = subtable_1[condition]
groups = subtable_1[~condition]

subtable_1 = groups.sort_values(groups.columns[-1], ascending=False)

subtable_1 = pd.concat([
        subtable_1,
        other,
        ], axis = 0)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_base , axis = 1) 
 


##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

household_theft_items_table = pd.concat([
        subtable_1,
        subtable_base,
        ], axis = 0)
household_theft_items_table.reset_index(inplace = True)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

household_theft_items_table.fillna(0, inplace = True)

household_theft_items_table.replace(np.inf, np.nan, inplace = True)

household_theft_items_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = household_theft_items_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

################################################################################
#FINAL TABLE
##################################################################################

household_theft_items_table_2c = household_theft_items_table.drop(['index'], axis = 1)

