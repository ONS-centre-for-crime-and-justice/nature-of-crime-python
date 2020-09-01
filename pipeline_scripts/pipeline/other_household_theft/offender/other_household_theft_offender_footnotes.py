# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.other_household_theft.offender.table_6a_offender import household_theft_offender_table_6a
from pipeline.other_household_theft.offender.table_6b_offender import household_theft_offender_table_6b
from pipeline.other_household_theft.offender.table_6c_offender import household_theft_offender_table_6c

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#Offender TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_offender_table_6a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$4$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$4$$"
         }, inplace=True)

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_offender_table_6a["table_title"].replace({
         "Age of offender(s)":"Age of offender(s)$$6$$",
         "Relationship to victim": "Relationtship to victim$$7$$",
          }, inplace=True)

household_theft_offender_table_6a["table_label"].replace({
         "Unweighted base - number of incidents (victim was able to say something about offender)":"Unweighted base - number of incidents (victim was able to say something about offender)$$5$$",
          }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_offender_table_6a_gptable = gpt.GPTable(
        table = household_theft_offender_table_6a,
        index_columns = {1: 0, 2: 1},
        title = "Table 6a: Offender characteristics in incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$$$3$$",
       subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                 "1": "Figures here are based on incidents in which the victim could say something about the offender(s).",
                "2": "The offender-victim relationship is classified as: 'strangers' if the victim did not have any information about the offender(s), or did not know and had never seen the offender(s) before; 'known by sight or to speak to' if at least one offender falls into either category; and 'known well' if at least one offender falls into this category (for multiple offenders this takes priority over any less well-known offenders).",
                "3": "All respondents were asked about their relationship to the offender(s) - this includes detailed questions of victims who experienced three or less offences and brief questions to those who experienced more than three but less than six offences in the last year. ",
                "4": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "5": "Unweighted base given for sex and age of offender is for the question asking about number of offenders; other bases are similar.",
                "6": "Figures may not sum to 100 as more than one response possible.",
                "7":  "All respondents were asked about their relationship to the offender(s) - this includes detailed questions of victims who experienced three or less offences and brief questions to those who experienced more than three but less than six offences in the last year.", 
                },
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT IN A DWELLING
############################################################################################################

household_theft_offender_table_6b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$4$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$4$$"
         }, inplace=True)

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_offender_table_6b["table_title"].replace({
         "Age of offender(s)":"Age of offender(s)$$6$$",
         "Relationship to victim": "Relationtship to victim$$7$$",
          }, inplace=True)

household_theft_offender_table_6b["table_label"].replace({
         "Unweighted base - number of incidents (victim was able to say something about offender)":"Unweighted base - number of incidents (victim was able to say something about offender)$$5$$",
          }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_offender_table_6b_gptable = gpt.GPTable(
        table = household_theft_offender_table_6b,
        index_columns = {1: 0, 2: 1},
        title = "Table 6b: Offender characteristics in incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$$$3$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                 "1": "Figures here are based on incidents in which the victim could say something about the offender(s).",
                "2": "The offender-victim relationship is classified as: 'strangers' if the victim did not have any information about the offender(s), or did not know and had never seen the offender(s) before; 'known by sight or to speak to' if at least one offender falls into either category; and 'known well' if at least one offender falls into this category (for multiple offenders this takes priority over any less well-known offenders).",
                "3": "All respondents were asked about their relationship to the offender(s) - this includes detailed questions of victims who experienced three or less offences and brief questions to those who experienced more than three but less than six offences in the last year. ",
                "4": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "5": "Unweighted base given for sex and age of offender is for the question asking about number of offenders; other bases are similar.",
                "6": "Figures may not sum to 100 as more than one response possible.",
                "7":  "All respondents were asked about their relationship to the offender(s) - this includes detailed questions of victims who experienced three or less offences and brief questions to those who experienced more than three but less than six offences in the last year.", 
                },
        additional_formatting = formatting
        )


############################################################################################################
#HOUSEHOLD THEFT OUTSIDE A DWELLING
############################################################################################################

household_theft_offender_table_6c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$4$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$4$$"
         }, inplace=True)

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_offender_table_6c["table_title"].replace({
         "Age of offender(s)":"Age of offender(s)$$6$$",
         "Relationship to victim": "Relationtship to victim$$7$$",
          }, inplace=True)

household_theft_offender_table_6c["table_label"].replace({
         "Unweighted base - number of incidents (victim was able to say something about offender)":"Unweighted base - number of incidents (victim was able to say something about offender)$$5$$",
          }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_offender_table_6c_gptable = gpt.GPTable(
        table = household_theft_offender_table_6c,
        index_columns = {1: 0, 2: 1},
        title = "Table 6a: Offender characteristics in incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$$$3$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures here are based on incidents in which the victim could say something about the offender(s).",
                "2": "The offender-victim relationship is classified as: 'strangers' if the victim did not have any information about the offender(s), or did not know and had never seen the offender(s) before; 'known by sight or to speak to' if at least one offender falls into either category; and 'known well' if at least one offender falls into this category (for multiple offenders this takes priority over any less well-known offenders).",
                "3": "All respondents were asked about their relationship to the offender(s) - this includes detailed questions of victims who experienced three or less offences and brief questions to those who experienced more than three but less than six offences in the last year. ",
                "4": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "5": "Unweighted base given for sex and age of offender is for the question asking about number of offenders; other bases are similar.",
                "6": "Figures may not sum to 100 as more than one response possible.",
                "7":  "All respondents were asked about their relationship to the offender(s) - this includes detailed questions of victims who experienced three or less offences and brief questions to those who experienced more than three but less than six offences in the last year.", 
                },
        additional_formatting = formatting
        )
