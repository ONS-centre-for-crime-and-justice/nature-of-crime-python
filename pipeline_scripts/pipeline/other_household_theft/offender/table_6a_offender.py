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
        (correct_area['offence'] == 56) |
        (correct_area['offence'] == 65)]

##################################################################################
#CREATING SUBTABLES
##################################################################################

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 1
##################################################################################

household_theft_offences =household_theft_offences[(household_theft_offences['seeany'] <3)]

subtable_1_base = household_theft_offences.groupby(['financial_year']).sum()

subtable_1_base.reset_index(inplace=True)

subtable_1_base = subtable_1_base [['financial_year', 'unweighted_base']]

subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'


##################################################################################
# Creating subtable 1  "able to say something about offender"
#################################################################################

subtable_1 = ct.table.percentages_binary(household_theft_offences,'financial_year', 'seeany','c11weighti', 'total_c11weighti',lookup_dict)

###################################################################################
#recoding for valid responses to numoff for subtable 2
##################################################################################

correct_offences_numoff = household_theft_offences[
        (household_theft_offences['numoff'] < 5) ]  

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 2
##################################################################################

subtable_2_base = correct_offences_numoff.groupby(['financial_year']).sum()

subtable_2_base.reset_index(inplace=True)

subtable_2_base = subtable_2_base [['financial_year','unweighted_base']]

subtable_2_base ['table_label'] = 'Unweighted base - number of incidents (victim was able to say something about offender)'

##################################################################################
# Creating subtable 2 " number of offenders"
#################################################################################

subtable_2 = ct.table.percentages_nonbinary(correct_offences_numoff,'financial_year','numoff','c11weighti', 'Total_c11weighti',lookup_dict)
 
###################################################################################
#Recoding for subtable 3
##################################################################################

correct_offences_sex = household_theft_offences[
        (household_theft_offences['ofsex'] < 4) ] 

subtable_3_base = correct_offences_sex.groupby(['financial_year']).sum()

subtable_3_base.reset_index(inplace=True)

subtable_3_base = subtable_3_base [['financial_year','unweighted_base']]

subtable_3_base ['table_label'] = 'Unweighted base - number of incidents'

##################################################################################
# Creating subtable 3  "sex of offender"
#################################################################################

subtable_3 = ct.table.percentages_nonbinary(correct_offences_sex,'financial_year','ofsex','c11weighti','Total_c11weighti',lookup_dict)

###############################################################################
 #Recodes for subtable 4 "age of offender"
###############################################################################

household_theft_offences['filtered_age'] = 0

# Recode to 0 when any condition is met
correct_offences_age = ct.recode.recode_conditionally(
       household_theft_offences,
        target = 'filtered_age',
        condition = [
                {"ageoff2": 8},
                {"ageoff2": 9},
                {"ageoff2f": 1},
                {"ageoff2g": 1}
                ],
        when = "any",
        value = 1
        )    
    

correct_offences_age1= correct_offences_age[(correct_offences_age['vftype'] == 1) ]

correct_offences_age1= correct_offences_age1 [(correct_offences_age['seeany'] == 1)]

correct_age= correct_offences_age1[(correct_offences_age1['filtered_age'] == 0)]

age_list = ['ageof12',
            'ageof1',
            'ageof2',
            'ageof3',
            'ageof4',
            'ageof5'
            ]

correct_age= correct_age[(correct_age['ageof12'] == 0) | (correct_age['ageof12'] == 1)]
correct_age= correct_age[(correct_age['ageof1'] == 0) | (correct_age['ageof1'] == 1)]
correct_age= correct_age[(correct_age['ageof2'] == 0) | (correct_age['ageof2'] == 1)]
correct_age= correct_age[(correct_age['ageof3'] == 0) | (correct_age['ageof3'] == 1)]
correct_age= correct_age[(correct_age['ageof4'] == 0) | (correct_age['ageof4'] == 1)]
correct_age= correct_age[(correct_age['ageof5'] == 0) | (correct_age['ageof5'] == 1)]

###################################################################################
#Creating subtable 4  using age function  "age of offender"
#######################################################################################

