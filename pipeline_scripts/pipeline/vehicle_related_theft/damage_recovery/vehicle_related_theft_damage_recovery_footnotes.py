# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.damage_recovery.table_4_damage_recovery import vehicle_damage_recovery_table_4
from pipeline.additional_formatting import formatting

##################################################################################
#Table 4
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_damage_recovery_table_4.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)
    
vehicle_damage_recovery_table_4.reset_index(inplace = True)

vehicle_damage_recovery_table_4 = vehicle_damage_recovery_table_4.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_damage_recovery_table_4_gptable = gpt.GPTable(
        table = vehicle_damage_recovery_table_4,
        index_columns = {2: 0},
        title = "Table 4: Stolen vehicles returned to owners - rates of return and damage, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "For survey years ending March 2014 through to March 2020 estimates are based on fewer than 50 respondents and should be interpreted with caution.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )
