from logstash import LogStash
from config import *
from plot_data import plot_data
from visual_renderer import visual_renderer

#Get plot data from files
logstash_obj = LogStash()
logstash_obj.process_logs(LOGS_DIRECTORY)
plot_info = logstash_obj.get_plot_data()
logstash_obj.dump()

#Convert plot data into required format
plot_info.convert_x_to_date()

#Draw sequence diagram
draw = visual_renderer()
draw.draw_timing_diagram(plot_info)
draw.draw_per_process_timing_diagram(plot_info)
draw.draw_line_diagram(plot_info)