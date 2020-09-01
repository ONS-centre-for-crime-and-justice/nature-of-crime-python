# -*- coding: utf-8 -*-
import pandas as pd
import crimetables as ct
import numpy as np
##################################################################################
#reading in data
###################################################################################

vf_data = pd.read_csv(r'G:\Crime RAP project\Python development script\pipeline\personal_other_theft\personal_other_theft_data.csv')

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

################################################################################################################################################################
#OTHER PERSONAL THEFT TABLES
################################################################################################################################################################

#SELECTING THE OFFENCES FOR THE TABLE (select if offence = 67,73)
other_personal_theft_offences = correct_area[
        (correct_area['offence'] == 67) |
        (correct_area['offence'] == 73)]

other_personal_theft_offences['validoff'] = 0

remove_dks = ct.recode.recode_conditionally(
        other_personal_theft_offences,
        target = "validoff",
        condition = [
                {"whemotk": 1},
                {"whemotl": 1},
                ],
        when = "any",
        value = 1
        )

removing_dks = remove_dks[(remove_dks['validoff'] == 0)]

#QUESTION ONLY ASKED ON THE LONG VF SO NEED TO PICK THOSE CASES
correct_vf_type= removing_dks[(removing_dks['vftype'] == 1)]

correct_vf = correct_vf_type[(correct_vf_type['respreac'] == 1) | 
        (correct_vf_type['respreac'] == 0)]

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 1
##################################################################################

subtable_1_base = correct_vf.groupby(['financial_year']).sum()
subtable_1_base.reset_index(inplace= True)

subtable_1_base = subtable_1_base[['financial_year','unweighted_base']]

##################################################################################
#CREATING DATAFRAME TO USE FOR SUBTABLE1
##################################################################################

#ONLY KEEPING THE VARIABLES WE NEED FOR THE TABLE
subtable_1_data= correct_vf[['financial_year','respreac','totaff','c11weighti']]


##################################################################################
#CREATING SUBTABLE_1A
##################################################################################

subtable_1a = ct.table.percentages_nonbinary(subtable_1_data,'financial_year', 'respreac', 'c11weighti', 'Total_C11weighti',lookup_dict)

##################################################################################
#CREATING SUBTABLE_1b
##################################################################################

subtable_1b_data = subtable_1_data[(subtable_1_data['totaff'] == 1) | 
        (subtable_1_data['totaff'] == 2) | 
        (subtable_1_data['totaff'] == 3) | 
        (subtable_1_data['totaff'] == 4)]

subtable_1b = ct.table.percentages_nonbinary(subtable_1b_data,'financial_year', 'totaff', 'c11weighti', 'Total_C11weighti',lookup_dict)

##################################################################################
#SUBTABLE 2 
##################################################################################

##################################################################################
#IDENTIFYING THE VARIABLES NEEDED FOR THIS TABLE IN A LIST
##################################################################################

subtable_2_variables = ['anger',
                        'shock',
                        'fear',
                        'sleeping',
                        'crying',
                        'depress',
                        'anxiety',
                        'confid',
                        'annoy',
                        'othemot']

##################################################################################
#CREATING A DATAFRAME SPECIFICALLY FOR SUBTABLE_2
##################################################################################

#ONLY KEEPING THE VARIABLES WE NEED FOR THE TABLE
subtable_2_data= correct_vf[subtable_2_variables + ['financial_year', 'c11weighti','respreac','unweighted_base']]

##################################################################################
#APPLYING ADDITIONAL FILTERING NEEDED FOR SUBTABLE_2
##################################################################################

subtable_2_data = subtable_2_data[(subtable_2_data['respreac'] == 1)]

##################################################################################
#CREATING UNWEIGHTED BASES FOR SUBTABLE 2
##################################################################################

subtable_2_base = subtable_2_data.groupby(['financial_year']).sum()
subtable_2_base.reset_index(inplace = True)

subtable_2_base = subtable_2_base[['financial_year','unweighted_base']]

