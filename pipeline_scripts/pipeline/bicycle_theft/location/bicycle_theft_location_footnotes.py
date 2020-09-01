# -*- coding: utf-8 -*-

import gptables as gpt

from pipeline.bicycle_theft.location.table_2_location import bicycle_location_table_2
from pipeline.additional_formatting import formatting

#########################################################################################################################################
#LOCATION TABLE
#########################################################################################################################################

##################################################################################
#ADDING FOOTNOTES - AMENDING TABLE LABELS TO INCORPORATE '$$X$$' AS THIS SIGNIFIES A FOOTNOTE.
##################################################################################

bicycle_location_table_2.rename(columns={
         "Latest year compared with Mar 10" : "Latest year compared with Mar 10$$2$$",
         "Latest year compared with Mar 19" :  "Latest year compared with Mar 19$$2$$"
         }, inplace=True)

bicycle_location_table_2["table_label"].replace({
        "Home - Semi-private":"Home - Semi-private$$3$$",
        "Other - Grounds of a public place": "Other - Grounds of a public place$$4$$",
        }, inplace=True)

bicycle_location_table_2.reset_index(inplace=True) 
bicycle_location_table_2 = bicycle_location_table_2.drop(['index'], axis = 1) 
    
##################################################################################
#RUNNING FINAL DATAFRAM THROUGH GPTABLES PACKAGE
##################################################################################

bicycle_location_gptable_2 = gpt.GPTable(
        table = bicycle_location_table_2,
        index_columns = {2: 0},
        title = "Table 2: Where incidents of bicycle theft occurred, year ending March 2010 to year ending March 2020 CSEW$$1$$",
        subtitles = ["Household incidents, percentages"],
        scope = "England and Wales",
        units = "",
        source = "Source: Office for National Statistics - Crime Survey for England and Wales",
        annotations = {
                "1": "Due to changes in the year ending March 2013 questionnaire and year ending March 2018 questionnaire, data cannot be compared to earlier years. As a result, no significance testing is available for the year ending March 2020 compared with the year ending March 2010.",
                "2": "Statistically significant change at the 5% level is indicated by an asterisk. For more information on statistical significance, see Chapter 8 of the User Guide.",
                "3": "'Semi-private' includes outside areas on the premises and garages or car parks around but not connected to the home.",
                "4": "Data not available prior to the year ending March 2013. Grounds of a public place includes: shop, supermarket, shopping centre or precinct; school, college or university; pub, bar or working mens club; place of entertainment; nightclub; sports centre; football ground.",
                },
        notes = [": denotes not applicable"],
        additional_formatting = formatting
        )
