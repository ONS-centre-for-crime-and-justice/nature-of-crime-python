# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.other_household_theft.cost.table_3a_cost import household_theft_cost_table_3a
from pipeline.other_household_theft.cost.table_3b_cost import household_theft_cost_table_3b
from pipeline.other_household_theft.cost.table_3c_cost import household_theft_cost_table_3c

from pipeline.additional_formatting import formatting

#########################################################################################################################################
#COST TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

household_theft_cost_table_3a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

household_theft_cost_table_3a["table_label"].replace({
        "No cost":"No cost$$2$$",
        "Mean cost": "Mean cost$$3$$",
        "Median cost": "Median cost$$3$$$$4$$$$5$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_cost_table_3a_gptable = gpt.GPTable(
        table = household_theft_cost_table_3a,
        index_columns = {2: 0},
        title = "Table 3a: Cost of stolen items in incidents of other household theft, year ending March 2010 to year ending March 2020 CSEW",
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
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT IN A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################


household_theft_cost_table_3b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

household_theft_cost_table_3b["table_label"].replace({
        "No cost":"No cost$$2$$",
        "Mean cost": "Mean cost$$3$$",
        "Median cost": "Median cost$$3$$$$4$$$$5$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_cost_table_3b_gptable = gpt.GPTable(
        table = household_theft_cost_table_3b,
        index_columns = {2: 0},
        title = "Table 3b: Cost of stolen items in incidents of other household theft in the dwelling, year ending March 2010 to year ending March 2020 CSEW",
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
        additional_formatting = formatting
        )

############################################################################################################
#HOUSEHOLD THEFT OUTSIDE A DWELLING
############################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################


household_theft_cost_table_3c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

household_theft_cost_table_3c["table_label"].replace({
        "No cost":"No cost$$2$$",
        "Mean cost": "Mean cost$$3$$",
        "Median cost": "Median cost$$3$$$$4$$$$5$$",
        }, inplace=True)

##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

household_theft_cost_table_3c_gptable = gpt.GPTable(
        table = household_theft_cost_table_3c,
        index_columns = {2: 0},
        title = "Table 3c: Cost of stolen items in incidents of household theft outside the dwelling, year ending March 2010 to year ending March 2020 CSEW",
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
        additional_formatting = formatting
        )
