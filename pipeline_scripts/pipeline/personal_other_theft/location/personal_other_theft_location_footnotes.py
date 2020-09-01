# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

from pipeline.personal_other_theft.location.table_2a_location import personal_theft_location_table_2a
from pipeline.personal_other_theft.location.table_2b_location import other_personal_theft_location_table_2b

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#LOCATION TABLE 2a
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

personal_theft_location_table_2a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

personal_theft_location_table_2a["table_label"].replace({
        "In/around public entertainment":"In/around public entertainment$$3$$",
        "Inside a pub":"Inside a pub$$3$$",
        "Other": "Other location$$4$$",
        }, inplace=True)

personal_theft_location_table_2a.reset_index(inplace=True) 
personal_theft_location_table_2a = personal_theft_location_table_2a.drop(['index'], axis = 1) 
    
##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

personal_theft_location_gptable_2a = gpt.GPTable(
        table = personal_theft_location_table_2a,
        index_columns = {2: 0},
        title = "Table 2a: Where incidents of theft from the person occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Categories changed in the year ending March 2009 so that nightclubs are now included in 'public entertainment' and not 'a pub'",
                "4": "Includes own home, inside a friend or relatives' home, inside or near place of work, car park, a school/college/university and somewhere else",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )

#########################################################################################################################################
#LOCATION TABLE 2b
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

other_personal_theft_location_table_2b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

other_personal_theft_location_table_2b["table_label"].replace({
        "In/around public entertainment ":"In/around public entertainment$$3$$",
        "Inside a pub":"Inside a pub$$3$$",
        "Inside other building":"Inside other building$$4$$",
        "Other": "Other location$$5$$",
        }, inplace=True)

other_personal_theft_location_table_2b.reset_index(inplace=True) 
other_personal_theft_location_table_2b = other_personal_theft_location_table_2b.drop(['index'], axis = 1) 
    
##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

other_personal_theft_location_gptable_2b = gpt.GPTable(
        table = other_personal_theft_location_table_2b,
        index_columns = {2: 0},
        title = "Table 2b: Where incidents of theft from the person occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2018 compared with the year ending March 2008 or year ending March 2017.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Categories changed in the year ending March 2009 so that nightclubs are now included in 'public entertainment' and not 'a pub'.",
                "4": "Inside other building' includes home, relatives or friends homes, sports club, public building other than work, and other building.",
                "5": "Includes outside a shop/supermarket, outside a school/college/university, car park and somewhere else.", 
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )

