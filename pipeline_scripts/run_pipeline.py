# -*- coding: utf-8 -*-

import os
import sys

'''
INSTRUCTIONS:
    
   1. RESTART THE KERNAL BEFORE RUNNING THIS CODE
    
   2. EITHER RUN BY HITTING PLAY OR RUN THROUGH THE ANACONDA PROMPT.

   3. IF YOU ARE RUNNING THIS PIPELINE FOR THE FIRST TIME YOU NEED TO RUN OFF THE DATASETS FOR EACH CRIME TYPE. 
      GO INTO EACH 'run_(crimetype)' IN THE PIPELINE FOLDER AND REMOVE THE '#' FROM THE FIRST FROM STATEMENT.

   4. IF YOU ARE RE-RUNNING YOU DONT NEED TO RUN THE DATA OFF EACH TIME SO CAN # OUT THE LINE PREVIOUSLY UNHASHED.
   
 '''   

current_directory = os.path.dirname(os.path.realpath(__file__))

sys.path.append(current_directory)

from pipeline import run_bicycle_theft
from pipeline import run_household_theft
from pipeline import run_personal_other_theft
from pipeline import run_criminal_damage
from pipeline import run_vehicle_theft