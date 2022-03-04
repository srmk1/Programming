# %%
from pynse import *
import datetime
import matplotlib.pyplot as plt
import mplfinance as mpf

nse = Nse()
# %%
bhavcopy_full = nse.bhavcopy(series='all')
# %%
bhavcopy_full = bhavcopy_full.reset_index(level=1)
# %%
bhavcopy_eq = bhavcopy_full[bhavcopy_full['SERIES'] == 'EQ']
# %%
bhavcopy_eq = bhavcopy_eq[['OPEN_PRICE', 'HIGH_PRICE',
                           'LOW_PRICE', 'CLOSE_PRICE', 'TTL_TRD_QNTY',
                           'DELIV_QTY', 'DELIV_PER']]

# %%
bhavcopy_eq = bhavcopy_eq.astype(float, errors='raise')

# %%
nifty_50_list = nse.symbols[IndexSymbol.Nifty50.name]
# %%
bhavcopy_eq = bhavcopy_eq[bhavcopy_eq.index.isin(nifty_50_list)]
# %%
# trading_days=nse.get_hist(from_date=datetime.date(2020,1,1)).index
# trading_days=list(trading_days.map(lambda x: x.date()))
# %%


def stock_deliv_data(symbol, from_date: datetime.date = None, to_date: datetime.date = None):
    trading_days = nse.get_hist(from_date=from_date, to_date=to_date).index
    trading_days = list(trading_days.map(lambda x: x.date()))
    data = pd.DataFrame()

    for date in trading_days:
        try:
            bhav = nse.bhavcopy(date).loc[symbol]
            bhav.set_index('DATE1', inplace=True)
            data = data.append(bhav)
        except Exception as e:
            print(f'error {e} for {date}')

    data = data.astype(float)
    data.index = data.index.map(pd.to_datetime)
    data = data[['OPEN_PRICE', 'HIGH_PRICE',
                 'LOW_PRICE', 'CLOSE_PRICE', 'TTL_TRD_QNTY',
                 'DELIV_QTY', 'DELIV_PER']]

    data.columns = 'open high low close volume deliv_qty deliv_per'.split()
    return data


data = stock_deliv_data('HDFC', from_date=datetime.date(2021, 1, 1))
deliv_data = [mpf.make_addplot(data['deliv_per'], panel=2)]
mpf.plot(data, addplot=deliv_data, type='candle', style='yahoo', volume=True)
# %%
deliv_data = [mpf.make_addplot(data['deliv_per'], panel=2, mav=5)]
mpf.plot(data, addplot=deliv_data, type='candle', style='yahoo', volume=True)

# %%
# candlesticks patterns

engulfing_pattern = talib.CDLENGULFING(
    data.open, data.high, data.low, data.close).replace(0, np.nan)

bull_engulf = engulfing_pattern.replace(-100, np.nan)/100
bear_engulf = engulfing_pattern.replace(100, np.nan)/100

deliv_data = [mpf.make_addplot(data['deliv_per'], panel=2, mav=5),
              mpf.make_addplot(bull_engulf*data.low*0.95,
                               type='scatter', marker='^', color='green'),
              mpf.make_addplot(-bear_engulf*data.high*1.05, type='scatter',
                               marker='v', color='red')
              ]
mpf.plot(data, addplot=deliv_data, type='candle', style='yahoo', volume=True)

# %%
# oi data


