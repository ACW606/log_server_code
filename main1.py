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

class create_df:
   # def __init__(self):
        #un = get un from encrypted file for this specific dB
        #pw = get pw from encrypted file for this specific dB
        #engine = create_engine('mysql+pymysql://root:505!R0nman@localhost/Syslog')
    def db(self,db,table):
        un = 'root'
        pw = '505!R0nman'
        engine = create_engine('mysql+pymysql://' + un +":"+ pw + '@localhost/'+ dB)
        df = pd.read_sql_query('SELECT * FROM ' + table, engine)
        df1 = df[['ReceivedAt','Message']]

        return df1
        
 
class get_Data():

    def srcIP(self,df):
        df['srcIP'] = df['Message'].str.extract(r'(?<= SRC=)(.*)(?= DST)')
    def mac(self,df):
        df['MAC'] = df['Message'].str.extract(r'(?<= MAC=)(.*?)(?= SRC)')
    def dstIP(self,df):
        df['dstIP'] = df['Message'].str.extract(r'(?<= DST=)(.*?)(?= LEN)') 
    def pr_df(self,df):
        print(df.head(5))
          
    def run(self,df):
        t1 = threading.Thread(target=self.srcIP(df))
        t2 = threading.Thread(target=self.mac(df))
        t3 = threading.Thread(target=self.dstIP(df))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        print ("I'm working!!")
      
    def get_df(self):
        return df

class create_df2:
    def modify1 (self,df1):
        df2 = df1[['ReceivedAt','MAC','dstIP']]
        return df2
    def pr_df(self,df2):
        print(df2.head(5))
        
    
        
dB = 'Syslog'
table = 'SystemEvents'

if __name__ == '__main__':
    one = create_df()
    df1 = one.db(dB,table)
   
    d1 = get_Data()
  
    d1.pr_df(df1)
   
    d1.run(df1)
    d1.pr_df(df1)
    
    d2 = create_df2()
    df2 =d2.modify1(df1)
    d2.pr_df(df2)
    
    
        




