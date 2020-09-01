# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.vehicle_related_theft.cost_stolen.table_7a_cost_stolen import vehicle_cost_stolen_table_7a
from pipeline.vehicle_related_theft.cost_stolen.table_7b_cost_stolen import vehicle_cost_stolen_table_7b
from pipeline.additional_formatting import formatting, cost_formatting

##################################################################################
#Table 7a
##################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_cost_stolen_table_7a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

vehicle_cost_stolen_table_7a["table_label"].replace({
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$2$$$$3$$$$4$$"
        }, inplace=True)
    
vehicle_cost_stolen_table_7a.reset_index(inplace = True)

vehicle_cost_stolen_table_7a = vehicle_cost_stolen_table_7a.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_cost_stolen_table_7a_gptable = gpt.GPTable(
        table = vehicle_cost_stolen_table_7a,
        index_columns = {2: 0},
        title = "Table 7a: Cost of stolen items in incidents of theft of vehicles, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "Respondents were asked to estimate the total cost of items stolen. The mean is affected by the small number of offences with high costs, hence the median (or middle value in the range) is also presented.",
                "3": "Values include all respondents who said an item(s) were stolen, even if the cost was valued at zero.",
                "4": "It is not possible to calculate statistical significance for the median cost.",
                },
        additional_formatting = formatting + cost_formatting
        )

##################################################################################
#Table 7b
##################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################
vehicle_cost_stolen_table_7b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

vehicle_cost_stolen_table_7b["table_label"].replace({
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$2$$$$3$$$$4$$"
        }, inplace=True)
    
vehicle_cost_stolen_table_7b.reset_index(inplace = True)

vehicle_cost_stolen_table_7b = vehicle_cost_stolen_table_7b.drop(['index'], axis = 1)

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

vehicle_cost_stolen_table_7b_gptable = gpt.GPTable(
        table = vehicle_cost_stolen_table_7b,
        index_columns = {2: 0},
        title = "Table 7b: Cost of stolen items in incidents of theft from vehicles, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": "Respondents were asked to estimate the total cost of items stolen. The mean is affected by the small number of offences with high costs, hence the median (or middle value in the range) is also presented.",
                "3": "Values include all respondents who said an item(s) were stolen, even if the cost was valued at zero.",
                "4": "It is not possible to calculate statistical significance for the median cost.",
                },
        additional_formatting = formatting + cost_formatting
        )
