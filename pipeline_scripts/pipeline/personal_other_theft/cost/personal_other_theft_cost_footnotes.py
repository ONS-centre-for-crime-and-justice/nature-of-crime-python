# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.personal_other_theft.cost.table_4a_cost import personal_theft_cost_table_4a
from pipeline.personal_other_theft.cost.table_4b_cost import other_personal_theft_cost_table_4b

from pipeline.additional_formatting import formatting, cost_formatting

##########################################################################################
#cost table 4a
#############################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

personal_theft_cost_table_4a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)


personal_theft_cost_table_4a["table_label"].replace({
        "No cost":"No cost$$2$$",
        "Mean cost": "Mean cost$$3$$",
        "Median cost": "Median cost$$3$$$$4$$$$5$$",
        }, inplace=True)

personal_theft_cost_table_4a.reset_index(inplace=True) 
personal_theft_cost_table_4a = personal_theft_cost_table_4a.drop(['index'], axis = 1) 

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

personal_theft_cost_gptable_4a = gpt.GPTable(
        table = personal_theft_cost_table_4a,
        index_columns = {2: 0},
        title = "Table 4a: Cost of stolen items in incidents of theft from the person, year ending March 2010 to year ending March 2020 CSEW",
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

##########################################################################################
#cost table 4b
#############################################################################################
##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

other_personal_theft_cost_table_4b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)


other_personal_theft_cost_table_4b["table_label"].replace({
        "No cost":"No cost$$2$$",
        "Mean cost": "Mean cost$$3$$",
        "Median cost": "Median cost$$3$$$$4$$$$5$$",
        }, inplace=True)

other_personal_theft_cost_table_4b.reset_index(inplace=True) 
other_personal_theft_cost_table_4b = other_personal_theft_cost_table_4b.drop(['index'], axis = 1) 

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

other_personal_theft_cost_gptable_4b = gpt.GPTable(
        table = other_personal_theft_cost_table_4b,
        index_columns = {2: 0},
        title = "Table 4b: Cost of stolen items in incidents of other theft of personal property, year ending March 2010 to year ending March 2020 CSEW",
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