def stock_oi_data(symbol, from_date: datetime.date = None, to_date: datetime.date = None):
    trading_days = nse.get_hist(from_date=from_date, to_date=to_date).index
    trading_days = list(trading_days.map(lambda x: x.date()))
    data = pd.DataFrame()

    for date in trading_days:
        try:
            bhav = nse.bhavcopy_fno(date).loc[symbol]
            bhav = bhav[bhav['INSTRUMENT'].isin(['FUTSTK', 'FUTIDX'])]
            expiry_list = list(bhav['EXPIRY_DT'].sort_values())
            current_expiry = expiry_list[0]

            bhav['DATE'] = bhav['TIMESTAMP'].apply(
                lambda x: datetime.datetime.strptime(x, "%d-%b-%Y").date())
            bhav = bhav[bhav['EXPIRY_DT'] == current_expiry]

            bhav.set_index('DATE', inplace=True)
            data = data.append(bhav)
        except Exception as e:
            print(f'error {e} for {date}')

    data = data[['EXPIRY_DT',  'OPEN', 'HIGH', 'LOW', 'CLOSE', 'CONTRACTS', 'OPEN_INT',
                 'CHG_IN_OI']]

    data.columns = [col.lower() for col in data.columns]
    data.index = data.index.map(pd.to_datetime)

    return data


data = stock_oi_data('NIFTY', from_date=datetime.date(2020, 5, 1))


# %%
oi_plots = [mpf.make_addplot(data['open_int'], panel=1)]
mpf.plot(data, addplot=oi_plots, type='candle', style='yahoo')

# %%
trading_days = nse.get_hist().index
trading_days = list(trading_days.map(lambda x: x.date()))
day_1 = trading_days[-1]
day_2 = trading_days[-7]
bhav_1 = nse.bhavcopy_fno(day_1)
bhav_2 = nse.bhavcopy_fno(day_2)

# filter data for futures
bhav_1 = bhav_1[bhav_1['INSTRUMENT'].isin(['FUTSTK', 'FUTIDX'])]
bhav_2 = bhav_2[bhav_2['INSTRUMENT'].isin(['FUTSTK', 'FUTIDX'])]

group_bhav_1 = bhav_1.groupby(bhav_1.index)
group_bhav_2 = bhav_2.groupby(bhav_2.index)
current_expiry_1 = group_bhav_1['EXPIRY_DT'].min()
current_expiry_2 = group_bhav_2['EXPIRY_DT'].min()

bhav_1['current_expiry'] = current_expiry_1
bhav_2['current_expiry'] = current_expiry_2

bhav_1 = bhav_1[bhav_1['EXPIRY_DT'] == bhav_1['current_expiry']]
bhav_2 = bhav_2[bhav_2['EXPIRY_DT'] == bhav_2['current_expiry']]

pch_oi = group_bhav_1['OPEN_INT'].sum()/group_bhav_2['OPEN_INT'].sum()-1
pch_close = bhav_1['CLOSE']/bhav_2['CLOSE']-1

builtup = pd.DataFrame({'pch_close': pch_close, 'pch_oi': pch_oi})

builtup.plot(kind='scatter', x='pch_close', y='pch_oi', figsize=(20, 10))
plt.axvline(x=0, color='black', lw=2)
plt.axhline(y=0, color='black', lw=2)

for symbol in builtup.index:
    plt.annotate(
        symbol, (builtup.loc[symbol]['pch_close'],
                 builtup.loc[symbol]['pch_oi']), color='b',
        size=6)

plt.title(f'Futures Builtup {day_2} to {day_1}')
# %%

# Option Chain recreation
bhavcopy_fno = nse.bhavcopy_fno()
options_data = bhavcopy_fno[bhavcopy_fno['INSTRUMENT'].isin(
    ['OPTSTK', 'OPTIDX'])]

# %%
symbol = 'NIFTY'

options_grouped = options_data.groupby(options_data.index)
current_expiry = options_grouped['EXPIRY_DT'].min()[symbol]

options_data = options_data.loc[symbol]
options_data = options_data[options_data['EXPIRY_DT'] == current_expiry]
options_data.set_index(options_data['STRIKE_PR'], inplace=True)
# %%

options_data = options_data[['STRIKE_PR', 'OPTION_TYP', 'OPEN', 'HIGH',
                             'LOW', 'CLOSE', 'CONTRACTS', 'OPEN_INT',
                             'CHG_IN_OI']]

