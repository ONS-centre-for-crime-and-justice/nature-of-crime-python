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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 81,82)
criminal_damage_offences = correct_area[
        (correct_area['offence'] == 81) |
        (correct_area['offence'] == 82)]



##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_data = criminal_damage_offences[(criminal_damage_offences['newloc1d'] == 1) |
                                 (criminal_damage_offences['newloc1d'] == 2) |
                                 (criminal_damage_offences['newloc1d'] == 3) |
                                 (criminal_damage_offences['newloc1d'] == 4) |
                                 (criminal_damage_offences['newloc1d'] == 5) |
                                 (criminal_damage_offences['newloc1d'] == 6) |
                                 (criminal_damage_offences['newloc1d'] == 7) |
                                 (criminal_damage_offences['newloc1d'] == 8) |
                                 (criminal_damage_offences['newloc1d'] == 9) ]

subtable_1 = ct.table.percentages_nonbinary(criminal_damage_offences, 'financial_year', 'newloc1d', 'c11weighti', 'total_c11weighti',lookup_dict)

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

criminal_damage_location_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)
criminal_damage_location_table.reset_index(inplace = True)

criminal_damage_location_table = criminal_damage_location_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

criminal_damage_location_table.fillna(0, inplace = True)

criminal_damage_location_table.replace(np.inf, np.nan, inplace = True)

criminal_damage_location_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = criminal_damage_location_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])


##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

criminal_damage_location_table_order = [0,1,2,6,7,3,4,5,8]

criminal_damage_location_table_2 = criminal_damage_location_table.reindex(criminal_damage_location_table_order)

