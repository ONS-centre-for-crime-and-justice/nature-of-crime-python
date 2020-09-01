# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt


from pipeline.bicycle_theft.lock.table_6_lock import bicycle_lock_table_6
from pipeline.additional_formatting import formatting

#########################################################################################################################################
#LOCK TABLE
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

bicycle_lock_table_6.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

bicycle_lock_table_6["table_label"].replace({
        "Bicycle was locked":"Bicycle was locked$$2$$",
        }, inplace=True)

bicycle_lock_table_6["table_title"].replace({
        "Reason why bike was not locked":"Reason why bike was not locked$$3$$",
        }, inplace=True)

bicycle_lock_table_6.reset_index(inplace=True) 
bicycle_lock_table_6 = bicycle_lock_table_6.drop(['index'], axis = 1) 

    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

bicycle_lock_gptable_6 = gpt.GPTable(
        table = bicycle_lock_table_6,
        index_columns = {1: 0, 2: 1},
        title = "Table 6: Whether bicycle was locked at the time it was stolen and reasons why not, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "Question asks whether bicycle had a lock (chain, cable, shackle etc) on it when stolen; if bicycle was in a locked garage, shed or similar but not actually secured by a lock itself, this counts as not being locked.",
                "3": "Question asked since year ending March 2011. Question only asked of respondents who said their bicycle was not locked at the time of being stolen.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )











