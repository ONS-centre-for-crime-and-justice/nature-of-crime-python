# -*- coding: utf-8 -*-
##################################################################################
#READING IN ALL NECESSARY PACKAGES
##################################################################################
import crimetables as ct
import numpy as np

##################################################################################
#IDENTIFYING ALL VARIABLES USED IN TABLE CREATION
##################################################################################

variables_used = ['victarea',
                  'wherhapp',
                  'vftype',
                  'vehtheft',
                  'c11weighti',
                  'offence',
                  'when1',
                  'time1',
                  'time2',
                  'time3',
                  'monthid',
                  'newloc1d',
                  'totvalue',
                  'valveh',
                  'valvehx',
                  'respreac',
                  'totaff',
                  'anger',
                  'shock',
                  'fear',
                  'sleeping',
                  'crying',
                  'depress',
                  'anxiety',
                  'confid', 
                  'annoy',
                  'othemot',
                  'cartheft',
                  'vehage',
                  'vehdam2',
                  'vehfound',
                  'vehtheft',
                  'vehstole',
                  'valstol',
                  'electric',
                  'hifi',
                  'cartele',
                  'tools',
                  'bike',
                  'camera',
                  'cdtapedvd',
                  'hhitems',
                  'foodcigs',
                  'Hkeys',
                  'Ckeys',
                  'extfit',
                  'tyres',
                  'othervp',
                  'fuel',
                  'garden',
                  'glasses',
                  'otherst',
                  'howbrc_noca',
                  'howbrc_nocb',
                  'howbrc_nocc',
                  'howbrc_nocd',
                  'howbrc_noce',
                  'howbrc_nocf',
                  'howbrc_nocg',
                  'howbrc_noch',
                  'howbrc_noci',
                  'howbrc_nocj',
                  'htryca3',
                  'totdamag',
                  'totdamx',
                  'vehtht2',
                  'totvalux',
                  'score1',
                  'score2',
                  'vcentlo', 
                  'vcarala', 
                  'vimmobm', 
                  'vimmobe', 
                  'vanyimob', 
                  'vvtrack',
                  'valid_item_stolen_NoC',
                  'whemotk',
                  'whemotl',
                  'daylight',
                  'crime'
                  ]
                  
##################################################################################
#READING IN ALL OF THE DATA
##################################################################################


vf_data = ct.reading.read_csv_data_in_directory(r"D:\repos\crime-tables-python\data", variables_used)

vf_data['year_code'] = vf_data['monthid'].apply(ct.mapping.to_financial_year)

vf_data['financial_year'] = vf_data["year_code"].replace({
        "0910": "Apr '09 to Mar '10",
        "1011": "Apr '10 to Mar '11",
        "1112": "Apr '11 to Mar '12",
        "1213": "Apr '12 to Mar '13",
        "1314": "Apr '13 to Mar '14",
        "1415": "Apr '14 to Mar '15",
        "1516": "Apr '15 to Mar '16",
        "1617": "Apr '16 to Mar '17",
        "1718": "Apr '17 to Mar '18",
        "1819": "Apr '18 to Mar '19",
        "1920": "Apr '19 to Mar '20"
        })

#Exculding years where questions were not asked
exclude_years = ["Apr '09 to Mar '10",
                 "Apr '10 to Mar '11",
                 "Apr '11 to Mar '12",
                 "Apr '12 to Mar '13",
                 "Apr '13 to Mar '14",
                 "Apr '14 to Mar '15",
                 "Apr '15 to Mar '16",
                 "Apr '16 to Mar '17",
                 "Apr '17 to Mar '18"]

exclude_variables = ['howbrc_noch']


vf_data.loc[vf_data['financial_year'].isin(exclude_years), exclude_variables] = np.inf 

##################################################################################
#ADDING UNWEIGHTED BASE FOR ALL CASES
##################################################################################

vf_data['unweighted_base'] = 1

##################################################################################
#SAVING DATASET TO CSV
##################################################################################

vf_data.to_csv(r'G:\Crime RAP project\Python development script\pipeline\vehicle_related_theft\vehicle_theft_data.csv', index = False)
