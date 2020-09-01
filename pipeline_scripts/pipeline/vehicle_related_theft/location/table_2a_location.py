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
#READING IN FILE FOR CREATION OF LABEL DICTIONARY - all vehicle related theft
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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 60,61,62,63,71,72)
vehicle_offences = correct_area[
        ((correct_area['offence'] == 60) | (correct_area['offence'] == 61) |
        (correct_area['offence'] == 62) | (correct_area['offence'] == 63) | 
        (correct_area['offence'] == 71) | (correct_area['offence'] == 72) )
        ]

vehicle_offences = vehicle_offences[
        (vehicle_offences['vehtheft'] == 1) | (vehicle_offences['vehtheft'] == 2)
        | (vehicle_offences['vehtheft'] == 3)]

vehicle_offences = vehicle_offences[(vehicle_offences['newloc1d'] < 9)]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_data = vehicle_offences[(vehicle_offences['newloc1d'] == 1) |
                                 (vehicle_offences['newloc1d'] == 2) |
                                 (vehicle_offences['newloc1d'] == 3) |
                                 (vehicle_offences['newloc1d'] == 4) |
                                 (vehicle_offences['newloc1d'] == 5) |
                                 (vehicle_offences['newloc1d'] == 6) |
                                 (vehicle_offences['newloc1d'] == 7) |
                                 (vehicle_offences['newloc1d'] == 8) ]

subtable_1 = ct.table.percentages_nonbinary(
        vehicle_offences, 'financial_year', 'newloc1d', 'c11weighti', 'total_c11weighti', lookup_dict)

##################################################################################
#CREATING BASES
##################################################################################
subtable_1_base = subtable_data.groupby(['financial_year']).sum() 
subtable_1_base.reset_index(inplace=True)
subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]
subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'

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
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

#Can't sig test this year due to changes in the questionnaire.
subtable_1['Latest year compared with Mar 10'] = ":"

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
 
##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

vehicle_location_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)
vehicle_location_table.reset_index(inplace = True)
vehicle_location_table = vehicle_location_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

vehicle_location_table.fillna(0, inplace = True)

vehicle_location_table.replace(np.inf, np.nan, inplace = True)

vehicle_location_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_location_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

vehicle_location_table_order = [0,1,2,6,7,3,4,5,8]
vehicle_location_table_2a = vehicle_location_table.reindex(vehicle_location_table_order)
