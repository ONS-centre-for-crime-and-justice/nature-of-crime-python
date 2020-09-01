# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.method_of_entry.table_3a_entry import vehicle_entry_table_3a
from pipeline.vehicle_related_theft.method_of_entry.table_3b_entry import vehicle_entry_table_3b
from pipeline.vehicle_related_theft.method_of_entry.table_3c_entry import vehicle_entry_table_3c
from pipeline.vehicle_related_theft.method_of_entry.table_3d_entry import vehicle_entry_table_3d
from pipeline.additional_formatting import formatting

##################################################################################
#Table 3a
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_entry_table_3a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_entry_table_3a["table_label"].replace({
        "Offender manipulated signal from remote locking device" : "Offender manipulated signal from remote locking device$$3$$",
        "Unweighted base - number of incidents": "Unweighted base - number of incidents$$4$$"
        }, inplace=True)
    
vehicle_entry_table_3a.reset_index(inplace = True)

vehicle_entry_table_3a = vehicle_entry_table_3a.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_entry_table_3a_gptable = gpt.GPTable(
        table = vehicle_entry_table_3a,
        index_columns = {2: 0},
        title = "Table 3a: Method of entry in incidents of all vehicle-related theft, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as respondents can provide up to two options.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "A new category was added into the survey from the year ending March 2019.",
                "4": "Base includes theft of and from vehicles and attempts where there was entry.",
                },
        notes = [": denotes not applicable"],
            additional_formatting = formatting
        )

##################################################################################
#Table 3b
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_entry_table_3b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)
         
vehicle_entry_table_3b["table_label"].replace({
        "Offender manipulated signal from remote locking device" : "Offender manipulated signal from remote locking device$$4$$",
        }, inplace=True)
    
vehicle_entry_table_3b.reset_index(inplace = True)

vehicle_entry_table_3b = vehicle_entry_table_3b.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_entry_table_3b_gptable = gpt.GPTable(
        table = vehicle_entry_table_3b,
        index_columns = {2: 0},
        title = "Table 3b: Method of entry in incidents of theft of vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as respondents can provide up to two options.",
                "2": "For survey years ending March 2013 through to March 2019 estimates are based on fewer than 50 respondents and should be interpreted with caution.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "4": "A new category was added into the survey from the year ending March 2019.",
                },
         notes = [": denotes not applicable"],
            additional_formatting = formatting
        )

##################################################################################
#Table 3c
##################################################################################
vehicle_entry_table_3c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)
         
vehicle_entry_table_3c["table_label"].replace({
        "Offender manipulated signal from remote locking device" : "Offender manipulated signal from remote locking device$$3$$",
        }, inplace=True)
    
vehicle_entry_table_3c.reset_index(inplace = True)

vehicle_entry_table_3c = vehicle_entry_table_3c.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_entry_table_3c_gptable = gpt.GPTable(
        table = vehicle_entry_table_3c,
        index_columns = {2: 0},
        title = "Table 3c: Method of entry in incidents of theft from vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as respondents can provide up to two options.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "A new category was added into the survey from the year ending March 2019.",
                },
         notes = [": denotes not applicable"],
            additional_formatting = formatting
        )

##################################################################################
#Table 3d
##################################################################################
vehicle_entry_table_3d.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)
         
vehicle_entry_table_3d["table_label"].replace({
             }, inplace=True)
    
vehicle_entry_table_3d.reset_index(inplace = True)

vehicle_entry_table_3d = vehicle_entry_table_3d.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_entry_table_3d_gptable = gpt.GPTable(
        table = vehicle_entry_table_3d,
        index_columns = {2: 0},
        title = "Table 3d: Method of entry in attempts of and from vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures may not sum to 100 as respondents can provide up to two options.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
         additional_formatting = formatting
        )
