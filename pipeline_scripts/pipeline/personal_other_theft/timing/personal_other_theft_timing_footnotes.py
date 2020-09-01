# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.personal_other_theft.timing.table_1a_timing import personal_theft_timing_table_1a
from pipeline.personal_other_theft.timing.table_1b_timing import other_personal_theft_timing_table_1b

from pipeline.additional_formatting import formatting


#########################################################################################################################################
#TIMING TABLE 1a
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

personal_theft_timing_table_1a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

personal_theft_timing_table_1a["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
personal_theft_timing_table_1a.reset_index(inplace = True)

personal_theft_timing_table_1a = personal_theft_timing_table_1a.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

personal_theft_timing_gptable_1a = gpt.GPTable(
        table = personal_theft_timing_table_1a,
        index_columns = {2: 0},
        title = "Table 1a: Timing of when incidents of theft from the person occurred, year ending March 2010 to year ending March 2020 CSEW",
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

#########################################################################################################################################
#TIMING TABLE 1b
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

other_personal_theft_timing_table_1b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

other_personal_theft_timing_table_1b["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
other_personal_theft_timing_table_1b.reset_index(inplace = True)

other_personal_theft_timing_table_1b = other_personal_theft_timing_table_1b.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

other_personal_theft_timing_gptable_1b = gpt.GPTable(
        table = other_personal_theft_timing_table_1b,
        index_columns = {2: 0},
        title = "Table 1b: Timing of when incidents of other theft of personal property occurred, year ending March 2010 to year ending March 2020 CSEW",
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
