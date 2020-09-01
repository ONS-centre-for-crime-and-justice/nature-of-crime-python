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

vf_data = pd.read_csv(r"G:\Crime RAP project\Python development script\pipeline\criminal_damage\criminal_damage_data.csv")

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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 80,81,82,83,84,85,86)
criminal_damage_offences = correct_area[
        (correct_area['offence'] == 80) |
        (correct_area['offence'] == 81) |
        (correct_area['offence'] == 82) |
        (correct_area['offence'] == 83) |
        (correct_area['offence'] == 84) |
        (correct_area['offence'] == 85) |
        (correct_area['offence'] == 86)]



criminal_damage_offences['validoff'] = 0

remove_dks = ct.recode.recode_conditionally(
        criminal_damage_offences,
        target = "validoff",
        condition = [
                {'damveh_DK': 1},
                {'damveh_ref': 1},
                ],
        when = "any",
        value = 1
        )

criminal_damage_offences = remove_dks[(remove_dks['validoff'] == 0)]

criminal_damage_offences = criminal_damage_offences[
        (criminal_damage_offences['damveh_window'] == 0) | 
        (criminal_damage_offences['damveh_window'] == 1)
        ]

criminal_damage_offences = criminal_damage_offences[(criminal_damage_offences['VanHomVe'] == 2)]

##################################################################################
#IDENTIFYING THE VARIABLES NEEDED FOR THIS TABLE IN A LIST
##################################################################################

table_variables = ['damveh_window',
                  'damveh_windscreen',
                  'damveh_lock',
                  'damveh_bodywork',
                  'damveh_slash',
                  'damveh_deflate',
                  'damveh_wingmirror',
                  'damveh_scratch',
                  'damveh_fire',
                  'damveh_catalytic',
                  'damveh_other',
                  ]

##################################################################################
#CREATING A DATAFRAME SPECIFICALLY FOR SUBTABLE_2
##################################################################################

#ONLY KEEPING THE VARIABLES WE NEED FOR THE TABLE
subtable_1 = ct.table.apply_percentages_binary(criminal_damage_offences,'financial_year',table_variables,'c11weighti','Total_C11weighti', lookup_dict)

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE
##################################################################################

subtable_1_base = criminal_damage_offences.groupby(['financial_year']).sum()
subtable_1_base.reset_index(inplace = True)

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

criminal_damage_type_of_damage_table_3a = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)
criminal_damage_type_of_damage_table_3a .reset_index(inplace = True)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

criminal_damage_type_of_damage_table_3a.fillna(0, inplace = True)

criminal_damage_type_of_damage_table_3a.replace(np.inf, np.nan, inplace = True)

criminal_damage_type_of_damage_table_3a[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = criminal_damage_type_of_damage_table_3a[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#CREATING THE FINAL TABLE
##################################################################################

criminal_damage_type_of_damage_table_3a = criminal_damage_type_of_damage_table_3a.drop(['index'], axis = 1) 
