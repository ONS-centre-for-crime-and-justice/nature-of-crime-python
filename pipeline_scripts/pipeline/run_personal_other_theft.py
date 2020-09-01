# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

#IF YOU ARE RUNNING THIS FOR THE FIRST TIME YOU NEED TO REMOVE THE '#' FROM THE LINE BELOW
#from pipeline.personal_other_theft.creating_personal_other_theft_data import vf_data

from pipeline.personal_other_theft.timing.personal_other_theft_timing_footnotes import personal_theft_timing_gptable_1a
from pipeline.personal_other_theft.timing.personal_other_theft_timing_footnotes import other_personal_theft_timing_gptable_1b

from pipeline.personal_other_theft.location.personal_other_theft_location_footnotes import personal_theft_location_gptable_2a
from pipeline.personal_other_theft.location.personal_other_theft_location_footnotes import other_personal_theft_location_gptable_2b

from pipeline.personal_other_theft.item_stolen.personal_other_theft_item_stolen_footnotes import personal_theft_items_gptable_3a
from pipeline.personal_other_theft.item_stolen.personal_other_theft_item_stolen_footnotes import other_personal_theft_items_gptable_3b

from pipeline.personal_other_theft.cost.personal_other_theft_cost_footnotes import personal_theft_cost_gptable_4a
from pipeline.personal_other_theft.cost.personal_other_theft_cost_footnotes import other_personal_theft_cost_gptable_4b

from pipeline.personal_other_theft.emotional_impact.personal_other_theft_emotional_impact_footnotes import personal_theft_emotional_impact_gptable_5a
from pipeline.personal_other_theft.emotional_impact.personal_other_theft_emotional_impact_footnotes import other_personal_theft_emotional_impact_gptable_5b

from pipeline.personal_other_theft.seriousness.personal_other_theft_seriousness_footnotes import personal_theft_seriousness_gptable_6a
from pipeline.personal_other_theft.seriousness.personal_other_theft_seriousness_footnotes import other_personal_theft_seriousness_gptable_6b

from pipeline.personal_other_theft.offender.personal_other_theft_offender_footnotes import personal_theft_offender_gptable_7a
from pipeline.personal_other_theft.offender.personal_other_theft_offender_footnotes import other_personal_theft_offender_gptable_7b

##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################

crime_theme = gpt.Theme(r"D:\Repos\crime-tables-python\crimetheme.yaml")

cover = gpt.Cover(
        cover_label = "Notes",
        title = "Nature of crime: personal and other theft",
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
        filename = str(output_directory / "NoC Personal and Other Theft Tables.xlsx"),
        sheets = {"Table_1a": personal_theft_timing_gptable_1a,
                  "Table_1b": other_personal_theft_timing_gptable_1b,
                  "Table_2a": personal_theft_location_gptable_2a,
                  "Table_2b": other_personal_theft_location_gptable_2b,
                  "Table_3a": personal_theft_items_gptable_3a,
                  "Table_3b": other_personal_theft_items_gptable_3b,
                  "Table_4a": personal_theft_cost_gptable_4a,
                  "Table_4b": other_personal_theft_cost_gptable_4b,
                  "Table_5a": personal_theft_emotional_impact_gptable_5a,
                  "Table_5b": other_personal_theft_emotional_impact_gptable_5b,
                  "Table_6a": personal_theft_seriousness_gptable_6a,
                  "Table_6b": other_personal_theft_seriousness_gptable_6b,
                  "Table_7a": personal_theft_offender_gptable_7a,
                  "Table_7b": other_personal_theft_offender_gptable_7b
                    },
        theme = crime_theme,
        cover = cover
        )

##################################################################################
#FORMATTING TABLE 1a
##################################################################################

ws=wb.worksheets()[1]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 1b
##################################################################################

ws=wb.worksheets()[2]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2a
##################################################################################

ws=wb.worksheets()[3]
ws.set_row(12,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2b
##################################################################################

ws=wb.worksheets()[4]
ws.set_row(13,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 3a
##################################################################################

ws=wb.worksheets()[5]
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 3b
##################################################################################

ws=wb.worksheets()[6]
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 4a
##################################################################################

ws=wb.worksheets()[7]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 4b
##################################################################################

ws=wb.worksheets()[8]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 5a
##################################################################################

ws=wb.worksheets()[9]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 5b
##################################################################################

ws=wb.worksheets()[10]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 6a
##################################################################################

ws=wb.worksheets()[11]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 6b
##################################################################################

ws=wb.worksheets()[12]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 7a
##################################################################################

ws=wb.worksheets()[13]
ws.set_row(5,height = 30)
ws.set_row(6,height = 30)
ws.set_row(10,height = 30)
ws.set_row(13,height = 30)
ws.set_row(19,height = 30)
ws.set_row(20,height = 30)
ws.set_row(23,height = 30)
ws.set_column(0, 0, 20)
ws.set_column(1, 1, 72)

##################################################################################
#FORMATTING TABLE 7b
##################################################################################

ws=wb.worksheets()[14]
ws.set_row(5,height = 30)
ws.set_row(6,height = 30)
ws.set_row(10,height = 30)
ws.set_row(13,height = 30)
ws.set_row(19,height = 30)
ws.set_row(20,height = 30)
ws.set_row(23,height = 30)
ws.set_column(0, 0, 20)
ws.set_column(1, 1, 72)

wb.close()
