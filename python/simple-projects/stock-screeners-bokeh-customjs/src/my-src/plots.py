from bokeh.plotting import figure, output_file, ColumnDataSource
import collections
from bokeh.io import show
from bokeh.models import Dropdown
from bokeh.layouts import column
from bokeh.models.callbacks import CustomJS
from bokeh.models.widgets import Tabs, Panel

# my own libraries
from nse import nse


class NsePlot:

    # bokeh.palettes Category20_20 + Category20b_20 + Category20c_20
    Category20_20_custom = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896',
                            '#9467bd',
                            '#c5b0d5',
                            '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',
                            '#17becf',
                            '#9edae5',
                            '#393b79', '#5254a3', '#6b6ecf', '#9c9ede', '#637939', '#8ca252', '#b5cf6b', '#cedb9c',
                            '#8c6d31',
                            '#bd9e39',
                            '#e7ba52', '#e7cb94', '#843c39', '#ad494a', '#d6616b', '#e7969c', '#7b4173', '#a55194',
                            '#ce6dbd',
                            '#de9ed6',
                            '#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#e6550d', '#fd8d3c', '#fdae6b', '#fdd0a2',
                            '#31a354',
                            '#74c476',
                            '#a1d99b', '#c7e9c0', '#756bb1', '#9e9ac8', '#bcbddc', '#dadaeb', '#636363', '#969696',
                            '#bdbdbd',
                            '#d9d9d9',
                            '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896',
                            '#9467bd',
                            '#c5b0d5',
                            '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',
                            '#17becf',
                            '#9edae5',
                            '#393b79', '#5254a3', '#6b6ecf', '#9c9ede', '#637939', '#8ca252', '#b5cf6b', '#cedb9c',
                            '#8c6d31',
                            '#bd9e39',
                            '#e7ba52', '#e7cb94', '#843c39', '#ad494a', '#d6616b', '#e7969c', '#7b4173', '#a55194',
                            '#ce6dbd',
                            '#de9ed6',
                            '#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#e6550d', '#fd8d3c', '#fdae6b', '#fdd0a2',
                            '#31a354',
                            '#74c476',
                            '#a1d99b', '#c7e9c0', '#756bb1', '#9e9ac8', '#bcbddc', '#dadaeb', '#636363', '#969696',
                            '#bdbdbd',
                            '#d9d9d9',
                            '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896',
                            '#9467bd',
                            '#c5b0d5',
                            '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',
                            '#17becf',
                            '#9edae5',
                            '#393b79', '#5254a3', '#6b6ecf', '#9c9ede', '#637939', '#8ca252', '#b5cf6b', '#cedb9c',
                            '#8c6d31',
                            '#bd9e39',
                            '#e7ba52', '#e7cb94', '#843c39', '#ad494a', '#d6616b', '#e7969c', '#7b4173', '#a55194',
                            '#ce6dbd',
                            '#de9ed6',
                            '#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#e6550d', '#fd8d3c', '#fdae6b', '#fdd0a2',
                            '#31a354',
                            '#74c476',
                            '#a1d99b', '#c7e9c0', '#756bb1', '#9e9ac8', '#bcbddc', '#dadaeb', '#636363', '#969696',
                            '#bdbdbd',
                            '#d9d9d9'
                            ]

    # Plotting output of
    # https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY
    # data
    # ": [
    # {
    #     "strikePrice": 7500,
    #     "expiryDate": "29-Dec-2022",
    #     "PE": {
    #         "strikePrice": 7500,
    #         "expiryDate": "29-Dec-2022",
    #         "underlying": "NIFTY",
    #         "identifier": "OPTIDXNIFTY29-12-2022PE7500.00",
    #         "openInterest": 21,
    #         "changeinOpenInterest": 0,
    #         "pchangeinOpenInterest": 0,
    #         "totalTradedVolume": 0,
    #         "impliedVolatility": 0,
    #         "lastPrice": 0,
    #         "change": 0,
    #         "pChange": 0,
    #         "totalBuyQuantity": 2550,
    #         "totalSellQuantity": 0,
    #         "bidQty": 750,
    #         "bidprice": 0.3,
    #         "askQty": 0,
    #         "askPrice": 0,
    #         "underlyingValue": 17101.95
    #     }
    # }"
    def plot_index_option_chain_bids(self):
        nse_obj = nse()
        index_option_chain = nse_obj.get_index_option_chain("NIFTY")

############################ Create dictionary of symbol ###############
        # Create a dictionary indexed by date
        bids_per_expiry = collections.defaultdict(list)
        for record in index_option_chain['records']['data']:
            # print(record)
            if 'CE' in record:
                expiry_record = {}
                expiry_record['strikePrice'] = record['strikePrice']
                expiry_record['bidprice'] = record['CE']['bidprice']
                expiry_record['openInterest'] = record['CE']['openInterest']
                expiry_string = str(record['expiryDate'])
                bids_per_expiry[expiry_string].append(expiry_record)

        x = []
        y = []
        desc_rend = []
        oi = []
        for key in bids_per_expiry:
            strike_price_list = []
            bid_price_list = []
            open_interest_list = []
            expiry_date_list = []
            for record in bids_per_expiry[key]:
                strike_price_list.append(record['strikePrice'])
                bid_price_list.append(record['bidprice'])
                open_interest_list.append(record['openInterest'])
                expiry_date_list.append(key)

            x.append(strike_price_list)
            y.append(bid_price_list)
            desc_rend.append(expiry_date_list)
            oi.append(open_interest_list)
############################ Create dictionary of symbol ###############

        output_file("categorical2.html")
        # # https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#basic-tooltips
        TOOLTIPS = [
            ("Expiry Date", "@desc"),
            ("Strike Price", "@xs"),
            ("Bid Price", "@ys")
        ]

############################ Strike-price vs bidprice ###############
        # desc would be required for the hover tooltip
        p = figure(plot_width=500, plot_height=500,
                    toolbar_location="below",
                    tools=['hover', 'pan', 'xzoom_in', 'xzoom_out', 'xwheel_zoom', "crosshair"],
                    tooltips=TOOLTIPS)
        #Store the line-plot and date to provide for drop-down
        menu_renderer = []
        plots_renderer = []
        # plot multiple lines
        for x_data, y_data, desc_data, color in zip(x, y, desc_rend, self.Category20_20_custom):
            print(desc_data)
            source = ColumnDataSource(data=dict(
                    xs=x_data,
                    ys=y_data,
                    desc=desc_data
            ))
            # Append all plots
            plot = p.line('xs', 'ys', color=color, source=source)
            # Append the plot
            plots_renderer.append(plot)
            # Menu populated with the expiry dates
            menu_renderer.append(desc_data[0])

        # Create a dropdown menu with expiry dates
        dropdown = Dropdown(label="Expiry Date", button_type="warning", menu=menu_renderer)
        # To debug this on chrome - right-click + Inspect
        callback = CustomJS(args=dict(plots=plots_renderer, menus=menu_renderer, dp=dropdown), code="""
            for(var i=0; i<plots.length; i++){
                console.log(this.item);
                if (menus[i] == this.item)
                    plots[i].visible = true;
                else
                    plots[i].visible = false;
            }
            dp.label = this.item;
            """)

        dropdown.js_on_event("menu_item_click", callback)
############################ Strike-price vs bidprice ###############

        layout = column(dropdown, p)
        #tab1 = Panel(child=layout, title="This is Tab 1")
        #tab2 = Panel(child=layout, title="This is Tab 2")
        #tabs = Tabs(tabs=[tab1, tab2])
        show(layout)