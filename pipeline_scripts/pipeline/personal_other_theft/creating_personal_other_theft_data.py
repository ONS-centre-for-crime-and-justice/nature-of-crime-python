

import crimetables as ct
import numpy as np


##################################################################################
#IDENTIFYING ALL VARIABLES USED IN TABLE CREATION
##################################################################################

variables_used = ['rowlabel',
                  'victarea',
                  'wherhapp',
                  'vftype',
                  'c11weighti',
                  'offence',
                  'when1',
                  'time1',
                  'time2',
                  'time3',
                  'monthid',
                  'newloc1b',
                  'newloc1c',
                  'whast_pt1',
                  'whast_pt2',
                  'whast_pt3',
                  'whast_pt4',
                  'whast_pt5',
                  'whast_pt6',
                  'whast_pt7',
                  'whast_pt8',
                  'whast_pt9',
                  'whast_pt10',
                  'whast_pt11',
                  'whast_pt12',
                  'whast_pt13',
                  'whast_pt14',
                  'whast_pt15',
                  'whast_pt16',
                  'whast_pt17',   
                  'totvalue',
                  'totval2',
                  'whemotk',
                  'whemotl',
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
                  'score1',
                  'score2',
                  'daylight',
                  'crime',
                 'seeany',
                 'numoff',
                 'vftype',
                 'ofsex',
                 'ageoff2',
                 'ageoff2',
                 'ageoff2f',
                 'ageoff2g',
                 'ageof12',
                 'ageof1',
                 'ageof2',
                 'ageof3',
                 'ageof4',
                 'ageof5',
                 'relate',                            
                  ]
                  
##################################################################################
#READING IN ALL OF THE DATA
##################################################################################
vf_data = ct.reading.read_csv_data_in_directory(r"D:\crimetables\data", variables_used)

##################################################################################
#CALCULATING FINANCIAL YEAR TO PROVIDE ALL YEARS IN ONE TABLE
##################################################################################

vf_data['year_code'] = vf_data['monthid'].apply(ct.mapping.to_financial_year)


vf_data["financial_year"] = vf_data["year_code"] .replace({
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
        "1920": "Apr '19 to Mar '20"})
    
    


##################################################################################
#SETTING GENUINE MISSINGS FROM THE DATA
##################################################################################

exclude_years = ["Apr '09 to Mar '10",
                 "Apr '10 to Mar '11",
                 "Apr '11 to Mar '12",
                 "Apr '12 to Mar '13",
                 "Apr '13 to Mar '14"
                 ]

exclude_variables = ["whast_pt16",
                    "whast_pt17"
                    ]

vf_data.loc[vf_data['financial_year'].isin(exclude_years), exclude_variables] = np.inf

##################################################################################
#ADDING UNWEIGHTED BASE FOR ALL CASES
##################################################################################

vf_data['unweighted_base'] = 1



vf_data.to_csv(r'G:\Crime RAP project\Python development script\pipeline\personal_other_theft\personal_other_theft_data.csv', index = False)




