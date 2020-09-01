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

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\bicycle_theft\bicycle_theft_data.csv')

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

remove_unweighted_cases = ct.filters.filter_with_weight(
        vf_data,
        "c11weighti"
        )

correct_area= remove_unweighted_cases[(remove_unweighted_cases['victarea'] == 1) | 
        (remove_unweighted_cases['wherhapp'] == 1)]

##############################################################################
#SELECTING THE OFFENCES FOR THE TABLE 
###############################################################################

bicycle_offences = correct_area[
        (correct_area['offence'] == 64)]


##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_data = bicycle_offences[(bicycle_offences['newloc1e'] < 10)]

subtable_1 = ct.table.percentages_nonbinary(bicycle_offences, 'financial_year', 'newloc1e', 'c11weighti', 'total_c11weighti',lookup_dict)

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

bicycle_location_table = pd.concat([
        subtable_1,
        subtable_1_base,
        ], axis = 0)
bicycle_location_table.reset_index(inplace = True)

bicycle_location_table = bicycle_location_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
##################################################################################

#bicycle_location_table.fillna(0, inplace = True)

bicycle_location_table.replace(np.inf, np.nan, inplace = True)

bicycle_location_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = bicycle_location_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([np.nan], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

bicycle_location_table_order = [0,1,2,7,8,3,6,4,5,9]

bicycle_location_table_2 = bicycle_location_table.reindex(bicycle_location_table_order)
