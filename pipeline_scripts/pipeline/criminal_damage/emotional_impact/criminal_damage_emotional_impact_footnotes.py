# -*- coding: utf-8 -*-
import gptables as gpt


from pipeline.criminal_damage.emotional_impact.table_5a_emotional_impact import criminal_damage_emotional_impact_table_5a
from pipeline.criminal_damage.emotional_impact.table_5b_emotional_impact import criminal_damage_emotional_impact_table_5b
from pipeline.criminal_damage.emotional_impact.table_5c_emotional_impact import criminal_damage_emotional_impact_table_5c
from pipeline.additional_formatting import formatting

#########################################################################################################################################
#EMOTIONAL IMPACT TABLE
#########################################################################################################################################

criminal_damage_emotional_impact_table_5a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_emotional_impact_gptable_5a = gpt.GPTable(
        table = criminal_damage_emotional_impact_table_5a,
        index_columns = {1: 0, 2: 1},
        title = "Table 5a: Emotional impact of criminal damage, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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
#CRIMINAL DAMAGE TO A VEHICLE.
#########################################################################################################################################

criminal_damage_emotional_impact_table_5b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_emotional_impact_gptable_5b = gpt.GPTable(
        table = criminal_damage_emotional_impact_table_5b,
        index_columns = {1: 0, 2: 1},
        title = "Table 5b: Emotional impact of incidents of criminal damage to a vehicle, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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
#ARSON AND OTHER CRIMINAL DAMAGE.
#########################################################################################################################################

criminal_damage_emotional_impact_table_5c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_emotional_impact_gptable_5c = gpt.GPTable(
        table = criminal_damage_emotional_impact_table_5c,
        index_columns = {1: 0, 2: 1},
        title = "Table 5c: Emotional impact of incidents of arson and other criminal dmaage, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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
