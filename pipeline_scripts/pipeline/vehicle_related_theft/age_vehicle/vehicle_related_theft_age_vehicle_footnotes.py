# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.age_vehicle.table_10_age_vehicle import vehicle_age_table_10
from pipeline.additional_formatting import formatting

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################
vehicle_age_table_10.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)


vehicle_age_table_10_gptable = gpt.GPTable(
        table = vehicle_age_table_10,
        index_columns = {2: 0},
        title = "Table 10: Age of stolen vehicles, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Includes car/van, motorbike/moped.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
               },
        additional_formatting = formatting
        )