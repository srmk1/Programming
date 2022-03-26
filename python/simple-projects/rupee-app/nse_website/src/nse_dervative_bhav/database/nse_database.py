import sqlite3
import pandas as pd

def connect_to_db():
    connection = sqlite3.connect("nse_website_db")
    cursor = connection.cursor()
    return connection, cursor

def insert_into_nse_derivative_bhav_data(conn, cursor, derivative_key, values):
    derivative_type = derivative_key[0:2]
    symbol = values[0]
    expiry_date = str(values[1])[0:10].upper()
    option_type = values[3]
    strike_price = values[2]
    open_price = values[4]
    high_price = values[5]
    low_price = values[6]
    close_price = values[7]
    settle_pr = values[8]
    contracts = values[9]
    val_inlakh = values[10]
    open_interest = values[11]
    change_in_oi = values[12]
    timestamp = str(values[13])[0:10].upper()

    cursor.execute("""
            INSERT OR IGNORE INTO nse_derivative_bhav_data 
             (derivative_key, derivative_type, symbol, option_type, expiry_date, strike_price,
             open_price, close_price, low_price, high_price,
             settle_pr, contracts, val_inlakh, open_interest, change_in_oi, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (derivative_key, derivative_type, symbol, option_type, expiry_date, strike_price,
                open_price, close_price, low_price, high_price,
                settle_pr, contracts, val_inlakh, open_interest, change_in_oi, timestamp))
    
    conn.commit()

def get_unique_index_symbols(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    symbols = c.execute('SELECT DISTINCT symbol FROM nse_derivative_bhav_data WHERE derivative_key LIKE \'%IDX%\';').fetchall()
    c.close()
    return symbols

def get_unique_stock_symbols(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    symbols = c.execute('SELECT DISTINCT symbol FROM nse_derivative_bhav_data WHERE derivative_key LIKE \'%STK%\';').fetchall()
    c.close()
    return symbols

def get_unique_fut_index(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    der_types = c.execute('SELECT DISTINCT symbol FROM nse_derivative_bhav_data WHERE derivative_type LIKE \'%FU%\''
        'AND derivative_key LIKE \'%IDX%\';').fetchall()
    c.close()
    return der_types

def get_unique_fut_stocks(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    der_types = c.execute('SELECT DISTINCT symbol FROM nse_derivative_bhav_data WHERE derivative_type LIKE \'%FU%\''
        'AND derivative_key LIKE \'%STK%\';').fetchall()
    c.close()
    return der_types

def get_fut_index_expiries(conn, index):
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    der_types = c.execute('SELECT DISTINCT expiry_date FROM nse_derivative_bhav_data WHERE symbol LIKE \'%'
    + index + '%\' AND derivative_key LIKE \'%IDX%\';').fetchall()
    c.close()
    return der_types

def get_expiry_data_frame(conn, index, expiry_date):
    # check https://datatofish.com/sql-to-pandas-dataframe/
    c = conn.cursor()
    #der_types = c.execute('SELECT * FROM nse_derivative_bhav_data WHERE symbol LIKE \'%'
    #+ index + '%\' AND derivative_key LIKE \'%IDX%\';')
    query = c.execute("SELECT * From nse_derivative_bhav_data")
    cols = [column[0] for column in query.description]
    results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    print(results)


def insert_into_participant_oi_data(conn, cursor, client_type, temp_date, values):
    print(temp_date)
    client_type = client_type
    future_index_long = values[0]
    future_index_short = values[1]
    future_stock_long = values[2]
    future_stock_short = values[3]
    option_index_call_long = values[4]
    option_index_put_long = values[5]
    option_index_call_short = values[6]
    option_index_put_short = values[7]
    option_stock_call_long = values[4]
    option_stock_put_long = values[5]
    option_stock_call_short = values[6]
    option_stock_put_short = values[7]

    cursor.execute("""
            INSERT OR IGNORE INTO nse_derivative_participant_oi_data 
             (client_type, future_index_long, future_index_short, future_stock_long, future_stock_short,
             option_index_call_long, option_index_put_long, option_index_call_short, option_index_put_short,
             option_stock_call_long, option_stock_put_long, option_stock_call_short, option_stock_put_short,
             timestamp)
            VALUES (?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, 
                    ?, ?, ?, ?, 
                    ?)
        """, (client_type, future_index_long, future_index_short, future_stock_long, future_stock_short,
             option_index_call_long, option_index_put_long, option_index_call_short, option_index_put_short,
             option_stock_call_long, option_stock_put_long, option_stock_call_short, option_stock_put_short,
             temp_date))
    
    conn.commit()


def get_oi_fii_index(conn):
    c = conn.cursor()
    c.execute("""SELECT option_index_put_short ,option_index_put_long, "
        "option_index_call_long, option_index_call_short, future_index_long, "
        "future_index_short, timestamp "
        "FROM nse_derivative_participant_oi_data WHERE client_type LIKE \'%FII%\'""")

    # Convert the database query to dataframe
    col_names = [description[0] for description in c.description]
    results= pd.DataFrame.from_records(data = c.fetchall(), columns = col_names)

    # convert the 'Date' column to datetime format
    results['timestamp'] = pd.to_datetime(results['timestamp'], )
    # Set index to timestamp
    results = results.set_index('timestamp')

    c.close()
    return results

