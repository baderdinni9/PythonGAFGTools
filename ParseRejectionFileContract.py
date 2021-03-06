#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

******************************************************
Parse Contract Rejection Validation Script
******************************************************

"""
__author__ = 'Vasista'
__copyright__ = '2015 AIR Worldwide, Inc.. All rights reserved'
__version__ = '1.0'
__interpreter__ = 'Anaconda - Python 2.7.10 64 bit'
__maintainer__ = 'Vasista'
__email__ = 'skapadia@air-worldwide.com'
__status__ = 'Complete'



# Import standard Python packages and read outfile
import getopt
import sys
import datetime
import warnings
import pandas as pd

warnings.filterwarnings('ignore')

OPTLIST, ARGS = getopt.getopt(sys.argv[1:], [''], ['outfile='])

OUTFILE = None
for o, a in OPTLIST:
    if o == "--outfile":
        OUTFILE = a
    print ("Outfile: " + OUTFILE)

if OUTFILE is None:
    print ('Outfile is not passed')
    sys.exit()

# Import standard Python packages and read outfile
import time
import logging
import multiprocessing as mp
import glob, os


import numpy
import glob, os



def order(frame,var):
    varlist =[w for w in frame.columns if w not in var]
    frame = frame[var+varlist]
    return frame

str1 = "_RejectionFileContract"
TCID = sys.argv[3] #TCID
str4 = "*.txt"
ValID = sys.argv[4]
str5 = TCID + "_Csv_Import_" +  ValID  + str1  + str4
Filename = sys.argv[5]
print(Filename)
os.chdir(Filename)
files = glob.glob(str5)


datacontractnew = pd.DataFrame()
for file in files:
    Filename = file.replace('_'+ ValID,'')
    try:
        datafile = pd.read_csv(file, encoding='utf-16', sep=',')
    except:
        datafile = pd.read_csv(file, encoding='utf-8', sep=',')

datafile.columns = pd.Series(datafile.columns).str.replace(' ', '')

actualcolumns = [r'ContractID',	r'InsuredName',	r'Producer',	r'Underwriter',	r'Branch',	r'ExpiringContract',	r'Status',	r'InceptionDate',	r'ExpirationDate',	r'Perils',	r'LOB',	r'Form',
                 r'Currency',	r'UDF1',	r'UDF2',	r'UDF3',	r'UDF4',	r'UDF5',	r'LayerID',	r'LayerPerils',	r'LimitType',	r'Limit1',	r'LimitA',	r'LimitB',	r'LimitC',	r'LimitD',	r'Limit2',	r'DedAmt1',	r'DedAmt2',	r'AttachmentAmt',	r'DedType',	r'Premium',
                 r'SublimitPerils',	r'SublimitArea',	r'SubLimitLimitType',	r'SublimitDedType',	r'SubLimitOcc',	r'SublimitPart',	r'SublimitLimitA',
                 r'SublimitLimitB',	r'SublimitLimitC',	r'SublimitLimitD',	r'SublimitAttachA',	r'SublimitAttachB',	r'SublimitAttachC',	r'SublimitAttachD',	r'SublimitDedAmt1',	r'SublimitDedAmt2',r'TouchstoneErrorCodes']
columnmissing = set(actualcolumns)-set(datafile.columns)
print(columnmissing)
for column in columnmissing:
    datafile[column] = 0

datacontract = datafile[[r'ContractID',	r'InsuredName',	r'Producer',	r'Underwriter',	r'Branch',	r'ExpiringContract',	r'Status',	r'InceptionDate',	r'ExpirationDate',	r'Perils',
                     r'LOB',	r'Form',	r'Currency',	r'UDF1',	r'UDF2',	r'UDF3',	r'UDF4',	r'UDF5',	r'LayerID',	r'LayerPerils',	r'LimitType',	r'Limit1',	r'LimitA',
                     r'LimitB',	r'LimitC',	r'LimitD',	r'Limit2',	r'DedAmt1',	r'DedAmt2',	r'AttachmentAmt',	r'DedType',	r'Premium',	r'SublimitPerils',	r'SublimitArea',
                     r'SubLimitLimitType',	r'SublimitDedType',	r'SubLimitOcc',	r'SublimitPart',	r'SublimitLimitA',	r'SublimitLimitB',	r'SublimitLimitC',	r'SublimitLimitD',
                     r'SublimitAttachA',	r'SublimitAttachB',	r'SublimitAttachC',	r'SublimitAttachD',	r'SublimitDedAmt1',	r'SublimitDedAmt2',r'TouchstoneErrorCodes']]
datacontract = pd.DataFrame(datacontract)

datacontract['FileName'] = Filename
datacontract = order(datacontract , ['FileName'])
datacontractnew = datacontractnew.append(datacontract)




datacontractnew.to_csv(OUTFILE, sep=',', encoding='utf-8', index=False)