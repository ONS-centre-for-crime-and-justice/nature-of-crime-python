# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.other_household_theft.item_stolen.table_2a_item_stolen import household_theft_items_table_2a
from pipeline.other_household_theft.item_stolen.table_2b_item_stolen import household_theft_items_table_2b
from pipeline.other_household_theft.item_stolen.table_2c_item_stolen import household_theft_items_table_2c

from pipeline.additional_formatting import formatting
#########################################################################################################################################
#THEFT TABLE
#########################################################################################################################################

############################################################################################################
#ALL HOUSEHOLD THEFT
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_items_table_2a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

household_theft_items_table_2a["table_label"].replace({
        "Jewellery" : "Jewellery$$3$$",
        "Watches" : "Watches$$3$$",
        "Electrical goods/cameras" : "Electrical goods/cameras$$4$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_items_table_2a_gptable = gpt.GPTable(
        table = household_theft_items_table_2a,
        index_columns = {2: 0},
        title = "Table 2a: Items stolen in incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Separate categories for jewellery and watches were introduced in the year ending March 2015.",
                "4": "Electrical goods/cameras' includes televisions, videos, stereos, cameras, MP3 players and DVD players.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT IN A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_items_table_2b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

household_theft_items_table_2b["table_label"].replace({
        "Jewellery" : "Jewellery$$3$$",
        "Watches" : "Watches$$3$$",
        "Electrical goods/cameras" : "Electrical goods/cameras$$4$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_items_table_2b_gptable = gpt.GPTable(
        table = household_theft_items_table_2b,
        index_columns = {2: 0},
        title = "Table 2b: Items stolen in incidents of other household theft in a dwelling, year ending March 2010 to year ending March 2020 CSEW CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Separate categories for jewellery and watches were introduced in the year ending March 2015.",
                "4": "Electrical goods/cameras' includes televisions, videos, stereos, cameras, MP3 players and DVD players.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT OUTSIDE A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_items_table_2c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

household_theft_items_table_2c["table_label"].replace({
        "Jewellery" : "Jewellery$$3$$",
        "Watches" : "Watches$$3$$",
        "Electrical goods/cameras" : "Electrical goods/cameras$$4$$",
        }, inplace=True)
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_items_table_2c_gptable = gpt.GPTable(
        table = household_theft_items_table_2c,
        index_columns = {2: 0},
        title = "Table 2c: Items stolen in incidents of other household theft outside a dwelling, year ending March 2010 to year ending March 2020 CSEW CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "Separate categories for jewellery and watches were introduced in the year ending March 2015.",
                "4": "Electrical goods/cameras' includes televisions, videos, stereos, cameras, MP3 players and DVD players.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )
