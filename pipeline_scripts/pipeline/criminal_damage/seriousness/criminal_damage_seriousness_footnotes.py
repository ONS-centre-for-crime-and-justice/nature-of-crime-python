# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

from pipeline.criminal_damage.seriousness.table_6a_seriousness import criminal_damage_seriousness_table_6a
from pipeline.criminal_damage.seriousness.table_6b_seriousness import criminal_damage_seriousness_table_6b
from pipeline.criminal_damage.seriousness.table_6c_seriousness import criminal_damage_seriousness_table_6c
from pipeline.additional_formatting import formatting

#########################################################################################################################################
#Seriousness TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_seriousness_table_6a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

criminal_damage_seriousness_table_6a["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_seriousness_gptable_6a = gpt.GPTable(
        table = criminal_damage_seriousness_table_6a,
        index_columns = {1: 0, 2: 1},
        title = "Table 6a: Perceived seriousness of incidents of criminal damage, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )

#########################################################################################################################################
#CRIMINAL DAMAGE TO A VEHICLE.
#########################################################################################################################################

criminal_damage_seriousness_table_6b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

criminal_damage_seriousness_table_6b["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)


##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_seriousness_gptable_6b = gpt.GPTable(
        table = criminal_damage_seriousness_table_6b,
        index_columns = {1: 0, 2: 1},
        title = "Table 6b: Perceived seriousness of incidents of criminal damage to a vehicle, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )

#########################################################################################################################################
#ARSON AND OTHER CRIMINAL DAMAGE.
#########################################################################################################################################

criminal_damage_seriousness_table_6c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

criminal_damage_seriousness_table_6c["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_seriousness_gptable_6c = gpt.GPTable(
        table = criminal_damage_seriousness_table_6c,
        index_columns = {1: 0, 2: 1},
        title = "Table 6c: Perceived seriousness of incidents of arson and other criminal damage, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )
