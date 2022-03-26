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
import calendar
from database.nse_database import *

# This file has apis to track FII/DII movements in derivative world
# Participant wise Trading Volumes (csv)
# https://www1.nseindia.com/content/nsccl/fao_participant_vol_11022022.csv
# Participant wise Open Interest (csv)
# https://www1.nseindia.com/content/nsccl/fao_participant_oi_11022022.csv


def download_option_participant_volume_from_nse(url_name, csv_fullpath):
    while True:
        try:
            a=requests.get(url_name)
        except requests.ConnectionError:
            print('No connection, retrying')
        break

    if a.status_code==200:
        handle_download(a, csv_fullpath)


def get_participant_volume_url():
    base_url = 'https://www1.nseindia.com/content/nsccl/fao_participant_vol_'

    # current_date = date = datetime.now().day
    current_date = str(datetime.now().date)
    current_month = datetime.now().strftime("%b").upper()
    current_year = str(datetime.now().year)
    date = current_date + current_month + current_year
    # https://www1.nseindia.com/content/nsccl/fao_participant_vol_11022022.csv
    url_name = base_url + date + ".csv"
    return url_name

def get_participant_oi_url():
    base_url = 'https://www1.nseindia.com/content/nsccl/fao_participant_oi_'

    # current_date = date = datetime.now().day
    current_date = str(datetime.now().date)
    current_month = datetime.now().strftime("%b").upper()
    current_year = str(datetime.now().year)
    date = current_date + current_month + current_year
    # https://www1.nseindia.com/content/nsccl/fao_participant_oi_11022022.csv
    url_name = base_url + date + ".csv"
    return url_name

def handle_download(a, csv_fullpath):
    bhavcopy_download = open(csv_fullpath, 'wb+')
    bhavcopy_download.write(a.content)
    bhavcopy_download.close()
    
#### Participant OI Related ####
def get_oi_csv_path(curr_date, curr_month, curr_year):
    # why this path? check
    # https://stackoverflow.com/questions/39604876/using-xlwings-to-open-an-excel-file-on-mac-os-x-el-capitan-requires-grant-access/39635243#39635243
    csv_dir = "/Users/srmk/Library/Containers/com.microsoft.Excel/Data/rupee-app-data/csv"
    
    # fo11FEB2022bhav.csv.zip
    csv_filename = "fao_participant_oi" + curr_date + curr_month + curr_year + ".csv"
    csv_fullpath = os.path.join(csv_dir, csv_filename)

    return csv_fullpath

def get_participant_oi_url(curr_date, curr_month, curr_year):
    # https://www1.nseindia.com/content/nsccl/fao_participant_oi_11022022.csv
    base_url = 'https://www1.nseindia.com/content/nsccl/fao_participant_oi_'
    url_name = base_url + curr_date + curr_month + curr_year + ".csv"
    return url_name

def download_option_participant_oi_from_nse(url_name, csv_fullpath):
    while True:
        try:
            a=requests.get(url_name)
        except requests.ConnectionError:
            print('No connection, retrying')
        break
    
    print(a.status_code)
    if a.status_code==200:
        print("succcess")
        handle_oi_download(a, csv_fullpath)
        return 0
    if a.status_code==404:
        print("File not found")
        return -1

def handle_oi_download(a, csv_fullpath):
    bhavcopy_download = open(csv_fullpath, 'wb+')
    bhavcopy_download.write(a.content)
    bhavcopy_download.close()

def nse_derivative_participant_oi_data_table(csv_fullpath, curr_date, curr_month, curr_year):
    xw.App().visible = False
    book = xw.Book(csv_fullpath)
    sheet = book.sheets[0]
    data = sheet['A2'].expand().options(pd.DataFrame).value

    (db_conn, db_cursor) = connect_to_db()
    temp_string = "" + curr_date + calendar.month_abbr[curr_month] + curr_year

    for (client_type, values) in zip(data.index, data.values):
        insert_into_participant_oi_data(db_conn, db_cursor, client_type, temp_string, values)

    book.save()
    book.close()
    xw.App().quit()
    close_db(db_conn)

