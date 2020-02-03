from bokeh.plotting import figure, output_file, show
from datetime import datetime
import re

x_new = []
test_new = []
factors_new = []

#### Function for extracting all timestamp entries from a log file ####
def extractEventTimeStamps(filePath):
    # Read file
    lines = list(open(filePath))
    # Filter out empty entries
    lines_filtered = [line for line in lines if len(line) > 0]
    # Create a list of all timestamps
    for line in lines_filtered:
        if (re.search('2018', line.split(' ')[0], re.IGNORECASE)):
            x_new.append(line.split(' ')[0] + " " + line.split(' ')[1])
            test_new.append(line.split(' ')[2])


#Y-axis Modules
factors_new = ["{iomd_1-0}{1}:", "{cman_cc_1}{1}:"]

#data plotting for each modules
#https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
#2018/12/03 08:40:35.389 {iomd_1-0}{1}: [iomd] [12497]: TEXT
extractEventTimeStamps("/Users/srmk/Desktop/iomd_log.txt")
extractEventTimeStamps("/Users/srmk/Desktop/cman_fp_log.txt")

#X-axis all timestamp
x_new_date = []
for ts in x_new:
    x_new_date.append(datetime.strptime(ts, "%Y/%m/%d %I:%M:%S.%f"))

#plot the
output_file("categorical.html")
p = figure(plot_width=1600, plot_height=800,
           y_range=factors_new, x_axis_type='datetime',
           toolbar_location="below",
           tools=['hover', 'pan', 'wheel_zoom', 'xzoom_in', 'xzoom_out', 'xwheel_zoom'])
p.scatter(x_new_date, test_new, size=10, fill_color="orange", line_color="green", line_width=1)
show(p)
