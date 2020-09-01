# -*- coding: utf-8 -*-
'''
Creating a additional formatting list containing dictionaries to apply formatting to gptables objects

Can be used to apply consistant formatting to whole rows or columns or single cells.

'''

#########################################################################################################################################
#ADDITIONAL FORMATTING
#########################################################################################################################################
# Additional formatting
# Only columns can be references by name
# Column and row numbers include indexes and column headings
formatting = [
        {"row":
            {"rows": -1,  # Numbers only
             "format": {"bottom":1},
             "include_names": True,
             },
        },
        {"row":
            {"rows": 0,  # Numbers only
             "format": {"top":1},
             "include_names": True,
             },
        }
]

cost_formatting = [
        {"row":
            {"rows": [9,10],  # Numbers only
             "format": {"num_format": "£#,##0"},
             "include_names": True,
             },
        },

]