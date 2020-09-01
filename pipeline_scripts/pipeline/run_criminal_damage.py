# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt

# IF YOU ARE RUNNING THIS FOR THE FIRST TIME YOU NEED TO REMOVE THE '#' FROM THE LINE BELOW
# from pipeline.criminal_damage.creating_criminal_damage_data import vf_data

from pipeline.criminal_damage.timing.criminal_damage_timing_footnotes import criminal_damage_timing_gptable_1a
from pipeline.criminal_damage.timing.criminal_damage_timing_footnotes import criminal_damage_timing_gptable_1b
from pipeline.criminal_damage.timing.criminal_damage_timing_footnotes import criminal_damage_timing_gptable_1c

from pipeline.criminal_damage.location.criminal_damage_location_footnotes import criminal_damage_location_gptable_2
#from pipeline.criminal_damage.location.criminal_damage_location_footnotes import criminal_damage_location_gptable_2b
#from pipeline.criminal_damage.location.criminal_damage_location_footnotes import criminal_damage_location_gptable_2c

from pipeline.criminal_damage.damage.criminal_damage_type_of_damage_footnotes import criminal_damage_type_of_damage_gptable_3a
from pipeline.criminal_damage.damage.criminal_damage_type_of_damage_footnotes import criminal_damage_type_of_damage_gptable_3b
#from pipeline.criminal_damage.damage.criminal_damage_type_of_damage_footnotes import criminal_damage_location_gptable_3c

from pipeline.criminal_damage.cost.criminal_damage_cost_footnotes import criminal_damage_cost_gptable_4a
from pipeline.criminal_damage.cost.criminal_damage_cost_footnotes import criminal_damage_cost_gptable_4b
from pipeline.criminal_damage.cost.criminal_damage_cost_footnotes import criminal_damage_cost_gptable_4c

from pipeline.criminal_damage.emotional_impact.criminal_damage_emotional_impact_footnotes import criminal_damage_emotional_impact_gptable_5a
from pipeline.criminal_damage.emotional_impact.criminal_damage_emotional_impact_footnotes import criminal_damage_emotional_impact_gptable_5b
from pipeline.criminal_damage.emotional_impact.criminal_damage_emotional_impact_footnotes import criminal_damage_emotional_impact_gptable_5c

from pipeline.criminal_damage.seriousness.criminal_damage_seriousness_footnotes import criminal_damage_seriousness_gptable_6a
from pipeline.criminal_damage.seriousness.criminal_damage_seriousness_footnotes import criminal_damage_seriousness_gptable_6b
from pipeline.criminal_damage.seriousness.criminal_damage_seriousness_footnotes import criminal_damage_seriousness_gptable_6c

from pipeline.criminal_damage.offender.criminal_damage_offender_footnotes import criminal_damage_offender_gptable_7a
from pipeline.criminal_damage.offender.criminal_damage_offender_footnotes import criminal_damage_offender_gptable_7b
from pipeline.criminal_damage.offender.criminal_damage_offender_footnotes import criminal_damage_offender_gptable_7c




##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################

crime_theme = gpt.Theme(r"D:\Repos\crime-tables-python\crimetheme.yaml")

cover = gpt.Cover(
        cover_label = "Notes",
        title = "Nature of crime: criminal damage",
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
        filename = str(output_directory / "NoC Criminal Damage Tables.xlsx"),
        sheets = {"Table_1a": criminal_damage_timing_gptable_1a,
                  "Table_1b": criminal_damage_timing_gptable_1b,
                  "Table_1c": criminal_damage_timing_gptable_1c,
                  "Table_2": criminal_damage_location_gptable_2,
                  "Table_3a": criminal_damage_type_of_damage_gptable_3a,
                  "Table_3b": criminal_damage_type_of_damage_gptable_3b,
                  "Table_4a": criminal_damage_cost_gptable_4a,
                  "Table_4b": criminal_damage_cost_gptable_4b,
                  "Table_4c": criminal_damage_cost_gptable_4c,
                  "Table_5a": criminal_damage_emotional_impact_gptable_5a,
                  "Table_5b": criminal_damage_emotional_impact_gptable_5b,
                  "Table_5c": criminal_damage_emotional_impact_gptable_5c,
                  "Table_6a": criminal_damage_seriousness_gptable_6a,
                  "Table_6b": criminal_damage_seriousness_gptable_6b,
                  "Table_6c": criminal_damage_seriousness_gptable_6c,
                  "Table_7a": criminal_damage_offender_gptable_7a,
                  "Table_7b": criminal_damage_offender_gptable_7b,
                  "Table_7c": criminal_damage_offender_gptable_7c,
                    },
        theme = crime_theme,
        cover = cover
        )

##################################################################################
#TIMING TABLES
##################################################################################

ws=wb.worksheets()[1]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

ws=wb.worksheets()[2]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

ws=wb.worksheets()[3]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#LOCATION TABLE
##################################################################################

ws=wb.worksheets()[4]
ws.set_row(7,height = 30)
ws.set_row(9,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#TYPE OF DAMAGE TABLES
##################################################################################

ws=wb.worksheets()[5]
ws.set_row(15,height = 30)
ws.set_column(0, 0, 40)

ws=wb.worksheets()[6]
ws.set_row(9,height = 30)
ws.set_row(12,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_column(0, 0, 40)



##################################################################################
#COST TABLE
##################################################################################

ws=wb.worksheets()[7]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

ws=wb.worksheets()[8]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

ws=wb.worksheets()[9]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)



##################################################################################
#EMOTIONAL IMPACT TABLE
##################################################################################

ws=wb.worksheets()[10]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

ws=wb.worksheets()[11]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

ws=wb.worksheets()[12]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 34)

##################################################################################
#SERIOUSNESS TABLE
##################################################################################

ws=wb.worksheets()[13]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

ws=wb.worksheets()[14]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

ws=wb.worksheets()[15]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 26)
ws.set_column(1, 1, 34)

##################################################################################
#OFFENDER CHARACTERISTICS TABLE
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