def update_daily_participant_oi_table():
    for current_month in range(1,3):
        curr_month = '{:02d}'.format(current_month)
        for curr_date in range(1,31):
            curr_date = '{:02d}'.format(curr_date)
            url_name = get_participant_oi_url(str(curr_date), str(curr_month), str(2022))
            print(url_name)
            participant_ui_csv_fullpath = get_oi_csv_path(str(curr_date), str(curr_month), str(2022))
            ret_value = download_option_participant_oi_from_nse(url_name, participant_ui_csv_fullpath)
            if (ret_value == 0):
                nse_derivative_participant_oi_data_table(participant_ui_csv_fullpath, str(curr_date), current_month, str(2022))
                os.remove(participant_ui_csv_fullpath)

#update_daily_participant_oi_table()

#### Participant OI Related - END ####

def calculate_oi_percentage_change(results):
    # Need to calculate of % change w.r.t previous values
    # Add a column with previous values
    results['prev_long'] = results['future_index_long'].shift()
    results['Fut long % change'] = (results['future_index_long'] - results['prev_long']) * 100 / results['prev_long']
    # Delete the previous values column
    results.drop('prev_long', axis=1, inplace=True)

    # Need to calculate of % change w.r.t previous values
    # Add a column with previous values
    results['prev_short'] = results['future_index_short'].shift()
    results['Fut Short % change'] = (results['future_index_short'] - results['prev_short']) * 100 / results['prev_short']
    # Delete the previous values column
    results.drop('prev_short', axis=1, inplace=True)

    # Need to calculate of % change w.r.t previous values
    # Add a column with previous values
    results['prev_long'] = results['option_index_call_long'].shift()
    results['Call long % change'] = (results['option_index_call_long'] - results['prev_long']) * 100 / results['prev_long']
    # Delete the previous values column
    results.drop('prev_long', axis=1, inplace=True)

    # Need to calculate of % change w.r.t previous values
    # Add a column with previous values
    results['prev_short'] = results['option_index_call_short'].shift()
    results['Call Short % change'] = (results['option_index_call_short'] - results['prev_short']) * 100 / results['prev_short']
    # Delete the previous values column
    results.drop('prev_short', axis=1, inplace=True)

    # Need to calculate of % change w.r.t previous values
    # Add a column with previous values
    results['prev_long'] = results['option_index_put_long'].shift()
    results['Put long % change'] = (results['option_index_put_long'] - results['prev_long']) * 100 / results['prev_long']
    # Delete the previous values column
    results.drop('prev_long', axis=1, inplace=True)

    # Need to calculate of % change w.r.t previous values
    # Add a column with previous values
    results['prev_short'] = results['option_index_put_short'].shift()
    results['Put Short % change'] = (results['option_index_put_short'] - results['prev_short']) * 100 / results['prev_short']
    # Delete the previous values column
    results.drop('prev_short', axis=1, inplace=True)

    return results

def prepare_derivative_participant_oi_data_to_excel():
    (db_conn, db_cursor) = connect_to_db()
    results = get_oi_fii_index(db_conn)
    results = calculate_oi_percentage_change(results)

# def create_front_end():    
#     (db_conn, db_cursor) = connect_to_db()    
#     st.header("FII Future Index")
#     st.text("Long future is a position when somebody buys a future.")
#     st.text("Shorting future is a position when somebody selling a future.")
#     fii_fut = get_oi_fii_fut_index(db_conn)
#     st.dataframe(fii_fut, width=1000, height=200)
#     st.header("FII Call Index")
#     st.text("Long call is a position when somebody buys a call option.")
#     st.text("Shorting call is a position when somebody selling a call option.")
#     fii_call = get_oi_fii_call_option(db_conn)
#     st.dataframe(fii_call, width=1000, height=200)  
#     st.header("FII Put Index")
#     st.text("Long put is a position when somebody buys a put option.")
#     st.text("Shorting put is a position when somebody selling a put option.")
#     fii_put = get_oi_fii_put_option(db_conn)
#     st.dataframe(fii_put, width=1000, height=200)
#
# create_front_end()

def prepare_participant_oi_to_excel():
    (db_conn, db_cursor) = connect_to_db()