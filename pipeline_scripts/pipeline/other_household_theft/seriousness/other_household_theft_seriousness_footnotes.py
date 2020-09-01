# -*- coding: utf-8 -*-
import gptables as gpt


from pipeline.other_household_theft.seriousness.table_5a_seriousness import household_theft_seriousness_table_5a
from pipeline.other_household_theft.seriousness.table_5b_seriousness import household_theft_seriousness_table_5b
from pipeline.other_household_theft.seriousness.table_5c_seriousness import household_theft_seriousness_table_5c

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#SERIOUSNESS TABLE
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_seriousness_table_5a["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)

household_theft_seriousness_table_5a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_seriousness_table_5a_gptable = gpt.GPTable(
        table = household_theft_seriousness_table_5a,
        index_columns = {1: 0, 2: 1},
        title = "Table 5a: Perceived seriousness of incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW",
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

############################################################################################################
#HOUSEHOLD THEFT IN A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_seriousness_table_5b["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)

household_theft_seriousness_table_5b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_seriousness_table_5b_gptable = gpt.GPTable(
        table = household_theft_seriousness_table_5b,
        index_columns = {1: 0, 2: 1},
        title = "Table 5b: Perceived seriousness of incidents of other household theft in a dwelling, year ending March 2010 to year ending March 2020 CSEW",
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

############################################################################################################
#HOUSEHOLD THEFT OUTSIDE A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_seriousness_table_5c["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)

household_theft_seriousness_table_5c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_seriousness_table_5c_gptable = gpt.GPTable(
        table = household_theft_seriousness_table_5c,
        index_columns = {1: 0, 2: 1},
        title = "Table 5c: Perceived seriousness of incidents of other household theft outside the dwelling, year ending March 2010 to year ending March 2020 CSEW",
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

