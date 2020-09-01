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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 60,61,62,63,71,72)
vehicle_offences = correct_area[
        ((correct_area['offence'] == 60) | (correct_area['offence'] == 62))
        ]

#QUESTION ONLY ASKED ON THE LONG VF SO NEED TO PICK THOSE CASES
vehicle_offences= vehicle_offences[(vehicle_offences['vftype'] == 1)]
 
subtable_1_data = vehicle_offences[
        ((vehicle_offences['vehfound'] == 1) | (vehicle_offences['vehfound'] == 2))
        ]

##################################################################################
#CREATING SUBTABLE 1
##################################################################################

subtable_1 = ct.table.percentages_nonbinary(subtable_1_data,'financial_year', 'vehfound', 'c11weighti', 'Total_C11weighti',lookup_dict)

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 1
##################################################################################

subtable_1_base = subtable_1_data.groupby(['financial_year']).sum()
subtable_1_base.reset_index(inplace = True)
subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]
subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_2_data = vehicle_offences[
        ((vehicle_offences['vehdam2'] == 1) | (vehicle_offences['vehdam2'] == 2) | 
        (vehicle_offences['vehdam2'] == 3) | (vehicle_offences['vehdam2'] == 4) |
        (vehicle_offences['vehdam2'] == 5) | (vehicle_offences['vehdam2'] == 6))
        ]

##################################################################################
#CREATING SUBTABLE 2
##################################################################################

subtable_2 = ct.table.percentages_nonbinary(subtable_2_data,'financial_year', 'vehdam2', 'c11weighti', 'Total_C11weighti',lookup_dict)

##################################################################################
#CREATING SUBTABLE 3
##################################################################################

subtable_3 = subtable_2[(subtable_2['table_label'] == 'No damage')]
subtable_3['Damage'] = 100 - (subtable_2['percentage'])

subtable_3 = subtable_3.drop(['percentage'], axis = 1) 
subtable_3['table_label'] = 'Damage'
subtable_3 = subtable_3.rename(columns={"Damage": "percentage"})

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 2
##################################################################################

subtable_2_base = subtable_2_data.groupby(['financial_year']).sum()
subtable_2_base.reset_index(inplace = True)
subtable_2_base = subtable_2_base[['financial_year','unweighted_base']]
subtable_2_base ['table_label'] = 'Unweighted base- number of incidents'

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'
subtable_1_base = subtable_1_base.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'unweighted_base')
subtable_1_base.reset_index(inplace = True)



subtable_2 = subtable_2.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_2.reset_index(inplace = True)

subtable_2_base ['table_label'] = 'Unweighted base - number of incidents'
subtable_2_base = subtable_2_base.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'unweighted_base')
subtable_2_base.reset_index(inplace = True)


subtable_3 = subtable_3.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_3.reset_index(inplace = True)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
 

subtable_2['Latest year compared with Mar 10'] = subtable_2.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 

subtable_2['Latest year compared with Mar 19'] = subtable_2.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
 

subtable_3['Latest year compared with Mar 10'] = subtable_3.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 

subtable_3['Latest year compared with Mar 19'] = subtable_3.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
 
##################################################################################
#PUTTING TABLES TOGETHER
##################################################################################

vehicle_damage_recovery_table = pd.concat([
        subtable_1,
        subtable_1_base,
        subtable_2,
        subtable_3,
        subtable_2_base
        ], 
        axis = 0)
vehicle_damage_recovery_table.reset_index(inplace = True)
vehicle_damage_recovery_table = vehicle_damage_recovery_table.drop(['index'], axis = 1)  

##################################################################################
#FILLING IN MISSING DATA
##################################################################################
vehicle_damage_recovery_table.fillna(0, inplace = True)

vehicle_damage_recovery_table.replace(np.inf, np.nan, inplace = True)

vehicle_damage_recovery_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_damage_recovery_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE BASED ON EXISTING INDEX
##################################################################################

vehicle_damage_recovery_table_order = [1,0,2,6,5,4,3,7]
vehicle_damage_recovery_table = vehicle_damage_recovery_table.reindex(vehicle_damage_recovery_table_order)      

vehicle_damage_recovery_table.reset_index(inplace = True)
vehicle_damage_recovery_table_4 = vehicle_damage_recovery_table.drop(['index'], axis = 1) 
