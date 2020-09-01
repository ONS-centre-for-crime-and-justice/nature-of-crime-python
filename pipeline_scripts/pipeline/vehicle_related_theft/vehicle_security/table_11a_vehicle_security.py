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
remove_unweighted_cases =  ct.filters.filter_with_weight(
        vf_data,
        "c11weighti"
        )
#FILTERING CASES THAT HAPPENED IN ENGLAND AND WALES
correct_area= remove_unweighted_cases[(remove_unweighted_cases['victarea'] == 1) | 
        (remove_unweighted_cases['wherhapp'] == 1)]

##############################################################################
#SELECTING THE OFFENCES FOR THE TABLE 
###############################################################################

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 60,61,62,63,71,72)
vehicle_offences = correct_area[
        ((correct_area['offence'] == 60) | (correct_area['offence'] == 61) |
               (correct_area['offence'] == 71) )
        ]
subtable_1_data = vehicle_offences[
       (vehicle_offences['vftype'] == 1)]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_1_data = subtable_1_data[
       (subtable_1_data['vehtheft'] == 1) | (subtable_1_data['vehtheft'] == 2)
      | (subtable_1_data['vehtheft'] == 3)]


##################################################################################
#CREATING SUBTABLE 1
##################################################################################


subtable_1_base_data = subtable_1_data[(subtable_1_data['vcentlo'] < 3)]

subtable_1_data = subtable_1_data[(subtable_1_data['vcentlo'] < 3) |
                                 (subtable_1_data['vcarala'] < 3) |
                                 (subtable_1_data['vimmobm'] < 3) |
                                 (subtable_1_data['vimmobe'] < 3) |
                                 (subtable_1_data['vanyimob'] < 3) |
                                 (subtable_1_data['vvtrack'] < 3) 
                                 ]

subtable_1_variables = ['vcentlo',
                        'vcarala',
                        'vimmobm',
                        'vimmobe',
                        'vanyimob',
                        'vvtrack'
                        ]

##################################################################################
#CREATING SUBTABLE_1
##################################################################################

subtable_1 = ct.table.apply_percentages_binary(subtable_1_data,'financial_year',subtable_1_variables,'c11weighti','total_c11weighti', lookup_dict)

subtable_1_base = subtable_1_base_data.groupby(['financial_year']).sum() 
subtable_1_base.reset_index(inplace=True)
subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]

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

#################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
 
subtable_1.fillna(0, inplace = True)

subtable_1.replace(np.inf, np.nan, inplace = True)

##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

vehicle_security_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)

vehicle_security_table.reset_index(inplace=True)

vehicle_security_table = vehicle_security_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################
vehicle_security_table.fillna(0, inplace = True)

vehicle_security_table.replace(np.inf, np.nan, inplace = True)

vehicle_security_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_security_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

vehicle_security_table_order = [2,0,3,4,1,5,6]
vehicle_security_table_11a = vehicle_security_table.reindex(vehicle_security_table_order)
