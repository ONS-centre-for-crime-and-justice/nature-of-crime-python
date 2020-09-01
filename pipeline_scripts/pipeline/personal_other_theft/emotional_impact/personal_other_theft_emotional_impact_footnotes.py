# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.personal_other_theft.emotional_impact.table_5a_emotional_impact import personal_theft_emotional_impact_table_5a
from pipeline.personal_other_theft.emotional_impact.table_5b_emotional_impact import other_personal_theft_emotional_impact_table_5b

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#EMOTIONAL IMPACT TABLE 5a
#########################################################################################################################################

personal_theft_emotional_impact_table_5a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

personal_theft_emotional_impact_gptable_5a = gpt.GPTable(
        table = personal_theft_emotional_impact_table_5a,
        index_columns = {1: 0, 2: 1},
        title = "Table 5a: Emotional impact of incidents of theft from the person, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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

#########################################################################################################################################
#EMOTIONAL IMPACT TABLE 5b
#########################################################################################################################################

other_personal_theft_emotional_impact_table_5b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

other_personal_theft_emotional_impact_gptable_5b = gpt.GPTable(
        table = other_personal_theft_emotional_impact_table_5b,
        index_columns = {1: 0, 2: 1},
        title = "Table 5b: Emotional impact of incidents of other theft of personal property, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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

