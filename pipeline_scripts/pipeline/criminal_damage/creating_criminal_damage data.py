
import crimetables as ct
import numpy as np

##################################################################################
#IDENTIFYING ALL VARIABLES USED IN TABLE CREATION
##################################################################################

variables_used = ['ageof1',
                  'ageof2',
                  'ageof3',
                  'ageof4',
                  'ageof5',
                  'ageof12',
                  'anger',
                  'annoy',
                  'anxiety',
                  'c11weighti',
                  'confid',
                  'crying',
                  'damhomh',
                  'damveh_window',
                  'damveh_windscreen',
                  'damveh_lock',
                  'damveh_bodywork',
                  'damveh_slash',
                  'damveh_deflate',
                  'damveh_wingmirror',
                  'damveh_scratch',
                  'damveh_fire',
                  'damveh_catalytic',
                  'damveh_other',
                  'damveh_DK',
                  'damveh_ref',
                  'depress',
                  'fear',
                  'filthome',
                  'filtveh',
                  'hmdmoth',
                  'homewind',
                  'homedoor',
                  'homegraf',
                  'homesoil',
                  'homeoth',
                  'monthid',
                  'newloc1d',
                  'numoff',
                  'offence',
                  'ofsex',
                  'othemot',
                  'respreac',
                  'relate',
                  'score1',
                  'score2',
                  'seeany',
                  'shock',
                  'shedwind',
                  'sheddoor',
                  'shedgraf',
                  'shedsoil',
                  'shedoth',
                  'sleeping',
                  'time1',
                  'time2',
                  'time3',
                  'totaff',
                  'totdamag',
                  'totdam2',
                  'VanHomVe',
                  'vftype',
                  'victarea',
                  'wallgraf',
                  'wallbrke',
                  'walloth',
                  'whatdama',
                  'whatdamg',
                  'whemotk',
                  'whemotl',
                  'when1',
                  'wherhapp',
                  'daylight',
                  'newloc1d',
                  'crime',
                  'ageoff2',
                  'ageoff2f',
                  'ageoff2g',
                   ]
                  
##################################################################################
#READING IN ALL OF THE DATA
##################################################################################

vf_data = ct.reading.read_csv_data_in_directory(r"D:\crimetables\data", variables_used)

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

##################################################################################
#SETTING GENUINE MISSINGS FROM THE DATA
##################################################################################

exclude_years = ["Apr '09 to Mar '10",
                 "Apr '10 to Mar '11",
                 "Apr '11 to Mar '12",
                 "Apr '12 to Mar '13",
                 "Apr '13 to Mar '14"]

exclude_variables = ['damveh_catalytic'                        ]

vf_data.loc[vf_data['financial_year'].isin(exclude_years), exclude_variables] = np.inf
    
##################################################################################
#ADDING UNWEIGHTED BASE FOR ALL CASES
##################################################################################

vf_data['unweighted_base'] = 1

vf_data.to_csv(r'G:\Crime RAP project\Python development script\Tables\Table Development\criminal_damage_data.csv', index = False)
