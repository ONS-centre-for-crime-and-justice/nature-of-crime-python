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

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 55,56,)
household_theft_offences = correct_area[
        (correct_area['offence'] == 55) |
        (correct_area['offence'] == 56)]

household_theft_offences =household_theft_offences[(household_theft_offences['vftype'] == 1)]

##################################################################################
#CREATING SUBTABLES
##################################################################################

subtable_1_data = household_theft_offences[
        (household_theft_offences['totval2'] < 9)]

subtable_1 = ct.table.percentages_nonbinary(subtable_1_data, 'financial_year', 'totval2', 'c11weighti', 'total_c11weighti',lookup_dict)

subtable_1 = subtable_1.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')

subtable_1.reset_index(inplace = True)

##################################################################################
#CREATING BASES
##################################################################################

subtable_1_base = subtable_1_data.groupby(['financial_year']).sum() 
subtable_1_base.reset_index(inplace=True)
subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]
subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_1_base = subtable_1_base.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'unweighted_base')

subtable_1_base.reset_index(inplace = True)

##################################################################################
#GETTING RID OF DK/REF FROM TOTVALUE
##################################################################################

subtable_2_data = subtable_1_data[
        (subtable_1_data['totvalue'] < 99998) ]  

################################# MEAN ###############################################################

#weighting total value to calc weighted mean.
subtable_2_data['weighted_value'] = (
        (subtable_2_data['c11weighti'])*(subtable_2_data['totvalue'])
        ) 


subtable_2_MEAN = subtable_2_data.groupby(['financial_year']).sum()
subtable_2_MEAN.reset_index(inplace = True)

subtable_2_MEAN ['mean'] = ((subtable_2_MEAN['weighted_value'])/((subtable_2_MEAN['c11weighti'])))
subtable_2 = subtable_2_MEAN[['financial_year','mean']]


subtable_2 ['table_label'] = 'Mean cost'

subtable_2 = subtable_2.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'mean')

subtable_2.reset_index(inplace = True)


################################# MEDIAN ############################################################

data_10 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '09 to Mar '10") ] 
data_11 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '10 to Mar '11") ] 
data_12 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '11 to Mar '12") ] 
data_13 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '12 to Mar '13") ] 
data_14 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '13 to Mar '14") ] 
data_15 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '14 to Mar '15") ] 
data_16 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '15 to Mar '16") ] 
data_17 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '16 to Mar '17") ] 
data_18 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '17 to Mar '18") ] 
data_19 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '18 to Mar '19") ]
data_20 = subtable_2_data[(subtable_2_data['financial_year'] == "Apr '19 to Mar '20") ]

median_10 = ct.table.median_calculation(data_10, 'totvalue', 'c11weighti')
median_10 ['financial_year'] = "Apr '09 to Mar '10"

median_11 = ct.table.median_calculation(data_11, 'totvalue', 'c11weighti')
median_11 ['financial_year'] = "Apr '10 to Mar '11"

median_12 = ct.table.median_calculation(data_12, 'totvalue', 'c11weighti')
median_12 ['financial_year'] = "Apr '11 to Mar '12"

median_13 = ct.table.median_calculation(data_13, 'totvalue', 'c11weighti')
median_13 ['financial_year'] = "Apr '12 to Mar '13"

median_14 = ct.table.median_calculation(data_14, 'totvalue', 'c11weighti')
median_14 ['financial_year'] = "Apr '13 to Mar '14"

median_15 = ct.table.median_calculation(data_15, 'totvalue', 'c11weighti')
median_15 ['financial_year'] = "Apr '14 to Mar '15"

median_16 = ct.table.median_calculation(data_16, 'totvalue', 'c11weighti')
median_16 ['financial_year'] = "Apr '15 to Mar '16"

median_17 = ct.table.median_calculation(data_17, 'totvalue', 'c11weighti')
median_17 ['financial_year'] = "Apr '16 to Mar '17"

median_18 = ct.table.median_calculation(data_18, 'totvalue', 'c11weighti')
median_18 ['financial_year'] = "Apr '17 to Mar '18"

median_19 = ct.table.median_calculation(data_19, 'totvalue', 'c11weighti')
median_19 ['financial_year'] = "Apr '18 to Mar '19"

median_20 = ct.table.median_calculation(data_20, 'totvalue', 'c11weighti')
median_20 ['financial_year'] = "Apr '19 to Mar '20"

subtable_3 = pd.concat([
        median_10,
        median_11,
        median_12,
        median_13,
        median_14,
        median_15,
        median_16,
        median_17,
        median_18,
        median_19,
        median_20,
        ], axis = 0)
    
subtable_3 ['table_label'] = 'Median cost'

subtable_3 = subtable_3.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'median')

subtable_3.reset_index(inplace = True)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 10'] = ct.sig_testing.ten_year_sig_test_means(subtable_2, subtable_2_data, 'totvalue', subtable_1_base)



subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 19'] = ct.sig_testing.previous_year_sig_test_means(subtable_2, subtable_2_data, 'totvalue', subtable_1_base)



##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

household_theft_cost_table = pd.concat([
                                subtable_1,
                                subtable_2,
                                subtable_3,
                                subtable_1_base,
                                ], axis = 0)

household_theft_cost_table.reset_index(inplace=True)

household_theft_cost_table = household_theft_cost_table.drop(['index'], axis = 1)


##################################################################################
#FILLING IN MISSING DATA
#################################################################################

household_theft_cost_table.fillna(0, inplace = True)

household_theft_cost_table.replace(np.inf, np.nan, inplace = True)

household_theft_cost_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = household_theft_cost_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])





##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

household_theft_cost_table_order = [0,1,4,6,3,5,7,2,8,9,10]
household_theft_cost_table = household_theft_cost_table.reindex(household_theft_cost_table_order)

household_theft_cost_table.reset_index(inplace=True) 
household_theft_cost_table_3b = household_theft_cost_table.drop(['index'], axis = 1) 