##################################################################################
#CREATING SUBTABLE 2
##################################################################################

subtable_2 = ct.table.apply_percentages_binary(subtable_2_data,'financial_year',subtable_2_variables,'c11weighti','Total_C11weighti',lookup_dict)

##################################################################################
#RE-ARRANGING DATAFRAMES SO THEY HAVE YEARS AS COLUMNS 
##################################################################################

subtable_1a = subtable_1a.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_1a.reset_index(inplace = True)


subtable_1b = subtable_1b.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_1b.reset_index(inplace = True)

subtable_1b.drop(index = 1, inplace = True)

subtable_2 = subtable_2.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'percentage')
subtable_2.reset_index(inplace = True)

subtable_1_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_1_base = subtable_1_base.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'unweighted_base')
subtable_1_base.reset_index(inplace = True)


subtable_2_base ['table_label'] = 'Unweighted base - number of incidents'

subtable_2_base = subtable_2_base.pivot(index = 'table_label',
                                columns = 'financial_year',
                                values = 'unweighted_base')
subtable_2_base.reset_index(inplace = True)

##################################################################################
#SORTING IN DESCENDING ORDER AND KEEPING OTHER SEPERATE
##################################################################################

subtable_1 = pd.concat([
        subtable_1a,
        subtable_1b
        ], axis = 0)
subtable_1.reset_index(inplace = True)
subtable_1 = subtable_1.drop(['index'], axis = 1)  

subtable_1_order = [0,4,3,2,1]

subtable_1 = subtable_1.reindex(subtable_1_order)  

condition = (subtable_2.table_label=='Other')
other = subtable_2[condition]
groups = subtable_2[~condition]

subtable_2 = groups.sort_values(groups.columns[-1], ascending=False)

subtable_2 = pd.concat([
        subtable_2,
        other,
        ], axis = 0)

##################################################################################
#ADDING SIG TESTING TO ALL SUBTABLES
##################################################################################

subtable_1a['Latest year compared with Mar 10'] = subtable_1a.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_1b['Latest year compared with Mar 10'] = subtable_1b.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 10'] = subtable_2.apply(ct.sig_testing.ten_year_sig_test, bases = subtable_2_base , axis = 1) 

subtable_1a['Latest year compared with Mar 19'] = subtable_1a.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_1b['Latest year compared with Mar 19'] = subtable_1b.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_1_base , axis = 1) 
subtable_2['Latest year compared with Mar 19'] = subtable_2.apply(ct.sig_testing.previous_year_sig_test, bases = subtable_2_base , axis = 1) 

##################################################################################
#COMBINING THE FINAL TABLE
##################################################################################

emotional_impact_table = pd.concat([
        subtable_1a,
        subtable_1b,
        subtable_1_base,
        subtable_2,
        subtable_2_base
        ], axis = 0)
emotional_impact_table.reset_index(inplace = True)

##################################################################################
#FILLING IN MISSING DATA
#################################################################################

emotional_impact_table.fillna(0, inplace = True)

emotional_impact_table.replace(np.inf, np.nan, inplace = True)

emotional_impact_table[[
        'Latest year compared with Mar 10',
        'Latest year compared with Mar 19']] = emotional_impact_table[[
                'Latest year compared with Mar 10',
                'Latest year compared with Mar 19']].replace ([0], [''])

##################################################################################
#CREATING THE FINAL TABLE
##################################################################################

other_personal_theft_emotional_impact_table_5b = emotional_impact_table.drop(['index'], axis = 1) 

##################################################################################
#ADDING SUBTABLE TITLES
##################################################################################

other_personal_theft_emotional_impact_table_5b.insert(loc=0, column='table_title', value=['' for i in range(other_personal_theft_emotional_impact_table_5b.shape[0])])

other_personal_theft_emotional_impact_table_5b.loc[0, 'table_title'] = 'Extent of impact'

other_personal_theft_emotional_impact_table_5b.loc[6, 'table_title'] = 'Type of emotional response experienced'
