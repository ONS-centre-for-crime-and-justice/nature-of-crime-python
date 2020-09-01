# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

#IF YOU ARE RUNNING THIS FOR THE FIRST TIME YOU NEED TO REMOVE THE '#' FROM THE LINE BELOW
#from pipeline.bicycle_theft.creating_bicycle_theft_data import vf_data

from pipeline.bicycle_theft.timing.bicycle_theft_timing_footnotes import bicycle_timing_gptable_1
from pipeline.bicycle_theft.location.bicycle_theft_location_footnotes import bicycle_location_gptable_2
from pipeline.bicycle_theft.cost.bicycle_theft_cost_footnotes import bicycle_cost_gptable_3
from pipeline.bicycle_theft.emotional_impact.bicycle_theft_emotional_impact_footnotes import bicycle_emotional_impact_gptable_4
from pipeline.bicycle_theft.seriousness.bicycle_theft_seriousness_footnotes import bicycle_seriousness_gptable_5
from pipeline.bicycle_theft.lock.bicycle_theft_lock_footnotes import bicycle_lock_gptable_6



##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################

crime_theme = gpt.Theme(r"D:\Repos\crime-tables-python\crimetheme.yaml")

cover = gpt.Cover(
        cover_label = "Notes",
        title = "Nature of crime: bicycle theft",
        intro = ["Data tables shown in this workbook relate to the Crime Survey for England and Wales (CSEW)."],
        about = ["The data contained in these tables are from the Crime Survey for England and Wales (CSEW).", 
                 "For more information on these data, see the User guide to crime statistics for England and Wales",
                 "These tables have been built using Python and the code is available here – https://github.com/ONS-centre-for-crime-and-justice",
                 "Following a methodological change to the handling of repeat victimisation in the CSEW, these data are not comparable with data published before January 2019. For more information see ‘Improving victimisation estimates derived from the Crime Survey for England and Wales’",
                 "For further information about the Crime Survey for England and Wales (CSEW) and police recorded crime statistics, please email crimestatistics@ons.gov.uk",
                 "or write to: ONS Centre for Crime and Justice, Office for National Statistics, Room 2200, Segensworth Road, Titchfield, PO15 5RR"],           
        contact = ["Statistical contact: Nick Stripe", 
                   "Tel: 01329 444651",
                   "Email: crimestatistics@ons.gov.uk"])

##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################
output_directory = Path(r"D:\crimetables_output")
wb = gpt.produce_workbook(
        filename = str(output_directory / "NoC Bicycle Theft Tables.xlsx"),
        sheets = {"Table_1": bicycle_timing_gptable_1,
                  "Table_2": bicycle_location_gptable_2,
                  "Table_3": bicycle_cost_gptable_3,
                  "Table_4": bicycle_emotional_impact_gptable_4,
                  "Table_5": bicycle_seriousness_gptable_5,
                  "Table_6": bicycle_lock_gptable_6
                    },
        theme = crime_theme,
        cover = cover
        )

##################################################################################
#FORMATTING TABLE 1
##################################################################################

ws=wb.worksheets()[1]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2
##################################################################################

ws=wb.worksheets()[2]
ws.set_row(7,height = 30)
ws.set_row(9,height = 30)
ws.set_row(13,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 3
##################################################################################

ws=wb.worksheets()[3]

ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 4
##################################################################################

ws=wb.worksheets()[4]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)


##################################################################################
#FORMATTING TABLE 5
##################################################################################

ws=wb.worksheets()[5]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 30)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 6
##################################################################################

ws=wb.worksheets()[6]
ws.set_row(5,height = 30)
ws.set_row(6,height = 30)
ws.set_row(15,height = 30)
ws.set_column(0, 0, 30)
ws.set_column(1, 1, 40)

wb.close()


