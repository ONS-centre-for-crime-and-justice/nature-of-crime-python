# -*- coding: utf-8 -*-
##################################################################################
#READING IN ALL NECESSARY PACKAGES
##################################################################################

import pandas as pd
import crimetables as ct
import numpy as np
##################################################################################
#reading in data
###################################################################################

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\personal_other_theft\personal_other_theft_data.csv')

################################################################################################################################################################
#OTHER PERSONAL THEFT TABLES
################################################################################################################################################################

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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 67,73)
other_personal_theft_offences = correct_area[
        (correct_area['offence'] == 67) |
        (correct_area['offence'] == 73)]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_data = other_personal_theft_offences[(other_personal_theft_offences['newloc1c'] == 1) |
                                 (other_personal_theft_offences['newloc1c'] == 2) |
                                 (other_personal_theft_offences['newloc1c'] == 3) |
                                 (other_personal_theft_offences['newloc1c'] == 4) |
                                 (other_personal_theft_offences['newloc1c'] == 5) |
                                 (other_personal_theft_offences['newloc1c'] == 6) |
                                 (other_personal_theft_offences['newloc1c'] == 7) |
                                 (other_personal_theft_offences['newloc1c'] == 8) |
                                 (other_personal_theft_offences['newloc1c'] == 9) ]

subtable_1 = ct.table.percentages_nonbinary(other_personal_theft_offences, 'financial_year', 'newloc1c', 'c11weighti', 'total_c11weighti',lookup_dict)

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

#Can't sig test this year due to changes in the questionnaire.
subtable_1['Latest year compared with Mar 10'] = ":" 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 

##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

other_personal_theft_location_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)
other_personal_theft_location_table.reset_index(inplace = True)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

other_personal_theft_location_table.fillna(0, inplace = True)

other_personal_theft_location_table.replace(np.inf, np.nan, inplace = True)

other_personal_theft_location_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = other_personal_theft_location_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#CREATING THE FINAL TABLE
##################################################################################

other_personal_theft_location_table_2b = other_personal_theft_location_table.drop(['index'], axis = 1)
