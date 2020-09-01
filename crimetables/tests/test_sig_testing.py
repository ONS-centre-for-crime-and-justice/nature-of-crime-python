# -*- coding: utf-8 -*-
import pytest
from crimetables.core.sig_test_function import sig_test_crime

## Test as a function

def test_type_error():
        with pytest.raises(TypeError, match = "Function expects numbers for estimate_1 and estimate_2 which need to be input as integers not strings"):
            sig_test_crime("one", 52, 400, 500, design_1 = 1.2, design_2 = 1.2, threshold = 1.96)
            
        with pytest.raises(TypeError, match = "Function expects numbers for estimate_1 and estimate_2 which need to be input as integers not strings"):
            sig_test_crime(1, "52", 400, 500, design_1 = 1.2, design_2 = 1.2, threshold = 1.96)
         
        with pytest.raises(TypeError, match = "Function expects whole numbers for estimate_1 and estimate_2 which need to be input as integers not strings"):
            sig_test_crime(1, 52, 400.5, 500, design_1 = 1.2, design_2 = 1.2, threshold = 1.96)          
        
        with pytest.raises(TypeError, match = "Function expects whole numbers for estimate_1 and estimate_2 which need to be input as integers not strings"):
            sig_test_crime(1, 52, 400, 500.5, design_1 = 1.2, design_2 = 1.2, threshold = 1.96)
 
        with pytest.raises(TypeError, match = "Function expects whole numbers for estimate_1 and estimate_2 which need to be input as integers not strings"):
            sig_test_crime(1.5, 52, 400, 500, design_1 = 1.2, design_2 = 1.2, threshold = 1.96)
    
        with pytest.raises(TypeError, match = "Function expects whole numbers for estimate_1 and estimate_2 which need to be input as integers not strings"):
            sig_test_crime(1, 52.5, 400, 500, design_1 = 1.2, design_2 = 1.2, threshold = 1.96)           
            