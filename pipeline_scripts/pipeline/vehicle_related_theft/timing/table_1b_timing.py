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
        vf_data,
        "c11weighti"
        )
#FILTERING CASES THAT HAPPENED IN ENGLAND AND WALES
correct_area= remove_unweighted_cases[(remove_unweighted_cases['victarea'] == 1) | 
        (remove_unweighted_cases['wherhapp'] == 1)]

##############################################################################
#SELECTING THE OFFENCES FOR THE TABLE - theft of vehicle
###############################################################################

#SELECTING THE OFFENCES FOR THE TABLE (e.g select if offence = 60,61,62,63,71,72)
vehicle_offences = correct_area[
        ((correct_area['offence'] == 60) | (correct_area['offence'] == 61) |
        (correct_area['offence'] == 62) | (correct_area['offence'] == 63) | 
        (correct_area['offence'] == 71) | (correct_area['offence'] == 72) )
        ]

vehicle_offences = vehicle_offences[
        (vehicle_offences['vehtheft'] == 1)]

vehicle_offences = vehicle_offences[(vehicle_offences['vftype'] == 1)]
        
##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_1_data = vehicle_offences[(vehicle_offences['when1'] == 1) |
                                   (vehicle_offences['when1'] == 2) ]

subtable_1 = ct.table.percentages_nonbinary(subtable_1_data, 'financial_year', 'when1', 'c11weighti', 'total_c11weighti', lookup_dict)

subtable_data = vehicle_offences[(vehicle_offences['time1'] == 1) |
                                 (vehicle_offences['time1'] == 2) |
                                 (vehicle_offences['time1'] == 3) |
                                 (vehicle_offences['time1'] == 4) |
                                 (vehicle_offences['time1'] == 5) |
                                 (vehicle_offences['time1'] == 6) |
                                 (vehicle_offences['time1'] == 7) ]

subtable_2 = ct.table.percentages_nonbinary(subtable_data, 'financial_year', 'time1', 'c11weighti', 'total_c11weighti', lookup_dict)     

subtable_3 = ct.table.percentages_nonbinary(subtable_data, 'financial_year', 'time2', 'c11weighti', 'total_c11weighti', lookup_dict)

subtable_4 = ct.table.percentages_nonbinary(subtable_data, 'financial_year', 'time3', 'c11weighti', 'total_c11weighti', lookup_dict)       

##################################################################################
#CREATING NEW SUBTABLE - NoC review
##################################################################################

subtable_5_data = vehicle_offences[(vehicle_offences['daylight'] < 4)]

subtable_5 = ct.table.percentages_nonbinary(subtable_5_data, 'financial_year', 'daylight', 'c11weighti', 'total_c11weighti',lookup_dict) 

##################################################################################
#CREATING BASES
##################################################################################

subtable_1_base = subtable_1_data.groupby(['financial_year']).sum() 
subtable_1_base.reset_index(inplace=True)
subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]
subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'
        
subtable_2_base = subtable_data.groupby(['financial_year']).sum()
subtable_2_base.reset_index(inplace=True)
subtable_2_base = subtable_2_base[['financial_year','unweighted_base']]
subtable_2_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_5_base = subtable_5_data.groupby(['financial_year']).sum()
subtable_5_base.reset_index(inplace=True)
subtable_5_base = subtable_5_base[['financial_year','unweighted_base']]
subtable_5_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_2 = subtable_2.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_2.reset_index(inplace = True)

subtable_3 = subtable_3.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_3.reset_index(inplace = True)

subtable_4 = subtable_4.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_4.reset_index(inplace = True)

subtable_1_base = subtable_1_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_1_base.reset_index(inplace = True)

subtable_2_base = subtable_2_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_2_base.reset_index(inplace = True)


subtable_5 = subtable_5.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_5.reset_index(inplace = True)

subtable_5_base = subtable_5_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_5_base.reset_index(inplace = True)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 10'] = subtable_2.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_3['Latest year compared with Mar 10'] = subtable_3.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_4['Latest year compared with Mar 10'] = subtable_4.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_5['Latest year compared with Mar 10'] = subtable_5.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_5_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 19'] = subtable_2.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_3['Latest year compared with Mar 19'] = subtable_3.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_4['Latest year compared with Mar 19'] = subtable_4.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_5['Latest year compared with Mar 19'] = subtable_5.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_5_base , axis = 1)

##################################################################################
#PUTTING TABLES TOGETHER
##################################################################################

vehicle_timing_table = pd.concat([
        subtable_1,
        subtable_1_base,
        subtable_2,
        subtable_3,
        subtable_4,
        subtable_2_base,
        subtable_5,
        subtable_5_base,
        ], axis = 0)
vehicle_timing_table.reset_index(inplace = True)

vehicle_timing_table = vehicle_timing_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

vehicle_timing_table.fillna(0, inplace = True)

vehicle_timing_table.replace(np.inf, np.nan, inplace = True)

vehicle_timing_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_timing_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

vehicle_timing_table_order = [1,0,2,17,7,3,8,16,10,4,6,9,5,18,21,19,20,22]
vehicle_timing_table_1b = vehicle_timing_table.reindex(vehicle_timing_table_order)