subtable_4 = ct.table.apply_percentages_binary(correct_age,'financial_year',age_list,'c11weighti','Total_c11weighti',lookup_dict)

###############################################################################
 #Recodes for subtable 5 "relationship of offender"
###############################################################################

#recoding for valid responses to relate.
correct_offences_relate = household_theft_offences[(household_theft_offences['seeany'] == 1) &
       ((household_theft_offences['relate'] == 1) |
        (household_theft_offences['relate'] == 2) |
        (household_theft_offences['relate'] == 3)) ]
        
##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 5
##################################################################################

subtable_5_base = correct_offences_relate.groupby(['financial_year']).sum()

subtable_5_base.reset_index(inplace=True)

subtable_5_base = subtable_5_base [['financial_year','unweighted_base']]

subtable_5_base ['table_label'] = 'Unweighted base - number of incidents (victim was able to say something about offender)'

##################################################################################
# Creating subtable 5  "relationship of offender"
#################################################################################

subtable_5 = ct.table.percentages_nonbinary(correct_offences_relate,'financial_year','relate','c11weighti','Total_c11weighti', lookup_dict)

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


subtable_2 = subtable_2.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_2.reset_index(inplace = True)

subtable_2_base = subtable_2_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_2_base.reset_index(inplace = True)


subtable_3 = subtable_3.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_3.reset_index(inplace = True)


subtable_4 = subtable_4.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_4.reset_index(inplace = True)



subtable_5 = subtable_5.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'percentage')
subtable_5.reset_index(inplace = True)

subtable_5_base = subtable_5_base.pivot(index = 'table_label',
                              columns = 'financial_year',
                              values = 'unweighted_base')
subtable_5_base.reset_index(inplace = True)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1['Latest year compared with Mar 10'] = subtable_1.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 10'] = subtable_2.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_3['Latest year compared with Mar 10'] = subtable_3.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_4['Latest year compared with Mar 10'] = subtable_4.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_5['Latest year compared with Mar 10'] = subtable_5.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_5_base , axis = 1) 

subtable_1['Latest year compared with Mar 19'] = subtable_1.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 19'] = subtable_2.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_3['Latest year compared with Mar 19'] = subtable_3.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_4['Latest year compared with Mar 19'] = subtable_4.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 
subtable_5['Latest year compared with Mar 19'] = subtable_5.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_5_base , axis = 1)

##################################################################################
# Creating final combined table
#################################################################################

household_theft_offender_table = pd.concat([
        subtable_1,
        subtable_1_base,
        subtable_2,
        subtable_3,
        subtable_4,
        subtable_2_base,
        subtable_5,
        subtable_5_base
        ], axis = 0)

household_theft_offender_table.reset_index(inplace = True)

household_theft_offender_table = household_theft_offender_table.drop(['index'],axis =1)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################
household_theft_offender_table.fillna(0, inplace = True)

household_theft_offender_table.replace(np.inf, np.nan, inplace = True)

household_theft_offender_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = household_theft_offender_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#SORT OUT THE ORDERING OF THE FINAL TABLE
##################################################################################

household_theft_offender_table_order = [0,1,3,5,4,2,8,7,6,14,13,9,10,11,12,15,18,16,17,19]

household_theft_offender_table_6a = household_theft_offender_table.reindex(household_theft_offender_table_order)

household_theft_offender_table_6a.reset_index(inplace = True)

household_theft_offender_table_6a = household_theft_offender_table_6a.drop(['index'], axis = 1) 

##################################################################################
#ADDING SUBTABLE TITLES
##################################################################################

household_theft_offender_table_6a.insert(loc=0, column='table_title', value=['' for i in range(household_theft_offender_table_6a.shape[0])])

household_theft_offender_table_6a.loc[2, 'table_title'] = 'Number of offenders'

household_theft_offender_table_6a.loc[6, 'table_title'] = 'Sex of offender(s)'

household_theft_offender_table_6a.loc[9, 'table_title'] = 'Age of offender(s)'

household_theft_offender_table_6a.loc[16, 'table_title'] = 'Relationship to victim'