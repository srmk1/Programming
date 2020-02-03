import os
import re
from plot_data import plot_data
import sys

class LogStash:
    all_files = []
    plot_info = plot_data()

    def __init__(self):
        return

    def scan_directory(self, folder_path):
        # List all files in directory
        for root, dirs, files in os.walk(folder_path):
            for f in files:
                self.all_files.append(os.path.join(root, f))

    def filter_logs(self, folder_path):
        f_temp = open(folder_path + "/temp.txt", "w")

        for file in self.all_files:
            #Open files
            f = open(file, "r", errors="ignore")

            #Read lines from file
            lines = f.readlines()

            #filter unneccessary lines
            #if line.len <= 0 - filter
            #if line starts anything other than 2018 - filter
            lines_filtered = [line for line in lines
                              if (len(line) > 0
                              and re.search('2018', line.split(' ')[0], re.IGNORECASE)
                              and len(line.split(' ')) > 3)
                              and re.search('ERR', line, re.IGNORECASE)]

            #write filtered lines into new file
            for line in lines_filtered:
                f_temp.write(line)

            #close the files
            f.close()
        f_temp.close()

    def cleanup(self, folder_path):
        if os.path.exists(os.path.join(folder_path, "temp.txt")):
            os.remove(os.path.join(folder_path, "temp.txt"))

    def extract_info(self, folder_path):
        # Read file
        f = open(folder_path + "/temp.txt", "r", errors="ignore")
        lines = f.readlines()

        #self.plot_info.y_axis_scale.append(lines[0].split(' ')[2])
        #  Create a list of all timestamps
        for line in lines:
            if (re.search('2018', line.split(' ')[0], re.IGNORECASE)):
                self.plot_info.x_axis_data.append(line.split(' ')[0] + " " + line.split(' ')[1])
                self.plot_info.y_axis_data.append(line.split(' ')[2])
                self.plot_info.x_axis_desc.append(line.split(' ')[3:])
                self.plot_info.x_axis_sub_mod.append(line.split(' ')[2] + " " +
                                                            line.split(' ')[3])
                self.plot_info.all_lines.append(line)

        #Only unique y_axis_elements
        self.plot_info.y_axis_scale = list(set(self.plot_info.y_axis_data))

        f.close()

    def get_plot_data(self):
        return self.plot_info

    def process_logs(self, folder_path):
        self.scan_directory(folder_path)
        self.filter_logs(folder_path)
        self.scan_directory(folder_path)
        self.extract_info(folder_path)
        self.cleanup(folder_path)

    def dump(self):
        print(self.all_files)
        print(self.plot_info.y_axis_scale)