# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.location.table_2a_location import vehicle_location_table_2a
from pipeline.vehicle_related_theft.location.table_2b_location import vehicle_location_table_2b
from pipeline.vehicle_related_theft.location.table_2c_location import vehicle_location_table_2c
from pipeline.vehicle_related_theft.location.table_2d_location import vehicle_location_table_2d
from pipeline.additional_formatting import formatting

##################################################################################
#Table 2a
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_location_table_2a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_location_table_2a["table_label"].replace({
        "Home - Semi-private": "Home - Semi-private$$3$$",
        }, inplace=True)
    
vehicle_location_table_2a.reset_index(inplace = True)

vehicle_location_table_2a = vehicle_location_table_2a.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_location_table_2a_gptable = gpt.GPTable(
        table = vehicle_location_table_2a,
        index_columns = {2: 0},
        title = "Table 2a: Where incidents of all vehicle-related theft occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "'Semi-private' includes outside areas on the premises and garages or car parks around but not connected to the home.",
                },
        notes = [": denotes not applicable"], 
        additional_formatting = formatting
        )


##################################################################################
#Table 2b
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_location_table_2b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_location_table_2b["table_label"].replace({
        "Home - Semi-private": "Home - Semi-private$$3$$",
        }, inplace=True)
    
vehicle_location_table_2b.reset_index(inplace = True)

vehicle_location_table_2b = vehicle_location_table_2b.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_location_table_2b_gptable = gpt.GPTable(
        table = vehicle_location_table_2b,
        index_columns = {2: 0},
        title = "Table 2b: Where incidents of theft of vehicles occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "'Semi-private' includes outside areas on the premises and garages or car parks around but not connected to the home.",
                },
        notes = [": denotes not applicable"], 
        additional_formatting = formatting
        )

##################################################################################
#Table 2c
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_location_table_2c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_location_table_2c["table_label"].replace({
        "Home - Semi-private": "Home - Semi-private$$3$$",
        }, inplace=True)
    
vehicle_location_table_2c.reset_index(inplace = True)

vehicle_location_table_2c = vehicle_location_table_2c.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_location_table_2c_gptable = gpt.GPTable(
        table = vehicle_location_table_2c,
        index_columns = {2: 0},
        title = "Table 2c: Where incidents of theft from vehicles occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "'Semi-private' includes outside areas on the premises and garages or car parks around but not connected to the home.",
                 },
        notes = [": denotes not applicable"], 
        additional_formatting = formatting
        )

##################################################################################
#Table 2d
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_location_table_2d.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_location_table_2d["table_label"].replace({
        "Home - Semi-private": "Home - Semi-private$$3$$",
        }, inplace=True)
    
vehicle_location_table_2d.reset_index(inplace = True)

vehicle_location_table_2d = vehicle_location_table_2d.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_location_table_2d_gptable = gpt.GPTable(
        table = vehicle_location_table_2d,
        index_columns = {2: 0},
        title = "Table 2d: Where incidents of attempted theft of and from vehicles occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
               "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
               "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
               "3": "'Semi-private' includes outside areas on the premises and garages or car parks around but not connected to the home.",
                },
        notes = [": denotes not applicable"], 
        additional_formatting = formatting
        )
