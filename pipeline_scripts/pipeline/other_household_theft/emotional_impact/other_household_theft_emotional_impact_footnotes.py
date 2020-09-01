# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.other_household_theft.emotional_impact.table_4a_emotional_impact import household_theft_emotional_impact_table_4a
from pipeline.other_household_theft.emotional_impact.table_4b_emotional_impact import household_theft_emotional_impact_table_4b
from pipeline.other_household_theft.emotional_impact.table_4c_emotional_impact import household_theft_emotional_impact_table_4c

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#EMOTIONAL IMPACT TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_emotional_impact_table_4a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_emotional_impact_table_4a_gptable = gpt.GPTable(
        table = household_theft_emotional_impact_table_4a,
        index_columns = {1: 0, 2: 1},
        title = "Table 4a: Emotional impact of incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures here are based on incidents in which the victim reported that they were emotionally affected by the incident.",
                "2": "Figures may not sum to 100 as more than one response possible.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )


############################################################################################################
#HOUSEHOLD THEFT DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_emotional_impact_table_4b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_emotional_impact_table_4b_gptable = gpt.GPTable(
        table = household_theft_emotional_impact_table_4b,
        index_columns = {1: 0, 2: 1},
        title = "Table 4b: Emotional impact of incidents of other household theft in the dwelling, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures here are based on incidents in which the victim reported that they were emotionally affected by the incident.",
                "2": "Figures may not sum to 100 as more than one response possible.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT OUTSIDE A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_emotional_impact_table_4c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_emotional_impact_table_4c_gptable = gpt.GPTable(
        table = household_theft_emotional_impact_table_4c,
        index_columns = {1: 0, 2: 1},
        title = "Table 4c: Emotional impact of incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures here are based on incidents in which the victim reported that they were emotionally affected by the incident.",
                "2": "Figures may not sum to 100 as more than one response possible.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )

