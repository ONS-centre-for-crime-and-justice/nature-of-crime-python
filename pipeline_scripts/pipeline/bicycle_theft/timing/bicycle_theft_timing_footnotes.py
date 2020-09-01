# -*- coding: utf-8 -*-

import gptables as gpt

from pipeline.bicycle_theft.timing.table_1_timing import bicycle_timing_table_1
from pipeline.additional_formatting import formatting


#########################################################################################################################################
#TIMING TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

bicycle_timing_table_1.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

bicycle_timing_table_1["table_label"].replace({
        "At the weekend": "At the weekend$$2$$",
        "Morning/Afternoon":"Morning/Afternoon$$3$$",
        "Evening/Night": "Evening/Night$$4$$",
        "Early evening": "Early evening$$5$$",
        "Late evening": "Late evening$$6$$",
        }, inplace=True)
    
bicycle_timing_table_1.reset_index(inplace = True)

bicycle_timing_table_1 = bicycle_timing_table_1.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

bicycle_timing_gptable_1 = gpt.GPTable(
        table = bicycle_timing_table_1,
        index_columns = {2: 0},
        title = "Table 1: Timing of when incidents of bicycle thefts occurred, year ending March 2010 to year ending March 2020 CSEW",
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