# def get_oi_fii_call_option(conn):
#     c = conn.cursor()
#     c.execute("""SELECT option_index_call_long, option_index_call_short, timestamp FROM nse_derivative_participant_oi_data WHERE client_type LIKE \'%FII%\'""")
#     # Convert the database query to dataframe
#     col_names = [description[0] for description in c.description]
#     results= pd.DataFrame.from_records(data = c.fetchall(), columns = col_names)

#     # convert the 'Date' column to datetime format
#     results['timestamp'] = pd.to_datetime(results['timestamp'], )
#     # Set index to timestamp
#     results = results.set_index('timestamp')

#     # Need to calculate of % change w.r.t previous values
#     # Add a column with previous values
#     results['prev_long'] = results['option_index_call_long'].shift()
#     results['Call long % change'] = (results['option_index_call_long'] - results['prev_long']) * 100 / results['prev_long']
#     # Delete the previous values column
#     results.drop('prev_long', axis=1, inplace=True)

#     # Need to calculate of % change w.r.t previous values
#     # Add a column with previous values
#     results['prev_short'] = results['option_index_call_short'].shift()
#     results['Call Short % change'] = (results['option_index_call_short'] - results['prev_short']) * 100 / results['prev_short']
#     # Delete the previous values column
#     results.drop('prev_short', axis=1, inplace=True)

#     c.close()
#     return results

# def get_oi_fii_put_option(conn):
    # c = conn.cursor()
    # c.execute("""SELECT option_index_put_long, option_index_put_short, timestamp FROM nse_derivative_participant_oi_data WHERE client_type LIKE \'%FII%\'""")
    # # Convert the database query to dataframe
    # col_names = [description[0] for description in c.description]
    # results= pd.DataFrame.from_records(data = c.fetchall(), columns = col_names)

    # # convert the 'Date' column to datetime format
    # results['timestamp'] = pd.to_datetime(results['timestamp'], )
    # # Set index to timestamp
    # results = results.set_index('timestamp')

    # # Need to calculate of % change w.r.t previous values
    # # Add a column with previous values
    # results['prev_long'] = results['option_index_put_long'].shift()
    # results['Put long % change'] = (results['option_index_put_long'] - results['prev_long']) * 100 / results['prev_long']
    # # Delete the previous values column
    # results.drop('prev_long', axis=1, inplace=True)

    # # Need to calculate of % change w.r.t previous values
    # # Add a column with previous values
    # results['prev_short'] = results['option_index_put_short'].shift()
    # results['Put Short % change'] = (results['option_index_put_short'] - results['prev_short']) * 100 / results['prev_short']
    # # Delete the previous values column
    # results.drop('prev_short', axis=1, inplace=True)

    # c.close()
    # return results

def close_db(db_conn):
    db_conn.close()
