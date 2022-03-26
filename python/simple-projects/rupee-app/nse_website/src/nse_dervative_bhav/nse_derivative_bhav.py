from fileinput import filename
import xlwings as xw
import pandas as pd
import re
import os
import sys
import requests
import zipfile
import streamlit as st
from datetime import datetime
from database.nse_database import *

# This File has apis to downloads the bhavcopy from the below link:
# https://www1.nseindia.com/content/historical/DERIVATIVES/2022/FEB/fo11FEB2022bhav.csv.zip
# unzips the file, loads into the database

# References:
# https://github.com/naveen7v/Bhavcopy/blob/master/Bhavcopy.py
# https://pandas.pydata.org/docs/reference/frame.html
# https://docs.streamlit.io/library/api-reference/

interested_stocks = ['NIFTY', 'BANKNIFTY', 'MIDCPNIFTY', 'FINNIFTY',
                    'SBIN', 'HDFCBANK', 'KOTAKBANK', 'ICICIBANK', 'YESBANK', 'BAJFINANCE', 'EDELWEISS',
                    'INFY', 'WIPRO', 'TCS', 'PAYTM', 'ZOMATO', 'CDSL', 'CAMS', 'ROUTE', 'TANLA', 'HAPPSTMNDS', 'POLICYBZR',
                    'COALINDIA', 'MAITHANALL', 'SARDAEN',
                    'EIDPARRY', 'BALRAMCHIN', 'PRAJIND',
                    'HEROMOTOCO', 'NTPC', 'POWERGRID', 'RELIANCE', 'NATIONALUM', 'SBCL', 'TVSMOTOR', 'BAJAJ-AUTO', 'GRINDWELL', 'CARBORUNIV', 'TIMETECHNO', 'COSMOFILMS', 'JINDALPOLY', 'UFLEX', 'POLYPLEX',
                    'TATAELXSI', 'HINDALCO', 'HINDCOPPER', 'FIEMIND', 'SUPRAJIT', 'MINDAIND', 'MOTHERSUMI', 'TATVA', 'NEOGEN', 'TATACHEM',
                    'NTPC', 'IOC', 'KABRAEXTRU', 'EXIDEIND', 'AMARAJABAT', 'JBMA', 'OLECTRA']

def get_url():
    base_url = 'https://www1.nseindia.com/content/historical/DERIVATIVES/'

    # current_date = date = datetime.now().day
    current_date = 11
    current_month = datetime.now().strftime("%b").upper()
    current_year = datetime.now().year

    zip_filename = "fo" + str(current_date)+ current_month+ str(current_year)+ "bhav.csv.zip"

    # url: https://www1.nseindia.com/content/historical/DERIVATIVES/2022/FEB/fo11FEB2022bhav.csv.zip
    url_name = base_url + str(current_year) + "/" + current_month + "/" + zip_filename
    return url_name

def get_zip_csv_path():
    # Globals
    cwd = os.getcwd()
    zip_dir = os.path.join(cwd, "nse_website/data/zip/")
    csv_dir = os.path.join(cwd, "nse_website/data/csv/")
    
    # current_date = date = datetime.now().day
    current_date = 11
    current_month = datetime.now().strftime("%b").upper()
    current_year = datetime.now().year

    # fo11FEB2022bhav.csv.zip
    zip_filename = "fo" + str(current_date)+ current_month+ str(current_year)+ "bhav.csv.zip"
    csv_filename = "fo" + str(current_date)+ current_month+ str(current_year)+ "bhav.csv"
    zip_fullpath = os.path.join(zip_dir, zip_filename)
    csv_fullpath = os.path.join(csv_dir, csv_filename)

    return zip_fullpath, csv_fullpath, csv_dir

def download_option_bhavcopy_from_nse(url_name, zip_fullpath, csv_dir):
    while True:
        try:
            a=requests.get(url_name)
        except requests.ConnectionError:
            print('No connection, retrying')
        break

    if a.status_code==200:
        handle_download(a, zip_fullpath, csv_dir)

def handle_download(a, zip_fullpath, csv_dir):
    print(zip_fullpath)
    bhavcopy_download = open(zip_fullpath, 'wb+')
    bhavcopy_download.write(a.content)
    bhavcopy_download.close()
    bhavcopy_zip_file = zipfile.ZipFile(zip_fullpath, 'r')
    bhavcopy_zip_file.extractall(csv_dir)
    bhavcopy_zip_file.close()

def remove_files(zip_fullpath, csv_fullpath):
    os.remove(zip_fullpath)
    os.remove(csv_fullpath)
 
def read_and_upload_to_db(csv_fullpath):
    update_nse_derivative_bhav_data_table(csv_fullpath)

def update_nse_derivative_bhav_data_table(csv_fullpath):
    book = xw.Book(csv_fullpath)
    sheet = book.sheets[0]
    data = sheet['A1'].expand().options(pd.DataFrame).value

    (db_conn, db_cursor) = connect_to_db()

    for (der_type, values) in zip(data.index, data.values):
        if values[0] in interested_stocks:
            name = values[0]
            expiry = values[1]
            option_type = values[3]
            strike_price = values[2]

            # Primary key String will be of pattern "OPTIDXNIFTY13-APR-2022PE17650"
            # option type will be XX for futures
            primary_key = der_type + name + str(expiry)[0:10].upper() + option_type + str(strike_price)[:-2]
            insert_into_nse_derivative_bhav_data(db_conn, db_cursor, primary_key, values)

    book.save()
    book.close()
    close_db(db_conn)

def update_daily_derivative_table():
    url_name = get_url()
    zip_fullpath, csv_fullpath, csv_dir = get_zip_csv_path()
    download_option_bhavcopy_from_nse(url_name, zip_fullpath, csv_dir)
    read_and_upload_to_db(csv_fullpath)
    remove_files(zip_fullpath, csv_fullpath)

def create_front_end():    
    (db_conn, db_cursor) = connect_to_db()
    der_types = ['None', 'FUTURES', 'OPTIONS']
    option = st.sidebar.selectbox("Derivative Type", der_types)

    if (option == 'FUTURES'):
        indx_type = ['None', 'INDEX', 'STOCKS']
        type = st.sidebar.selectbox("TYPE", indx_type)

        if type == 'INDEX':
            unique_fut_index = get_unique_fut_index(db_conn)
            index = st.sidebar.selectbox("Indices", unique_fut_index)

            fut_index_expiries = get_fut_index_expiries(db_conn, index)
            expiry_date = st.sidebar.selectbox("Expiry Dates", fut_index_expiries)

            expiry_data_frame = get_expiry_data_frame(db_conn, index, expiry_date)
            st.dataframe(expiry_data_frame)

        if type == 'STOCKS':
            unique_fut_index = get_unique_fut_stocks(db_conn)
            stock = st.sidebar.selectbox("Stocks", unique_fut_index)

create_front_end()