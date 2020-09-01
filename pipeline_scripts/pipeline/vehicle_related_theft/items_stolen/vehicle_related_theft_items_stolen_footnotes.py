# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.items_stolen.table_6_items_stolen import vehicle_items_stolen_table_6
from pipeline.additional_formatting import formatting

##################################################################################
#Table 2a
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

vehicle_items_stolen_table_6.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_items_stolen_table_6["table_label"].replace({
        "Valuables": "Valuables$$3$$",
        "Electrical equipment": "Electrical equipment$$4$$",
        "Bicycle": "Bicycle$$5$$",
        }, inplace=True)
    
vehicle_items_stolen_table_6.reset_index(inplace = True)

vehicle_items_stolen_table_6 = vehicle_items_stolen_table_6.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_items_stolen_table_6_gptable = gpt.GPTable(
        table = vehicle_items_stolen_table_6,
        index_columns = {2: 0},
        title = "Table 6: Items stolen in incidents of theft from vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as more than one response possible.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "'Valuables' includes jewellery, handbag/briefcase/shopping bag, purses/wallets, cash, cheque books, credit cards, clothes and documents.",
                "4": "'Electrical equipment' includes satellite navigation systems, televisions, videos, MP3 players, DVD players and computer equipment.",
                "5": "Theft of bicycles only is not included in the category of theft from vehicles; hence bicycles stolen here are as a result of vehicle theft, e.g. being within a car when it is stolen. Theft of bicycles only can be found in the Nature of crime: bicycle theft tables.",
                  },
        additional_formatting = formatting
        )
