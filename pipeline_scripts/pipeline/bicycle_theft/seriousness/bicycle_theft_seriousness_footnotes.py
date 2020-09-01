# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

from pipeline.bicycle_theft.seriousness.table_5_seriousness import bicycle_seriousness_table_5
from pipeline.additional_formatting import formatting

#########################################################################################################################################
#Seriousness TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

bicycle_seriousness_table_5.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

bicycle_seriousness_table_5["table_title"].replace({
        "Rated seriousness of crime": "Rated seriousness of crime$$1$$",
        }, inplace=True)


##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

bicycle_seriousness_gptable_5 = gpt.GPTable(
        table = bicycle_seriousness_table_5,
        index_columns = {1: 0, 2: 1},
        title = "Table 5: Perceived seriousness of incidents of bicycle theft, year ending March 2010 to year ending March 2020 CSEW",
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
