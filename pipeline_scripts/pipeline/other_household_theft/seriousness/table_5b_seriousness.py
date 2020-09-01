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

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\other_household_theft\other_household_theft_data.csv')

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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 55,56,65)
household_theft_offences = correct_area[
        (correct_area['offence'] == 55) |
        (correct_area['offence'] == 56) ]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_1_data = household_theft_offences[
        (household_theft_offences['score2'] < 4)]

subtable_1 = ct.table.percentages_nonbinary(subtable_1_data, 'financial_year', 'score2', 'c11weighti', 'total_c11weighti',lookup_dict)

subtable_2_data = household_theft_offences[
        (household_theft_offences['crime'] < 4)]

subtable_2 = ct.table.percentages_nonbinary(subtable_2_data, 'financial_year', 'crime', 'c11weighti', 'total_c11weighti', lookup_dict)

##################################################################################
#CREATING BASES
##################################################################################

subtable_base = subtable_1_data.groupby(['financial_year']).sum() 
subtable_base.reset_index(inplace=True)
subtable_base = subtable_base[['financial_year','unweighted_base']]
subtable_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_2_base = subtable_2_data.groupby(['financial_year']).sum() 
subtable_2_base.reset_index(inplace=True)
subtable_2_base = subtable_2_base[['financial_year','unweighted_base']]
subtable_2_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
#GETTING RID OF DK/REF FROM SCORE1
##################################################################################

subtable_3_data = subtable_1_data[
        (subtable_1_data['score1'] < 99998) ]  

################################# MEAN ###############################################################

#weighting total value to calc weighted mean.
subtable_3_data['weighted_value'] = (
        (subtable_3_data['c11weighti'])*(subtable_3_data['score1'])
        ) 

subtable_3_MEAN = subtable_3_data.groupby(['financial_year']).sum()
subtable_3_MEAN.reset_index(inplace = True)

subtable_3_MEAN ['mean'] = ((subtable_3_MEAN['weighted_value'])/((subtable_3_MEAN['c11weighti'])))
subtable_3 = subtable_3_MEAN[['financial_year','mean']]


subtable_3 ['table_label'] = 'Mean rating'

subtable_3 = subtable_3.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'mean')

subtable_3.reset_index(inplace = True)

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1 = subtable_1.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_1.reset_index(inplace = True)

subtable_base = subtable_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_base.reset_index(inplace = True)

subtable_2 = subtable_2.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_2.reset_index(inplace = True)

subtable_2_base = subtable_2_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_2_base.reset_index(inplace = True)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_base , axis = 1) 
subtable_2['Latest year compared with Mar 10'] = subtable_2.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_3['Latest year compared with Mar 10'] = ct.sig_testing.ten_year_sig_test_means(subtable_3,subtable_3_data,'score1', subtable_base)  

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_base , axis = 1) 
subtable_2['Latest year compared with Mar 19'] = subtable_2.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_3['Latest year compared with Mar 19'] = ct.sig_testing.previous_year_sig_test_means(subtable_3,subtable_3_data,'score1', subtable_base) 
 
##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

household_theft_seriousness_table =pd.concat([
        subtable_2,
        subtable_2_base,
        subtable_1,
        subtable_3,
        subtable_base,
        ], axis = 0)

household_theft_seriousness_table.reset_index(inplace=True)

household_theft_seriousness_table = household_theft_seriousness_table.drop(['index'], axis = 1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################
household_theft_seriousness_table.fillna(0, inplace = True)

household_theft_seriousness_table.replace(np.inf, np.nan, inplace = True)

household_theft_seriousness_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = household_theft_seriousness_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

household_theft_seriousness_table_order = [0,2,1,3,4,6,5,7,8]
household_theft_seriousness_table = household_theft_seriousness_table.reindex(household_theft_seriousness_table_order)

household_theft_seriousness_table.reset_index(inplace=True)
household_theft_seriousness_table_5b = household_theft_seriousness_table.drop(['index'], axis = 1)

##################################################################################
#ADDING SUBTABLE TITLES
##################################################################################

household_theft_seriousness_table_5b.insert(loc=0, column='table_title', value=['' for i in range(household_theft_seriousness_table_5b.shape[0])])

household_theft_seriousness_table_5b.loc[0, 'table_title'] = 'Perception of incident'

household_theft_seriousness_table_5b.loc[4, 'table_title'] = 'Rated seriousness of crime'