# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.personal_other_theft.seriousness.table_6a_seriousness import personal_theft_seriousness_table_6a
from pipeline.personal_other_theft.seriousness.table_6b_seriousness import other_personal_theft_seriousness_table_6b

from pipeline.additional_formatting import formatting


#########################################################################################################################################
#SERIOUSNESS TABLE 6a
#########################################################################################################################################

personal_theft_seriousness_table_6a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

personal_theft_seriousness_table_6a["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$2$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

personal_theft_seriousness_gptable_6a = gpt.GPTable(
        table = personal_theft_seriousness_table_6a,
        index_columns = {1: 0, 2: 1},
        title = "Table 6a: Perceived seriousness of incidents of personal, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                },
        additional_formatting = formatting
        )

#########################################################################################################################################
#SERIOUSNESS TABLE 6b
#########################################################################################################################################

other_personal_theft_seriousness_table_6b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

other_personal_theft_seriousness_table_6b["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$2$$",
        }, inplace=True)


##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

other_personal_theft_seriousness_gptable_6b = gpt.GPTable(
        table = other_personal_theft_seriousness_table_6b,
        index_columns = {1: 0, 2: 1},
        title = "Table 6b: Perceived seriousness of incidents of other theft of personal property, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                },
        additional_formatting = formatting
        )
