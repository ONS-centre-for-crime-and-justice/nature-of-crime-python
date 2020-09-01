# -*- coding: utf-8 -*-
from pathlib import Path
import gptables as gpt


from pipeline.vehicle_related_theft.timing.vehicle_related_theft_timing_footnotes import vehicle_timing_1a_gptable
from pipeline.vehicle_related_theft.timing.vehicle_related_theft_timing_footnotes import vehicle_timing_1b_gptable
from pipeline.vehicle_related_theft.timing.vehicle_related_theft_timing_footnotes import vehicle_timing_1c_gptable
from pipeline.vehicle_related_theft.timing.vehicle_related_theft_timing_footnotes import vehicle_timing_1d_gptable

from pipeline.vehicle_related_theft.location.vehicle_related_theft_location_footnotes import vehicle_location_table_2a_gptable
from pipeline.vehicle_related_theft.location.vehicle_related_theft_location_footnotes import vehicle_location_table_2b_gptable
from pipeline.vehicle_related_theft.location.vehicle_related_theft_location_footnotes import vehicle_location_table_2c_gptable
from pipeline.vehicle_related_theft.location.vehicle_related_theft_location_footnotes import vehicle_location_table_2d_gptable

from pipeline.vehicle_related_theft.method_of_entry.vehicle_related_theft_entry_footnotes import vehicle_entry_table_3a_gptable
from pipeline.vehicle_related_theft.method_of_entry.vehicle_related_theft_entry_footnotes import vehicle_entry_table_3b_gptable
from pipeline.vehicle_related_theft.method_of_entry.vehicle_related_theft_entry_footnotes import vehicle_entry_table_3c_gptable
from pipeline.vehicle_related_theft.method_of_entry.vehicle_related_theft_entry_footnotes import vehicle_entry_table_3d_gptable

from pipeline.vehicle_related_theft.damage_recovery.vehicle_related_theft_damage_recovery_footnotes import vehicle_damage_recovery_table_4_gptable

from pipeline.vehicle_related_theft.cost_damage.vehicle_related_theft_cost_damage_footnotes import vehicle_cost_damage_table_5_gptable

from pipeline.vehicle_related_theft.items_stolen.vehicle_related_theft_items_stolen_footnotes import vehicle_items_stolen_table_6_gptable

from pipeline.vehicle_related_theft.cost_stolen.vehicle_related_theft_cost_stolen_footnotes import vehicle_cost_stolen_table_7a_gptable
from pipeline.vehicle_related_theft.cost_stolen.vehicle_related_theft_cost_stolen_footnotes import vehicle_cost_stolen_table_7b_gptable

from pipeline.vehicle_related_theft.emotional_impact.vehicle_related_theft_emotional_impact_footnotes import vehicle_emotional_impact_table_8a_gptable
from pipeline.vehicle_related_theft.emotional_impact.vehicle_related_theft_emotional_impact_footnotes import vehicle_emotional_impact_table_8b_gptable
from pipeline.vehicle_related_theft.emotional_impact.vehicle_related_theft_emotional_impact_footnotes import vehicle_emotional_impact_table_8c_gptable
from pipeline.vehicle_related_theft.emotional_impact.vehicle_related_theft_emotional_impact_footnotes import vehicle_emotional_impact_table_8d_gptable

from pipeline.vehicle_related_theft.percieved_seriousness.vehicle_related_theft_seriousness_footnotes import vehicle_seriousness_table_9a_gptable
from pipeline.vehicle_related_theft.percieved_seriousness.vehicle_related_theft_seriousness_footnotes import vehicle_seriousness_table_9b_gptable
from pipeline.vehicle_related_theft.percieved_seriousness.vehicle_related_theft_seriousness_footnotes import vehicle_seriousness_table_9c_gptable
from pipeline.vehicle_related_theft.percieved_seriousness.vehicle_related_theft_seriousness_footnotes import vehicle_seriousness_table_9d_gptable

