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

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\vehicle_related_theft\vehicle_theft_data.csv')

##################################################################################
#READING IN FILE FOR CREATION OF LABEL DICTIONARY
##################################################################################
label_lookup_file= r"D:\repos\crime-tables-python\mapping\variable_label_map.csv"

label_lookup_data=pd.read_csv(
        label_lookup_file,)


lookup_keys=zip(label_lookup_data['Variable name'],label_lookup_data['Value'])

lookup_dict=dict(zip(lookup_keys, label_lookup_data['Table label']))

##################################################################################
#APPLYING ALL THE FILTERING FOR TABLES
##################################################################################

#REMOVING THOSE WITH NO WEIGHT (select if weighti gt 0)
remove_unweighted_cases = ct.filters.filter_with_weight(
        vf_data, "c11weighti")

#FILTERING CASES THAT HAPPENED IN ENGLAND AND WALES
correct_area= remove_unweighted_cases[(remove_unweighted_cases['victarea'] == 1) | 
        (remove_unweighted_cases['wherhapp'] == 1)]

##############################################################################
#SELECTING THE OFFENCES FOR THE TABLE  - Theft of vehicles
###############################################################################

#SELECTING THE OFFENCES FOR THE TABLE (e.g select if offence = 60,61,62,63,71,72)
vehicle_offences = correct_area[
        ((correct_area['offence'] == 60) | (correct_area['offence'] == 61) |
        (correct_area['offence'] == 62) | (correct_area['offence'] == 63) | 
        (correct_area['offence'] == 71) | (correct_area['offence'] == 72) )
        ]
vehicle_offences = vehicle_offences[(
        (vehicle_offences['howbrc_noca'] == 1) | 
        (vehicle_offences['howbrc_nocb'] == 1) | 
        (vehicle_offences['howbrc_nocc'] == 1) | 
        (vehicle_offences['howbrc_nocd'] == 1) | 
        (vehicle_offences['howbrc_noce'] == 1) | 
        (vehicle_offences['howbrc_nocf'] == 1) | 
        (vehicle_offences['howbrc_nocg'] == 1) |
        (vehicle_offences['howbrc_noch'] == 1))
        ]

vehicle_offences = vehicle_offences[(vehicle_offences['vftype'] == 1)]

vehicle_offences = vehicle_offences[
        (vehicle_offences['vehtheft'] == 2)]

##################################################################################
#CREATING BASES
##################################################################################
subtable_1_base = vehicle_offences.groupby(['financial_year']).sum() 
subtable_1_base.reset_index(inplace=True)
subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]
subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'
        
##################################################################################
#IDENTIFYING THE VARIABLES NEEDED FOR THIS TABLE IN A LIST
##################################################################################

subtable_variables = ['howbrc_noca',
                      'howbrc_nocb',
                      'howbrc_nocc',
                      'howbrc_nocd',
                      'howbrc_noce',
                      'howbrc_nocf',
                      'howbrc_nocg',
                      'howbrc_noch'
                      ]

##################################################################################
#CREATING SUBTABLE 2
##################################################################################

subtable_1 = ct.table.apply_percentages_binary(vehicle_offences,'financial_year',subtable_variables,'c11weighti','Total_C11weighti',lookup_dict)
        
##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################
subtable_1 = subtable_1.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_1_base = subtable_1_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_1_base.reset_index(inplace = True)

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

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
 
##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

vehicle_entry_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)
vehicle_entry_table.reset_index(inplace = True)

vehicle_entry_table_3c = vehicle_entry_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
##################################################################################
vehicle_entry_table_3c.fillna(0, inplace = True)

vehicle_entry_table_3c.replace(np.inf, np.nan, inplace = True)

vehicle_entry_table_3c[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_entry_table_3c[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])
        