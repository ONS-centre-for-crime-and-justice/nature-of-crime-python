# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.personal_other_theft.item_stolen.table_3a_item_stolen import personal_theft_items_table_3a
from pipeline.personal_other_theft.item_stolen.table_3b_item_stolen import other_personal_theft_items_table_3b

from pipeline.additional_formatting import formatting


#########################################################################################################################################
#Items stolen TABLE 3a
#########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

personal_theft_items_table_3a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

personal_theft_items_table_3a["table_label"].replace({
        "Documents" : "Documents$$3$$",
        "Jewellery" : "Jewellery$$5$$",
        "Watches" : "Watches$$5$$",
        "Computers/other electrical goods" : "Computers/other electrical goods$$4$$",
        }, inplace=True)

personal_theft_items_table_3a.reset_index(inplace=True) 
personal_theft_items_table_3a = personal_theft_items_table_3a.drop(['index'], axis = 1) 
    
##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

personal_theft_items_gptable_3a = gpt.GPTable(
        table = personal_theft_items_table_3a,
        index_columns = {2: 0},
        title = "Table 3a: Items stolen in incidents of theft from the person, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Cheque book' was incorporated into the 'Documents' category from the year ending March 2012 onwards.",
                "4": "Electrical goods/cameras' includes televisions, videos, stereos, cameras, MP3 players and DVD players.",
                "5": "Separate categories for jewellery and watches were introduced in the year ending March 2015.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )

#########################################################################################################################################
#Items stolen TABLE 3b
########################################################################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

other_personal_theft_items_table_3b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

other_personal_theft_items_table_3b["table_label"].replace({
        "Documents" : "Documents$$3$$",
        "Jewellery" : "Jewellery$$5$$",
        "Watches" : "Watches$$5$$",
        "Computers/other electrical goods" : "Computers/other electrical goods$$4$$",
        }, inplace=True)

other_personal_theft_items_table_3b.reset_index(inplace=True) 
other_personal_theft_items_table_3b = other_personal_theft_items_table_3b.drop(['index'], axis = 1) 
    
##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

other_personal_theft_items_gptable_3b = gpt.GPTable(
        table = other_personal_theft_items_table_3b,
        index_columns = {2: 0},
        title = "Table 3b: Items stolen in incidents of other theft of personal property, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Cheque book' was incorporated into the 'Documents' category from the year ending March 2012 onwards.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "4": "Electrical goods/cameras' includes televisions, videos, stereos, cameras, MP3 players and DVD players.",
                "5": "Separate categories for jewellery and watches were introduced in the year ending March 2015.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )
