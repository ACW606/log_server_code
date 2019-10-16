#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:02:51 2019

@author: andrew
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine
import threading

class create_df():
    def __init__(self,dB,table):
        un = #get un from encrypted file for this specific dB
        pw = #get pw from encrypted file for this specific dB
        #engine = create_engine('mysql+pymysql://root:505!R0nman@localhost/Syslog')
        engine = create_engine('mysql+pymysql://' + un + pw + '@localhost/'+ dB)
        #df = pd.read_sql_query('SELECT * FROM SystemEvents', engine)
        self.df = pd.read_sql_query('SELECT * FROM' + table, engine)
        #not sure if I can make a variable for table
        
 
class use_re():
    def __init__(self,df):
        #multithread these ** maybe multithread the call and have these as functions
        srcIP = df['Message'].str.extract(r'(?<= SRC=)(.*)(?= DST)')
        mac = df['MAC'] = df5['Message'].str.extract(r'(?<= MAC=)(.*?)(?= SRC)')
        dstIP = df['dstIP'] = df5['Message'].str.extract(r'(?<= DST=)(.*?)(?= LEN)')

dB = 'Syslog'
table = 'SystemEvents'

df = create_df(dB,table)
#next use this df to regex the message and get MAC,dstIP,direction
use_re(df)
#now use the returned MAC to get the local_hostname

#use the returned dstIP to get the remote_hostname

#blocked or accepted

#what is the location of srcIP and dstIP

#use the returned indicator to determine inbound or outbound


        
        




