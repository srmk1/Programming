#V20 Statergy
# - Applicable on V40, V40Next and V200
# - Use 1D candel stick chart
# - Invest no more than 3% of total portfolio in one trade
# - No stoploss
# - Statergy has 4 steps (use 1 day chart) for V40, V40Next:
#    -> A bunch of continuous green candels without any red candel between
#    -> Movement from lowest low to highest high should be more than 20%
#    -> In future if the price touches lowest low price then BUY
#    -> When the price touches highest high price then SELL"
#- Statergy has 4 steps (use 1 day chart) for V200:
#    -> A bunch of continuous green candels without any red candel between
#    -> All the green candels should be below 200 Moving avarage 
#    -> Movement from lowest low to highest high should be more than 20%
#    -> In future if the price touches lowest low price then BUY
#    -> When the price touches highest high price then SELL"

import yfinance as yf

# Define a dictionary of lists of stock ticker symbols
stocks = {
    "V40": ["LUXIND.NS", "INFY.NS", "BAJAJ-AUTO.NS","NAM-INDIA.NS","AXISBANK.NS",
            "LIQUIDBEES.NS", "GOLDBEES.NS", "BANKBEES.NS", "NIFTYBEES.NS", "GILLETTE.NS",
            "PIDILITIND.NS", "PFIZER.NS", "SANOFI.NS", "GLAXO.NS", "ABBOTINDIA.NS",
            "HCLTECH.NS", "TCS.NS", "HAVELLS.NS", "WHIRLPOOL.NS", "PAGEIND.NS",
            "BATAINDIA.NS", "TITAN.NS", "AKZOINDIA.NS", "BERGEPAINT.NS", "ASIANPAINT.NS",
            "ITC.NS", "NESTLEIND.NS", "DABUR.NS", "BRITANNIA.NS", "HINDUNILVR.NS",
            "COLPAL.NS", "MARICO.NS", "PGHH.NS", "HDFCAMC.NS", "ICICIPRULI.NS",
            "BAJAJFINSV.NS", "HDFCLIFE.NS", "ICICIGI.NS", "BAJFINANCE.NS", "HDFC.NS",
            "KOTAKBANK.NS", "ICICIBANK.NS", "HDFCBANK.NS"],
    "V40Next": ["BAJAJ-AUTO.NS", "VIPIND.NS", "VINATIORGA.NS", "VGUARD.NS", "MCDOWELL-N.NS",
                "UJJIVANSFB.NS", "UJJIVAN.NS", "TTKPRESTIG.NS", "TEAMLEASE.NS", "TASTYBITE.NS",
                "SYMPHONY.NS", "SUNTV.NS", "SFL.NS", "RELAXO.NS", "RAJESHEXPO.NS",
                "RADICO.NS", "POLYCAB.NS", "OFSS.NS", "MCX.NS", "LALPATHLAB.NS",
                "KANSAINER.NS", "JCHAC.NS", "HONAUT.NS", "GODREJCP.NS", "FINEORG.NS",
                "FINCABLES.NS", "ERIS.NS", "EQUITAS.NS", "EICHERMOT.NS", "DIXON.NS",
                "CERA.NS", "CAPLIPOINT.NS", "BOSCHLTD.NS", "BAYERCROP.NS", "BAJAJHLDNG.BO",
                "AVANTIFEED.NS", "ASTRAZEN.NS", "3MINDIA.NS"],
}

# Open a file for writing the output
with open("stock_percent_moves.txt", "w") as outfile:
    # Write the header row to the file
    outfile.write("Sector,Symbol,Date,Percent Move\n")
    # Loop through each sector
    for list, symbols in stocks.items():
        # Loop through each stock symbol in the sector
        for symbol in symbols:
            # Create a Ticker object for the stock
            ticker = yf.Ticker(symbol)
            # Get the historical stock data for the past 5 days
            data = ticker.history(period="720d")
            # Calculate the percentage price move for each day
            percent_moves = ((data['Close'] - data['Open']) / data['Open']) * 100
            num_days_green_candle = 0
            total_swing_percentage = 0

            for i in range(len(data)):
                if round(percent_moves[i], 2) < 0:
                    if (total_swing_percentage >= 20.0):
                        outfile.write("{},{},{},{}\n".format(list,symbol, data.index[i].strftime('%Y-%m-%d'), round(total_swing_percentage, 2)))
                        #cursor.execute("INSERT INTO stock_prices (list, symbol, date, price_move) VALUES (?, ?, ?, ?)",(list, symbol, data.index[i].strftime('%Y-%m-%d'), round(total_swing_percentage, 2)))
                    num_days_green_candle = 0
                    total_swing_percentage = 0
                else:
                    num_days_green_candle = num_days_green_candle + 1
                    total_swing_percentage = total_swing_percentage + round(percent_moves[i], 2)