call_data = options_data[options_data['OPTION_TYP'] == 'CE']
put_data = options_data[options_data['OPTION_TYP'] == 'PE']
# %%
option_chain = pd.concat([call_data, put_data], keys=['CALL', 'PUT'], axis=1)

# %%


def bhavcopy_to_optionchain(symbol, date: datetime.date):
    bhavcopy_fno = nse.bhavcopy_fno(date)

    options_data = bhavcopy_fno[bhavcopy_fno['INSTRUMENT'].isin(
        ['OPTSTK', 'OPTIDX'])]
    options_grouped = options_data.groupby(options_data.index)

    current_expiry = options_grouped['EXPIRY_DT'].min()[symbol]

    options_data = options_data.loc[symbol]
    options_data = options_data[options_data['EXPIRY_DT'] == current_expiry]
    options_data.set_index(options_data['STRIKE_PR'], inplace=True)

    options_data = options_data[['STRIKE_PR', 'OPTION_TYP', 'OPEN', 'HIGH',
                                 'LOW', 'CLOSE', 'CONTRACTS', 'OPEN_INT',
                                 'CHG_IN_OI']]
    call_data = options_data[options_data['OPTION_TYP'] == 'CE']
    put_data = options_data[options_data['OPTION_TYP'] == 'PE']

    futures_data = bhavcopy_fno[bhavcopy_fno['INSTRUMENT'].isin(
        ['FUTSTK', 'FUTIDX'])].loc[symbol]

    futures_price = futures_data[futures_data['EXPIRY_DT']
                                 == futures_data['EXPIRY_DT'].min()].CLOSE[0]

    atm_strike = abs(options_data['STRIKE_PR']-futures_price).idxmin()

    return call_data, put_data, futures_price, atm_strike


def support_resistance(symbol, date: datetime.date):
    option_chain_data = bhavcopy_to_optionchain(
        symbol, date)

    return option_chain_data[0]['OPEN_INT'].idxmax(), option_chain_data[1]['OPEN_INT'].idxmax()


symbol = 'NIFTY'
date = datetime.date(2021, 5, 10)
sr = support_resistance(symbol, date)

option_chain_data = bhavcopy_to_optionchain(
    'NIFTY', datetime.date(2021, 5, 10))

option_chain_data[0]['OPEN_INT'].plot(kind='barh', color='r', figsize=(8, 10))
option_chain_data[1]['OPEN_INT'].plot(kind='barh', color='g')
plt.title(f'{symbol},{date},{sr}')

# %%
# put call ratio

trading_days = nse.get_hist(from_date=datetime.date(2021, 1, 1)).index
trading_days = list(trading_days.map(lambda x: x.date()))
pcr_data = pd.DataFrame()

symbol = 'NIFTY'
for date in trading_days:
    try:
        option_chain_data = bhavcopy_to_optionchain(symbol, date)
        pcr = option_chain_data[1]['OPEN_INT'].sum(
        )/option_chain_data[0]['OPEN_INT'].sum()
        price = option_chain_data[2]
        pcr_data = pcr_data.append(
            pd.Series({'close': price, 'pcr': pcr}, name=date))
    except Exception as e:
        print(f"error for {date}")

# %%
pcr_data.index = pcr_data.index.map(pd.to_datetime)
# %%
pcr_data.close.plot()
plt.show()
pcr_data.pcr.plot()

# %%
# max pain


def point_loss(call_data, put_data, strike):
    itm_calls = call_data[call_data['STRIKE_PR'] < strike]
    itm_puts = put_data[put_data['STRIKE_PR'] > strike]

    call_loss = (strike-itm_calls['STRIKE_PR'])*itm_calls['OPEN_INT']
    put_loss = (itm_puts['STRIKE_PR']-strike)*itm_puts['OPEN_INT']

    return call_loss.sum()+put_loss.sum()


loss = call_data['STRIKE_PR'].apply(
    lambda x: point_loss(call_data, put_data, x))

# %%
loss.plot()
plt.axvline(x=loss.idxmin(), color='r')
# %%