# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.bicycle_theft.cost.table_3_cost import bicycle_cost_table_3
from pipeline.additional_formatting import formatting, cost_formatting

#########################################################################################################################################
#COST TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

bicycle_cost_table_3.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

bicycle_cost_table_3["table_label"].replace({
        "No cost":"No cost$$2$$",
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$3$$$$4$$$$5$$",
        }, inplace=True)

bicycle_cost_table_3.reset_index(inplace=True) 
bicycle_cost_table_3 = bicycle_cost_table_3.drop(['index'], axis = 1) 

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

bicycle_cost_gptable_3 = gpt.GPTable(
        table = bicycle_cost_table_3,
        index_columns = {2: 0},
        title = "Table 3: Cost of stolen items in incidents of bicycle theft, year ending March 2010 to year ending March 2020 CSEW",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "2": " No cost includes respondents who said no item(s) were stolen.",
                "3": "Respondents were asked to estimate the total cost of items stolen. The mean is affected by the small number of offences with high costs, hence the median (or middle value in the range) is also presented.",
                "4": "Values include all respondents who said an item(s) were stolen, even if the cost was valued at zero.",
                "5": "It is not possible to calculate statistical significance for the median cost.",
                },
        additional_formatting = formatting + cost_formatting
        )


