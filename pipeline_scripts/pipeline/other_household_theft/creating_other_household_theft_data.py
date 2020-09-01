
import crimetables as ct
import numpy as np

##################################################################################
#IDENTIFYING ALL VARIABLES USED IN TABLE CREATION
##################################################################################

variables_used = ['victarea',
                  'wherhapp',
                  'vftype',
                  'c11weighti',
                  'offence',
                  'when1',
                  'time1',
                  'time2',
                  'time3',
                  'monthid',
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
                  'whast_h1',
                  'whast_h2',
                  'whast_h3',
                  'whast_h4',
                  'whast_h5',
                  'whast_h6',
                  'whast_h7',
                  'whast_h8',
                  'whast_h9',
                  'whast_h10',
                  'whast_h11',
                  'whast_h12',
                  'whast_h13',
                  'whast_h14',
                  'whast_h15',
                  'whast_h16',
                  'whast_h17',
                  'whast_h18',
                  'whast_h19',
                  'whast_h20',
                  'whast_h21',
                  'whast_h22',
                  'whast_h23',
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
                 'violentnr1',
                 'violentnr2',
                 'violgrpnr',
                 'respinj',
                 'offrel3',
                 'offrel3a',
                 'offrel3b',
                 'offrel3c',
                 'offrel3d',
                 'offrel3e',
                 'offrel3f',
                 'offrel3g',
                  ]
                  
##################################################################################
#READING IN ALL OF THE DATA
##################################################################################
vf_data = ct.reading.read_csv_data_in_directory(r"D:\crimetables\data", variables_used)

##################################################################################
#CALCULATING FINANCIAL YEAR TO PROVIDE ALL YEARS IN ONE TABLE
##################################################################################

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
        "1920": "Apr '19 to Mar '20",
        })
    
##################################################################################
#SETTING GENUINE MISSINGS FROM THE DATA
##################################################################################

exclude_years = ["Apr '09 to Mar '10",
                 "Apr '10 to Mar '11",
                 "Apr '11 to Mar '12",
                 "Apr '12 to Mar '13",
                 "Apr '13 to Mar '14"
                 ]

exclude_variables = ["whast_h22",
                    "whast_h23"
                    ]

vf_data.loc[vf_data['financial_year'].isin(exclude_years), exclude_variables] = np.inf

##################################################################################
#ADDING UNWEIGHTED BASE FOR ALL CASES
##################################################################################

vf_data['unweighted_base'] = 1


vf_data.to_csv(r'G:\Crime RAP project\Python development script\pipeline\other_household_theft\other_household_theft_data.csv', index = False)
