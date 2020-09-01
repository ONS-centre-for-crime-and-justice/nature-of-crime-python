# -*- coding: utf-8 -*-
import gptables as gpt

from pipeline.criminal_damage.cost.table_4a_cost import criminal_damage_cost_table_4a
from pipeline.criminal_damage.cost.table_4b_cost import criminal_damage_cost_table_4b
from pipeline.criminal_damage.cost.table_4c_cost import criminal_damage_cost_table_4c
from pipeline.additional_formatting import formatting, cost_formatting

#########################################################################################################################################
#COST TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_cost_table_4a.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)


criminal_damage_cost_table_4a["table_label"].replace({
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$2$$$$3$$$$4$$",
        }, inplace=True)

criminal_damage_cost_table_4a.reset_index(inplace=True) 
criminal_damage_cost_table_4a = criminal_damage_cost_table_4a.drop(['index'], axis = 1) 

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_cost_gptable_4a = gpt.GPTable(
        table = criminal_damage_cost_table_4a,
        index_columns = {2: 0},
        title = "Table 4a: Cost of incidents of criminal damage, year ending March 2010 to year ending March 2020 CSEW",
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


#########################################################################################################################################
#CRIMINAL DAMAGE TO A VEHICLE.
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_cost_table_4b.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

criminal_damage_cost_table_4b["table_label"].replace({
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$2$$$$3$$$$4$$",
        }, inplace=True)

criminal_damage_cost_table_4b.reset_index(inplace=True) 
criminal_damage_cost_table_4b = criminal_damage_cost_table_4b.drop(['index'], axis = 1) 

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_cost_gptable_4b = gpt.GPTable(
        table = criminal_damage_cost_table_4b,
        index_columns = {2: 0},
        title = "Table 4b: Cost of incidents of criminal damage to a vehicle, year ending March 2010 to year ending March 2020 CSEW",
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

#########################################################################################################################################
#ARSON AND OTHER CRIMINAL DAMAGE.
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

criminal_damage_cost_table_4c.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$1$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$1$$"
         }, inplace=True)

criminal_damage_cost_table_4c["table_label"].replace({
        "Mean cost": "Mean cost$$2$$",
        "Median cost": "Median cost$$2$$$$3$$$$4$$",
        }, inplace=True)

criminal_damage_cost_table_4c.reset_index(inplace=True) 
criminal_damage_cost_table_4c = criminal_damage_cost_table_4c.drop(['index'], axis = 1) 

##################################################################################
#RUNNING FINAL DATAFRAME THROUGH GPTABLES PACKAGE
##################################################################################

criminal_damage_cost_gptable_4c = gpt.GPTable(
        table = criminal_damage_cost_table_4c,
        index_columns = {2: 0},
        title = "Table 4c: Cost of incidents of arson and other criminal damage, year ending March 2010 to year ending March 2020 CSEW",
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
