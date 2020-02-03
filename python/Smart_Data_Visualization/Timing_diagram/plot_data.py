from datetime import datetime

class plot_data:
    x_axis_type = 'datetime'
    x_axis_scale = []
    y_axis_scale = []
    x_axis_data = []
    y_axis_data = []
    x_axis_desc = []
    x_axis_date_data = []

    #per_process scale
    x_axis_sub_mod = []

    all_lines = []


    def __init__(self):
        return

    def convert_x_to_date(self):
        # X-axis all timestamp
        for ts in self.x_axis_data:
            self.x_axis_date_data.append(datetime.strptime(ts, "%Y/%m/%d %I:%M:%S.%f"))
        print(self.x_axis_date_data)