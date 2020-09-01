# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.percieved_seriousness.table_9a_seriousness import vehicle_seriousness_table_9a
from pipeline.vehicle_related_theft.percieved_seriousness.table_9b_seriousness import vehicle_seriousness_table_9b
from pipeline.vehicle_related_theft.percieved_seriousness.table_9c_seriousness import vehicle_seriousness_table_9c
from pipeline.vehicle_related_theft.percieved_seriousness.table_9d_seriousness import vehicle_seriousness_table_9d
from pipeline.additional_formatting import formatting

##################################################################################
#Table 9a
##################################################################################

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################
vehicle_seriousness_table_9a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

vehicle_seriousness_table_9a_gptable = gpt.GPTable(
        table = vehicle_seriousness_table_9a,
        index_columns = {1: 0, 2: 1},
        title = "Table 9a: Perceived seriousness of incidents of vehicle-related theft, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )


vehicle_seriousness_table_9b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)


vehicle_seriousness_table_9b_gptable = gpt.GPTable(
        table = vehicle_seriousness_table_9b,
        index_columns = {1: 0, 2: 1},
        title = "Table 9b: Perceived seriousness of incidents of all vehicle-related theft, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )


vehicle_seriousness_table_9c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)


vehicle_seriousness_table_9c_gptable = gpt.GPTable(
        table = vehicle_seriousness_table_9c,
        index_columns = {1: 0, 2: 1},
        title = "Table 9c: Perceived seriousness of incidents of theft of a vehicle, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )


vehicle_seriousness_table_9d.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)


vehicle_seriousness_table_9d_gptable = gpt.GPTable(
        table = vehicle_seriousness_table_9d,
        index_columns = {1: 0, 2: 1},
        title = "Table 9d: Perceived seriousness of incidents of attempted theft of and from a vehicle, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "1-6 represents the least serious assessment and 14-20 represents the most serious.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                },
        additional_formatting = formatting
        )
