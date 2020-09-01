# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.vehicle_security.table_11a_vehicle_security import vehicle_security_table_11a
from pipeline.vehicle_related_theft.vehicle_security.table_11b_vehicle_security import vehicle_security_table_11b
from pipeline.vehicle_related_theft.vehicle_security.table_11c_vehicle_security import vehicle_security_table_11c
from pipeline.vehicle_related_theft.vehicle_security.table_11d_vehicle_security import vehicle_security_table_11d
from pipeline.additional_formatting import formatting

##################################################################################
#Table 11a
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_security_table_11a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_security_table_11a["table_label"].replace({
        "Unweighted base - number of incidents": "Unweighted base - number of incidents$$4$$",
        }, inplace=True)
    
vehicle_security_table_11a.reset_index(inplace = True)

vehicle_security_table_11a = vehicle_security_table_11a.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_security_table_11a_gptable = gpt.GPTable(
        table = vehicle_security_table_11a,
        index_columns = {2: 0},
        title = "Table 11a: Vehicle security precautions on cars/vans targeted in all vehicle-related theft, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures are based on all cars or light vans subject to all vehicle-related theft and are based on what security measures were in place at the time of the vehicle-related theft.",
                "2": "Figures may not sum to 100 as more than one response possible.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "4": "Base given is for 'Central locking'. Others bases are similar."
                },
         additional_formatting = formatting
        )


##################################################################################
#Table 11b
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_security_table_11b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$4$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$4$$"
         }, inplace=True)

vehicle_security_table_11b["table_label"].replace({
        "Unweighted base - number of incidents": "Unweighted base - number of incidents$$5$$",
        }, inplace=True)
    
vehicle_security_table_11b.reset_index(inplace = True)

vehicle_security_table_11b = vehicle_security_table_11b.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_security_table_11b_gptable = gpt.GPTable(
        table = vehicle_security_table_11b,
        index_columns = {2: 0},
        title = "Table 11b: Vehicle security precautions on cars/vans targeted in theft of a vehicle, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$$$3$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures are based on all cars or light vans subject to vehicle theft and are based on what security measures were in place at the time of the vehicle-related theft.",
                "2": "For survey years ending March 2013 through to March 2018 estimates are based on fewer than 50 respondents and should be interpreted with caution.",
                "3": "Figures may not sum to 100 as more than one response possible.",
                "4": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "5": "Base given is for 'Central locking'. Others bases are similar."
                },
         additional_formatting = formatting
        )



##################################################################################
#Table 11c
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_security_table_11c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_security_table_11c["table_label"].replace({
        "Unweighted base - number of incidents": "Unweighted base - number of incidents$$4$$",
        }, inplace=True)
    
vehicle_security_table_11c.reset_index(inplace = True)

vehicle_security_table_11c = vehicle_security_table_11c.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_security_table_11c_gptable = gpt.GPTable(
        table = vehicle_security_table_11c,
        index_columns = {2: 0},
        title = "Table 11c: Vehicle security precautions on cars/vans targeted in theft from a vehicle, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures are based on all cars or light vans subject to theft from the vehicle and are based on what security measures were in place at the time of the vehicle-related theft.",
                "2": "Figures may not sum to 100 as more than one response possible.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "4": "Base given is for 'Central locking'. Others bases are similar."
                },
         additional_formatting = formatting
        )



##################################################################################
#Table 11d
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_security_table_11d.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$3$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$3$$"
         }, inplace=True)

vehicle_security_table_11d["table_label"].replace({
        "Unweighted base - number of incidents": "Unweighted base - number of incidents$$4$$",
        }, inplace=True)
    
vehicle_security_table_11d.reset_index(inplace = True)

vehicle_security_table_11d = vehicle_security_table_11d.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_security_table_11d_gptable = gpt.GPTable(
        table = vehicle_security_table_11d,
        index_columns = {2: 0},
        title = "Table 11d: Vehicle security precautions on cars/vans targeted in attempted theft of and from a vehicle, year ending March 2010 to year ending March 2020 CSEW$$1$$$$2$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Figures are based on all cars or light vans subject to attempted vehicle theft and are based on what security measures were in place at the time of the vehicle-related theft.",
                "2": "Figures may not sum to 100 as more than one response possible.",
                "3": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "4": "Base given is for 'Central locking'. Others bases are similar."
                },
         additional_formatting = formatting
        )
