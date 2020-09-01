# -*- coding: utf-8 -*-

import gptables as gpt

from pipeline.criminal_damage.timing.table_1a_timing import criminal_damage_timing_table_1a
from pipeline.criminal_damage.timing.table_1b_timing import criminal_damage_timing_table_1b
from pipeline.criminal_damage.timing.table_1c_timing import criminal_damage_timing_table_1c
from pipeline.additional_formatting import formatting


#########################################################################################################################################
#TIMING TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_timing_table_1a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

criminal_damage_timing_table_1a["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
criminal_damage_timing_table_1a.reset_index(inplace = True)

criminal_damage_timing_table_1a = criminal_damage_timing_table_1a.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_timing_gptable_1a = gpt.GPTable(
        table = criminal_damage_timing_table_1a,
        index_columns = {2: 0},
        title = "Table 1a: Timing of when incidents of criminal damage occurred, year ending March 2010 to year ending March 2020 CSEW",
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
#CRIMINAL DAMAGE TO A VEHICLE.
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_timing_table_1b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

criminal_damage_timing_table_1b["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
criminal_damage_timing_table_1b.reset_index(inplace = True)

criminal_damage_timing_table_1b = criminal_damage_timing_table_1b.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_timing_gptable_1b = gpt.GPTable(
        table = criminal_damage_timing_table_1b,
        index_columns = {2: 0},
        title = "Table 1b: Timing of when incidents of criminal damage to a vehicle occurred, year ending March 2010 to year ending March 2020 CSEW",
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
#ARSON AND OTHER CRIMINAL DAMAGE.
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_timing_table_1c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

criminal_damage_timing_table_1c["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
criminal_damage_timing_table_1c.reset_index(inplace = True)

criminal_damage_timing_table_1c = criminal_damage_timing_table_1c.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_timing_gptable_1c = gpt.GPTable(
        table = criminal_damage_timing_table_1c,
        index_columns = {2: 0},
        title = "Table 1c: Timing of when incidents of arson and other criminal damage occurred, year ending March 2010 to year ending March 2020 CSEW",
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
