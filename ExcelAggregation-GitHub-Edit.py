'''
Title:      ExcelAggregation-GitHub-Edit.py    
Author:     @WallStCrash
Date:       06.10.21
Purpose:    Script to aggregate several excel files into one

Notes:      By using the pandas we don't necessarily need columns
            in the spreadsheets to be in the same order for them 
            to be aggregated successfully which is a nice feature. 
            Including a toy example of two worksheets to be merged
            in the repository to illustrate, along with resulting
            spreadsheet.
'''

import os
import pandas as pd
from pathlib import Path

# Location of excel files to aggregate is called files_to_agg_location
files_to_agg_location = "C:\\Users\\Username\\Directory1\\Directory2"       # change file path to filepath *containing* the files for aggregation
os.chdir(files_to_agg_location)                                             # change your working directory to this 
this_dir = Path(os.getcwd())                                                # Path() will determine whether it is a Windows filepath for example to solve backslash issue

spreadsheets = []
for path in (this_dir).rglob("*.xls*"): # use wildcard * for .xls and .xlsx workbooks
    print(f'Reading {path.name}')
    spreadsheet = pd.read_excel(path)
    spreadsheets.append(spreadsheet)
    
    df = pd.concat(spreadsheets)
    df.info()
    
    df.to_excel(this_dir/"Aggregated.xlsx")



