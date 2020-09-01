# -*- coding: utf-8 -*-

import gptables as gpt

from pipeline.criminal_damage.damage.table_3a_type_of_damage import criminal_damage_type_of_damage_table_3a
from pipeline.criminal_damage.damage.table_3b_type_of_damage import criminal_damage_type_of_damage_table_3b

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#TYPE OF DAMAGE TABLE
#########################################################################################################################################

criminal_damage_type_of_damage_table_3a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_type_of_damage_gptable_3a = gpt.GPTable(
        table = criminal_damage_type_of_damage_table_3a,
        index_columns = {2: 0},
        title = "Table 3a: Type of damage caused in incidents of criminal damage to a vehicle, year ending March 2010 to year ending March 2018 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )

#########################################################################################################################################
#ARSON AND OTHER CRIMINAL DAMAGE.
#########################################################################################################################################
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_type_of_damage_table_3b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

criminal_damage_type_of_damage_gptable_3b = gpt.GPTable(
        table = criminal_damage_type_of_damage_table_3b,
        index_columns = {2: 0},
        title = "Table 3b: Type of damage caused in incidents of arson and other criminal damage, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )
