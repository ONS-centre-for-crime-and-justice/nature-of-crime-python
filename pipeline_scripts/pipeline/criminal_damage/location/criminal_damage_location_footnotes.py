# -*- coding: utf-8 -*-

import gptables as gpt

from pipeline.criminal_damage.location.table_2_location import criminal_damage_location_table_2

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#LOCATION TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_location_table_2.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

criminal_damage_location_table_2["table_label"].replace({
        "Home - Semi-private":"Home - Semi-private$$3$$",
        }, inplace=True)

criminal_damage_location_table_2.reset_index(inplace=True) 
criminal_damage_location_table_2 = criminal_damage_location_table_2.drop(['index'], axis = 1) 
    
##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_location_gptable_2 = gpt.GPTable(
        table = criminal_damage_location_table_2,
        index_columns = {2: 0},
        title = "Table 2: Where incidents of criminal damage to a vehicle occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "'Semi-private' includes outside areas on the premises and garages or car parks around but not connected to the home.",
                },
        additional_formatting = formatting
        )
