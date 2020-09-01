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
#APPLYING ALL THE FIRST FILTERING FOR TABLES
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
##############################################################################

#SELECTING THE OFFENCES FOR THE TABLE (e.g select if offence = 60,61,62,63)
vehicle_offences = correct_area[
        (correct_area['offence'] == 60) | (correct_area['offence'] == 61) |
                (correct_area['offence'] == 62) | (correct_area['offence'] == 63)
        ]

vehicle_offences = vehicle_offences[vehicle_offences['vehtheft'] == 2]

vehicle_offences.reset_index(inplace = True)

##############################################################################
#REMOVING DK AND REFUSALS
##############################################################################
vehicle_offences['validoff'] = 0

remove_dks = ct.recode.recode_conditionally(
        vehicle_offences,
       target = "validoff",
      condition = [
            {"valid_item_stolen_NoC": 1},
           ],
              when = "any",
              value = 1
              )

##################################################################################
#APPLYING ADDITIONAL FILTERING FOR TABLES
##################################################################################

vehicle_offences = remove_dks[
        (remove_dks['vftype'] == 1) &
        (remove_dks['validoff'] == 1)]
                    

##################################################################################
#SUBTABLE 1
##################################################################################

##################################################################################
#IDENTIFYING THE VARIABLES NEEDED FOR THIS TABLE IN A LIST
##################################################################################

subtable_1_variables = ['valstol',
                        'electric',
                        'hifi',
                        'cartele',
                        'tools',
                        'bike',
                        'camera',
                        'hhitems',
                        'foodcigs',
                        'Hkeys',
                        'Ckeys',
                        'extfit',
                        'tyres',
                        'othervp',
                        'fuel',
                        'garden',
                        'glasses',
                        'cdtapedvd',
                        'otherst']

##################################################################################
#CREATING A DATAFRAME SPECIFICALLY FOR SUBTABLE_1
##################################################################################

#ONLY KEEPING THE VARIABLES WE NEED FOR THE TABLE

subtable_1_data = vehicle_offences[
        (vehicle_offences['valstol'] <2) ]
        
subtable_1_data= subtable_1_data[subtable_1_variables + ['financial_year', 'c11weighti','unweighted_base']]

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 1
##################################################################################

subtable_1_base = subtable_1_data.groupby(['financial_year']).sum()
subtable_1_base.reset_index(inplace = True)

subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]
subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
#CREATING SUBTABLE 1
##################################################################################

subtable_1 = ct.table.apply_percentages_binary(subtable_1_data,'financial_year',subtable_1_variables,'c11weighti','Total_C11weighti', lookup_dict)

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_base = subtable_1_base.pivot(index = 'table_label',
                                      columns = 'financial_year',
                              values = 'unweighted_base')
subtable_base.reset_index(inplace = True)

##################################################################################
#SORTING IN DESCENDING ORDER AND KEEPING OTHER SEPERATE
##################################################################################

condition = (subtable_1.table_label=='Other (non-vehicle parts)')
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

items_stolen_table_6 = pd.concat([
        subtable_1,
        subtable_base,
        ], axis = 0)
items_stolen_table_6.reset_index(inplace = True)

vehicle_items_stolen_table_6 = items_stolen_table_6.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

vehicle_items_stolen_table_6.fillna(0, inplace = True)

vehicle_items_stolen_table_6.replace(np.inf, np.nan, inplace = True)

vehicle_items_stolen_table_6[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = vehicle_items_stolen_table_6[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

