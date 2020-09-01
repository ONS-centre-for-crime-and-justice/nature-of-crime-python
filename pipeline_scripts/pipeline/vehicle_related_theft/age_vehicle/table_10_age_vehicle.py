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
#SELECTING THE OFFENCES FOR THE TABLE 
###############################################################################

#SELECTING THE OFFENCES FOR THE TABLE (e.g select if offence = 60,61,62,63,71,72)
vehicle_offences = correct_area[
        ((correct_area['offence'] == 60) | (correct_area['offence'] == 62))
        ]

vehicle_offences =vehicle_offences[(vehicle_offences['vftype'] == 1)]

vehicle_offences = vehicle_offences[
        ((vehicle_offences['vehage'] == 1)|
        (vehicle_offences['vehage'] == 2)|
        (vehicle_offences['vehage'] == 3)|
        (vehicle_offences['vehage'] == 4))]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_1_data = ct.table.percentages_nonbinary(vehicle_offences,'financial_year', 'vehage', 'c11weighti', 'Total_C11weighti', lookup_dict)

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 2
##################################################################################

subtable_1_base = vehicle_offences.groupby(['financial_year']).sum()
subtable_1_base.reset_index(inplace = True)

subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1_data.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_1_base = subtable_1_base.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'unweighted_base')
subtable_1_base.reset_index(inplace = True)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
 
subtable_1.fillna(0, inplace = True)

subtable_1.replace(np.inf, np.nan, inplace = True)

##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

vehicle_age_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], 
        axis = 0)
vehicle_age_table.reset_index(inplace = True)
vehicle_age_table = vehicle_age_table.drop(['index'], axis = 1)  


##################################################################################
#FILLING IN MISSING DATA
#################################################################################
vehicle_age_table.fillna(0, inplace = True)

vehicle_age_table.replace(np.inf, np.nan, inplace = True)

vehicle_age_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_age_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE BASED ON EXISTING INDEX
##################################################################################
vehicle_age_table_order = [0,2,1,3,4]
vehicle_age_table = vehicle_age_table.reindex(vehicle_age_table_order)      

vehicle_age_table.reset_index(inplace = True)
vehicle_age_table_10 = vehicle_age_table.drop(['index'], axis = 1) 
