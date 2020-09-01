# -*- coding: utf-8 -*-
import gptables as gpt


from pipeline.bicycle_theft.emotional_impact.table_4_emotional_impact import bicycle_emotional_impact_table_4
from pipeline.additional_formatting import formatting

#########################################################################################################################################
#EMOTIONAL IMPACT TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

bicycle_emotional_impact_table_4.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)


##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

bicycle_emotional_impact_gptable_4 = gpt.GPTable(
        table = bicycle_emotional_impact_table_4,
        index_columns = {1: 0, 2: 1},
        title = "Table 4: Emotional impact of incidents of bicycle theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
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
