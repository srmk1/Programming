from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.palettes import brewer
from plot_data import plot_data
from bokeh.transform import linear_cmap, factor_cmap
from bokeh.palettes import Spectral6, Category20_20, Inferno256, Greys256
import re
from datetime import datetime

class visual_renderer:

    #bokeh.palettes Category20_20 + Category20b_20 + Category20c_20
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

    def draw_timing_diagram(self, plot):
        # plot the
        output_file("categorical.html")

        #desc would be required for the hover tooltip
        source = ColumnDataSource(data=dict(
                x=plot.x_axis_date_data,
                y=plot.y_axis_data,
                desc=plot.x_axis_desc,
            ))

        #https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#basic-tooltips
        TOOLTIPS = [
                #("index", "$index"),
                #("(x,y)", "($x, $y)"),
                ("desc", "@desc"),
        ]

        #for different y axis entries use different color
        colors = factor_cmap('y', palette=self.Category20_20_custom, factors=plot.y_axis_scale)

        p = figure(plot_width=1600, plot_height=800,
                y_range=plot.y_axis_scale,
                x_axis_type='datetime',
                toolbar_location="below",
                tools=['hover', 'pan', 'xzoom_in', 'xzoom_out', 'xwheel_zoom', "crosshair"],
                tooltips=TOOLTIPS)

        #p.scatter(plot.x_axis_date_data, plot.y_axis_data,
            #          size=10, fill_color="orange", line_color="green", line_width=1)
        p.circle('x', 'y',
                  size=10, fill_color=colors, line_color="black", line_width=1,
                  source=source)

        show(p)

    def draw_line_diagram(self, plot):
        output_file("categorical2.html")

        x_axis_data1 = []
        x_axis_date_data1 = []
        y_axis_data1 = []
        x_axis_desc1 = []
        # desc would be required for the hover tooltip
        for line in plot.all_lines:
            if (re.search("cman_fp", line, re.IGNORECASE) or
                    re.search("iomd", line, re.IGNORECASE)):
                x_axis_data1.append(line.split(' ')[0] + " " + line.split(' ')[1])
                y_axis_data1.append(line.split(' ')[2])
                x_axis_desc1.append(line.split(' ')[3:])

        for ts in x_axis_data1:
            x_axis_date_data1.append(datetime.strptime(ts, "%Y/%m/%d %I:%M:%S.%f"))

        #https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#basic-tooltips
        TOOLTIPS = [
                #("index", "$index"),
                #("(x,y)", "($x, $y)"),
                ("desc", "@desc"),
        ]


        p = figure(plot_width=1600, plot_height=800,
                    y_range=list(set(y_axis_data1)),
                    x_axis_type='datetime',
                    toolbar_location="below",
                    tools=['hover', 'pan', 'xzoom_in', 'xzoom_out', 'xwheel_zoom', "crosshair"],
                    tooltips=TOOLTIPS)
        source1 = ColumnDataSource(data=dict(
            x=x_axis_date_data1,
            y=y_axis_data1,
            desc=x_axis_desc1
        ))

        colors = factor_cmap('y', palette=self.Category20_20_custom, factors=list(set(y_axis_data1)))
        #p.line('x', 'y', source=source1)
        p.circle('x', 'y',
                 fill_color=colors, line_color="black", line_width=1,
                 size=10, radius=500, source=source1)

        show(p)


    def draw_per_process_timing_diagram(self, plot):
        # plot the
        output_file("categorical1.html")

        # desc would be required for the hover tooltip
        source = ColumnDataSource(data=dict(
                x=plot.x_axis_date_data,
                y=plot.x_axis_sub_mod,
                desc=plot.x_axis_desc,
            ))

        # https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#basic-tooltips
        TOOLTIPS = [
                # ("index", "$index"),
                # ("(x,y)", "($x, $y)"),
                ("desc", "@desc"),
            ]

        # for different y axis entries use different color
        colors = factor_cmap('y', palette=self.Category20_20_custom, factors=list(set(plot.x_axis_sub_mod)))

        p = figure(plot_width=1600, plot_height=3200,
                       y_range=list(set(plot.x_axis_sub_mod)),
                       x_axis_type='datetime',
                       toolbar_location="below",
                       tools=['hover', 'pan', 'xzoom_in', 'xzoom_out', 'xwheel_zoom', "crosshair"],
                       tooltips=TOOLTIPS)

            # p.scatter(plot.x_axis_date_data, plot.y_axis_data,
            #          size=10, fill_color="orange", line_color="green", line_width=1)
        p.scatter('x', 'y',
                fill_color=colors, line_color="black", line_width=1,
                size=10, radius=500, source=source)

        show(p)

