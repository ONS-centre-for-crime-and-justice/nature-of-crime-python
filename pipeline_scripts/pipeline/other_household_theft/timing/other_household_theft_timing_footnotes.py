# -*- coding: utf-8 -*-

import gptables as gpt

from pipeline.other_household_theft.timing.table_1a_timing import household_theft_timing_table_1a
from pipeline.other_household_theft.timing.table_1b_timing import household_theft_timing_table_1b
from pipeline.other_household_theft.timing.table_1c_timing import household_theft_timing_table_1c

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#TIMING TABLES
#########################################################################################################################################

############################################################################################################
#ALL HOUSEHOLD THEFT
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
household_theft_timing_table_1a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)


household_theft_timing_table_1a["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_timing_table_1a_gptable = gpt.GPTable(
        table = household_theft_timing_table_1a,
        index_columns = {2: 0},
        title = "Table 1a: Timing of when incidents of other household theft occurred, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "Weekend is from Friday 6pm to Monday 6am.",
                "3": "Morning is from 6am to noon; afternoon is from noon to 6pm.",
                "4": "Evening is from 6pm to midnight; night is midnight to 6am.",
                "5": "Early evening is from 6pm to 10pm.",
                "6": "Late evening is from 10pm to midnight. ",
                },
        additional_formatting = formatting
        )


############################################################################################################
#HOUSEHOLD THEFT IN A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_timing_table_1b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

household_theft_timing_table_1b["table_label"].replace({
        "At the weekend": "At the weekend$$3$$",
        "Morning/Afternoon":"Morning/Afternoon$$4$$",
        "Evening/Night": "Evening/Night$$5$$",
        "Early evening": "Early evening$$6$$",
        "Late evening": "Late evening$$7$$",
        }, inplace=True)
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_timing_table_1b_gptable = gpt.GPTable(
        table = household_theft_timing_table_1b,
        index_columns = {2: 0},
        title = "Table 1b: Timing of when incidents of household theft in a dwelling occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "For survey year ending March 2018 estimates are based on fewer than 50 respondents and should be interpreted with caution.", 
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Weekend is from Friday 6pm to Monday 6am.",
                "4": "Morning is from 6am to noon; afternoon is from noon to 6pm.",
                "5": "Evening is from 6pm to midnight; night is midnight to 6am.",
                "6": "Early evening is from 6pm to 10pm.",
                "7": "Late evening is from 10pm to midnight. ",
                },
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT OUTSIDE A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_timing_table_1c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

household_theft_timing_table_1c["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_timing_table_1c_gptable = gpt.GPTable(
        table = household_theft_timing_table_1c,
        index_columns = {2: 0},
        title = "Table 1c: Timing of when incidents of  household theft outside the dwelling occurred, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "Weekend is from Friday 6pm to Monday 6am.",
                "3": "Morning is from 6am to noon; afternoon is from noon to 6pm.",
                "4": "Evening is from 6pm to midnight; night is midnight to 6am.",
                "5": "Early evening is from 6pm to 10pm.",
                "6": "Late evening is from 10pm to midnight. ",
                },
        additional_formatting = formatting
        )