from pipeline.vehicle_related_theft.age_vehicle.vehicle_related_theft_age_vehicle_footnotes import vehicle_age_table_10_gptable

from pipeline.vehicle_related_theft.vehicle_security.vehicle_related_theft_security_footnotes import vehicle_security_table_11a_gptable
from pipeline.vehicle_related_theft.vehicle_security.vehicle_related_theft_security_footnotes import vehicle_security_table_11b_gptable
from pipeline.vehicle_related_theft.vehicle_security.vehicle_related_theft_security_footnotes import vehicle_security_table_11c_gptable
from pipeline.vehicle_related_theft.vehicle_security.vehicle_related_theft_security_footnotes import vehicle_security_table_11d_gptable


##################################################################################
#RUNNING EACH INDIVIDUAL BICYCLE THEFT SCRIPT
##################################################################################


##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################

crime_theme = gpt.Theme(r"D:\Repos\crime-tables-python\crimetheme.yaml")

##################################################################################
#WRITING OUTPUT TO A EXCEL FILE
##################################################################################

cover = gpt.Cover(
        cover_label = "Notes",
        title = "Nature of crime: vehicle-related theft",
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

output_directory = Path(r"D:\crimetables_output")
wb = gpt.produce_workbook(
        filename = str(output_directory / "NoC Vehicle Theft Tables.xlsx"),
        sheets = {"Table_1a": vehicle_timing_1a_gptable,
                  "Table_1b": vehicle_timing_1b_gptable,
                  "Table_1c": vehicle_timing_1c_gptable,
                  "Table_1d": vehicle_timing_1d_gptable,
                  "Table_2a": vehicle_location_table_2a_gptable,
                  "Table_2b": vehicle_location_table_2b_gptable,
                  "Table_2c": vehicle_location_table_2c_gptable,
                  "Table_2d": vehicle_location_table_2d_gptable,
                  "Table_3a": vehicle_entry_table_3a_gptable,
                  "Table_3b": vehicle_entry_table_3b_gptable,
                  "Table_3c": vehicle_entry_table_3c_gptable,
                  "Table_3d": vehicle_entry_table_3d_gptable,
                  "Table_4": vehicle_damage_recovery_table_4_gptable,
                  "Table_5": vehicle_cost_damage_table_5_gptable,
                  "Table_6": vehicle_items_stolen_table_6_gptable,
                  "Table_7a": vehicle_cost_stolen_table_7a_gptable,
                  "Table_7b": vehicle_cost_stolen_table_7b_gptable,
                  "Table_8a": vehicle_emotional_impact_table_8a_gptable,
                  "Table_8b": vehicle_emotional_impact_table_8b_gptable,
                  "Table_8c": vehicle_emotional_impact_table_8c_gptable,
                  "Table_8d": vehicle_emotional_impact_table_8d_gptable,
                  "Table_9a": vehicle_seriousness_table_9a_gptable,
                  "Table_9b": vehicle_seriousness_table_9b_gptable,
                  "Table_9c": vehicle_seriousness_table_9c_gptable,
                  "Table_9d": vehicle_seriousness_table_9d_gptable,
                  "Table_10": vehicle_age_table_10_gptable,
                  "Table_11a": vehicle_security_table_11a_gptable,
                  "Table_11b": vehicle_security_table_11b_gptable,
                  "Table_11c": vehicle_security_table_11c_gptable,
                  "Table_11d": vehicle_security_table_11d_gptable,                
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
#FORMATTING TABLE 1d
##################################################################################

ws=wb.worksheets()[4]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(17,height = 30)
ws.set_row(18,height = 30)
ws.set_row(21,height = 30)
ws.set_column(0, 0, 40)




##################################################################################
#FORMATTING TABLE 2a
##################################################################################

ws=wb.worksheets()[5]
ws.set_row(7,height = 30)
ws.set_row(9,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2b
##################################################################################

ws=wb.worksheets()[6]
ws.set_row(7,height = 30)
ws.set_row(9,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2c
##################################################################################

ws=wb.worksheets()[7]
ws.set_row(7,height = 30)
ws.set_row(9,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 2d
##################################################################################

ws=wb.worksheets()[8]
ws.set_row(7,height = 30)
ws.set_row(9,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 40)



##################################################################################
#FORMATTING TABLE 3a
##################################################################################

ws=wb.worksheets()[9]
ws.set_row(12,height = 30)
ws.set_column(0, 0, 45)

##################################################################################
#FORMATTING TABLE 3b
##################################################################################

ws=wb.worksheets()[10]
ws.set_row(12,height = 30)
ws.set_column(0, 0, 45)

##################################################################################
#FORMATTING TABLE 3c
##################################################################################

ws=wb.worksheets()[11]
ws.set_row(12,height = 30)
ws.set_column(0, 0, 45)

##################################################################################
#FORMATTING TABLE 3d
##################################################################################

ws=wb.worksheets()[12]
ws.set_row(11,height = 30)
ws.set_column(0, 0, 45)




##################################################################################
#FORMATTING TABLE 4
##################################################################################

ws=wb.worksheets()[13]
ws.set_row(6,height = 30)
ws.set_row(7,height = 30)
ws.set_row(11,height = 30)
ws.set_column(0, 0, 40)



##################################################################################
#FORMATTING TABLE 5
##################################################################################

ws=wb.worksheets()[14]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)




##################################################################################
#FORMATTING TABLE 6
##################################################################################

ws=wb.worksheets()[15]
ws.set_row(23,height = 30)
ws.set_column(0, 0, 40)




##################################################################################
#FORMATTING TABLE 7a
##################################################################################

ws=wb.worksheets()[16]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 7b
##################################################################################

ws=wb.worksheets()[17]
ws.set_row(12,height = 30)
ws.set_row(14,height = 30)
ws.set_column(0, 0, 40)



##################################################################################
#FORMATTING TABLE 8a
##################################################################################

ws=wb.worksheets()[18]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 8b
##################################################################################

ws=wb.worksheets()[19]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 8b
##################################################################################

ws=wb.worksheets()[20]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 8d
##################################################################################

ws=wb.worksheets()[21]
ws.set_row(9,height = 30)
ws.set_row(10,height = 30)
ws.set_row(20,height = 30)
ws.set_column(0, 0, 40)
ws.set_column(1, 1, 40)


##################################################################################
#FORMATTING TABLE 9a
##################################################################################

ws=wb.worksheets()[22]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 30)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 9b
##################################################################################

ws=wb.worksheets()[23]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 30)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 9b
##################################################################################

ws=wb.worksheets()[24]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 30)
ws.set_column(1, 1, 40)

##################################################################################
#FORMATTING TABLE 9d
##################################################################################

ws=wb.worksheets()[25]
ws.set_row(7,height = 30)
ws.set_row(8,height = 30)
ws.set_row(11,height = 30)
ws.set_row(12,height = 30)
ws.set_column(0, 0, 30)
ws.set_column(1, 1, 40)



##################################################################################
#FORMATTING TABLE 10
##################################################################################

ws=wb.worksheets()[26]
ws.set_row(8,height = 30)
ws.set_column(0, 0, 40)




##################################################################################
#FORMATTING TABLE 11a
#################################################################################

ws=wb.worksheets()[27]
ws.set_row(10,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 11b
##################################################################################

ws=wb.worksheets()[28]
ws.set_row(10,height = 30)
ws.set_column(0, 0, 40)

##################################################################################
#FORMATTING TABLE 11b
##################################################################################

ws=wb.worksheets()[29]
ws.set_row(10,height = 30)
ws.set_column(0, 0, 40)


##################################################################################
#FORMATTING TABLE 11d
##################################################################################

ws=wb.worksheets()[30]
ws.set_row(10,height = 30)
ws.set_column(0, 0, 40)

wb.close()
