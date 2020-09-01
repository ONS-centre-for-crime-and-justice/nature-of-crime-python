# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.emotional_impact.table_8a_emotional_impact import vehicle_emotional_impact_table_8a
from pipeline.vehicle_related_theft.emotional_impact.table_8b_emotional_impact import vehicle_emotional_impact_table_8b
from pipeline.vehicle_related_theft.emotional_impact.table_8c_emotional_impact import vehicle_emotional_impact_table_8c
from pipeline.vehicle_related_theft.emotional_impact.table_8d_emotional_impact import vehicle_emotional_impact_table_8d
from pipeline.additional_formatting import formatting

##################################################################################
#Table 8a
##################################################################################

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################
vehicle_emotional_impact_table_8a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_emotional_impact_table_8a_gptable = gpt.GPTable(
        table = vehicle_emotional_impact_table_8a,
        index_columns = {1: 0, 2: 1},
        title = "Table 8a: Emotional impact of incidents of all vehicle-related theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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
##################################################################################
#Table 8b
##################################################################################

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################
vehicle_emotional_impact_table_8b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_emotional_impact_table_8b_gptable = gpt.GPTable(
        table = vehicle_emotional_impact_table_8b,
        index_columns = {1: 0, 2: 1},
        title = "Table 8b: Emotional impact of incidents of theft of vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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

##################################################################################
#Table 8c
##################################################################################

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################
vehicle_emotional_impact_table_8c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_emotional_impact_table_8c_gptable = gpt.GPTable(
        table = vehicle_emotional_impact_table_8c,
        index_columns = {1: 0, 2: 1},
        title = "Table 8c: Emotional impact of incidents of theft from vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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

##################################################################################
#Table 8d
##################################################################################

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################
vehicle_emotional_impact_table_8d.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_emotional_impact_table_8d_gptable = gpt.GPTable(
        table = vehicle_emotional_impact_table_8d,
        index_columns = {1: 0, 2: 1},
        title = "Table 8d: Emotional impact of incidents of attempted theft of and from vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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