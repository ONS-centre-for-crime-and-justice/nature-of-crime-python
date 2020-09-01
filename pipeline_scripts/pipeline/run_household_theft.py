# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

#IF YOU ARE RUNNING THIS FOR THE FIRST TIME YOU NEED TO REMOVE THE '#' FROM THE LINE BELOW
#from pipeline.other_household_theft.creating_other_household_theft_data import vf_data

from pipeline.other_household_theft.timing.other_household_theft_timing_footnotes import household_theft_timing_table_1a_gptable
from pipeline.other_household_theft.timing.other_household_theft_timing_footnotes import household_theft_timing_table_1b_gptable
from pipeline.other_household_theft.timing.other_household_theft_timing_footnotes import household_theft_timing_table_1c_gptable

from pipeline.other_household_theft.item_stolen.other_household_theft_item_stolen_footnotes import household_theft_items_table_2a_gptable
from pipeline.other_household_theft.item_stolen.other_household_theft_item_stolen_footnotes import household_theft_items_table_2b_gptable
from pipeline.other_household_theft.item_stolen.other_household_theft_item_stolen_footnotes import household_theft_items_table_2c_gptable

from pipeline.other_household_theft.cost.other_household_theft_cost_footnotes import household_theft_cost_table_3a_gptable
from pipeline.other_household_theft.cost.other_household_theft_cost_footnotes import household_theft_cost_table_3b_gptable
from pipeline.other_household_theft.cost.other_household_theft_cost_footnotes import household_theft_cost_table_3c_gptable

from pipeline.other_household_theft.emotional_impact.other_household_theft_emotional_impact_footnotes import household_theft_emotional_impact_table_4a_gptable
from pipeline.other_household_theft.emotional_impact.other_household_theft_emotional_impact_footnotes import household_theft_emotional_impact_table_4b_gptable
from pipeline.other_household_theft.emotional_impact.other_household_theft_emotional_impact_footnotes import household_theft_emotional_impact_table_4c_gptable

from pipeline.other_household_theft.seriousness.other_household_theft_seriousness_footnotes import household_theft_seriousness_table_5a_gptable
from pipeline.other_household_theft.seriousness.other_household_theft_seriousness_footnotes import household_theft_seriousness_table_5b_gptable
from pipeline.other_household_theft.seriousness.other_household_theft_seriousness_footnotes import household_theft_seriousness_table_5c_gptable

from pipeline.other_household_theft.offender.other_household_theft_offender_footnotes import household_theft_offender_table_6a_gptable
from pipeline.other_household_theft.offender.other_household_theft_offender_footnotes import household_theft_offender_table_6b_gptable
from pipeline.other_household_theft.offender.other_household_theft_offender_footnotes import household_theft_offender_table_6c_gptable


##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################

crime_theme = gpt.Theme(r"D:\Repos\crime-tables-python\crimetheme.yaml")

cover = gpt.Cover(
        cover_label = "Notes",
        title = "Nature of crime: other household theft",
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
        filename = str(output_directory / "NoC Other Household Theft Tables.xlsx"),
        sheets = {"Table_1a": household_theft_timing_table_1a_gptable,
                  "Table_1b": household_theft_timing_table_1b_gptable,
                  "Table_1c": household_theft_timing_table_1c_gptable,
                  "Table_2a": household_theft_items_table_2a_gptable,
                  "Table_2b": household_theft_items_table_2b_gptable,
                  "Table_2c": household_theft_items_table_2c_gptable,
                  "Table_3a": household_theft_cost_table_3a_gptable,
                  "Table_3b": household_theft_cost_table_3b_gptable,
                  "Table_3c": household_theft_cost_table_3c_gptable,
                  "Table_4a": household_theft_emotional_impact_table_4a_gptable,
                  "Table_4b": household_theft_emotional_impact_table_4b_gptable,
                  "Table_4c": household_theft_emotional_impact_table_4c_gptable,
                  "Table_5a": household_theft_seriousness_table_5a_gptable,
                  "Table_5b": household_theft_seriousness_table_5b_gptable,
                  "Table_5c": household_theft_seriousness_table_5c_gptable, 
                  "Table_6a": household_theft_offender_table_6a_gptable,
                  "Table_6b": household_theft_offender_table_6b_gptable,
                  "Table_6c": household_theft_offender_table_6c_gptable,   
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
#FORMATTING TABLE 1c
##################################################################################

ws=wb.worksheets()[3]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2a
##################################################################################

ws=wb.worksheets()[4]
ws.set_row(27,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2b
##################################################################################

ws=wb.worksheets()[5]
ws.set_row(27,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2c
##################################################################################

ws=wb.worksheets()[6]
ws.set_row(27,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 3a
##################################################################################

ws=wb.worksheets()[7]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 3b
##################################################################################

ws=wb.worksheets()[8]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 3c
##################################################################################

ws=wb.worksheets()[9]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 4a
##################################################################################

ws=wb.worksheets()[10]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 4b
##################################################################################

ws=wb.worksheets()[11]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 4c
##################################################################################

ws=wb.worksheets()[12]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 5a
##################################################################################

ws=wb.worksheets()[13]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 5b
##################################################################################

ws=wb.worksheets()[14]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 5c
##################################################################################

ws=wb.worksheets()[15]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

##################################################################################
#FORMATTING TABLE 6a
##################################################################################

ws=wb.worksheets()[16]
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
#FORMATTING TABLE 6b
##################################################################################

ws=wb.worksheets()[17]
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
#FORMATTING TABLE 6c
##################################################################################
ws=wb.worksheets()[18]
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







