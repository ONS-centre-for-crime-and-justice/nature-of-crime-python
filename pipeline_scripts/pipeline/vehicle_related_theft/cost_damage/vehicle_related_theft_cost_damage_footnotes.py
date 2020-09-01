# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.cost_damage.table_5_cost_damage import vehicle_cost_damage_table_5
from pipeline.additional_formatting import formatting, cost_formatting

##################################################################################
#Table 5
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_cost_damage_table_5.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

vehicle_cost_damage_table_5["table_label"].replace({
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$1$$$$3$$$$4$$"
        }, inplace=True)
    
vehicle_cost_damage_table_5.reset_index(inplace = True)

vehicle_cost_damage_table_5 = vehicle_cost_damage_table_5.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_cost_damage_table_5_gptable = gpt.GPTable(
        table = vehicle_cost_damage_table_5,
        index_columns = {2: 0},
        title = "Table 5: Cost of damage in incidents of theft of and from vehicles, year ending March 2010 to year ending March 20120 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "Respondents were asked to estimate the total cost of items damaged. The mean is affected by the small number of offences with high costs, hence the median (or middle value in the range) is also presented.",
                "3": "Values include all respondents who said an item(s) were damaged, even if the cost was valued at zero.",
                "4": "It is not possible to calculate statistical significance for the median cost.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting + cost_formatting
        )
