import tkinter as tk
import screeninfo as si
import math as mt
import time
from GUI.ImageDisplay import ImageDisplay as disp


class MainWindow:

    @staticmethod
    def get_monitor_data():
        # Getting monitor data
        monitor_info_raw = si.get_monitors()[0]
        monitor_info_str = str(monitor_info_raw)
        # Determining current used monitor width
        w_index = monitor_info_str.find("width=") + len("width=")
        width = ""
        stoppoint = ""
        while stoppoint != ",":
            width += monitor_info_str[w_index]
            w_index += 1
            stoppoint = monitor_info_str[w_index]
        # Determining current used monitor height
        h_index = monitor_info_str.find("height=") + len("height=")
        height = ""
        stoppoint = ""
        while stoppoint != ",":
            height += monitor_info_str[h_index]
            h_index += 1
            stoppoint = monitor_info_str[h_index]
        return width, height

    def initialize_geometry(self):
        # Setting root start resolution
        self.root.geometry('{0}x{1}+{2}+{3}'.format(str(mt.ceil(float(self.default_x) / 2)),
                                                    str(mt.ceil(float(self.default_y) / 2)),
                                                    str(mt.ceil(float(self.default_x) / 4)),
                                                    str(mt.ceil(float(self.default_y) / 4))))
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=3)
        self.root.rowconfigure(1, weight=1)

    def update(self):
        self.image_frame.update()

    def __init__(self):
        # Root of window
        self.root = tk.Tk()
        # Default screen resolution
        self.default_x = self.get_monitor_data()[0]
        self.default_y = self.get_monitor_data()[1]
        # Initializing geometry
        self.initialize_geometry()
        # Image display frame
        self.image_frame = tk.Frame(self.root, bg='blue',
                                    height=mt.floor(float(self.default_y) * (3 / 8)),
                                    width=mt.floor(float(self.default_x) * (3 / 8)))
        self.image_frame.grid(column=0, row=0, sticky='wens')

        # Menu display frame
        self.menu_frame = tk.Frame(self.root, bg='green',
                                   height=mt.floor(float(self.default_y) * (4 / 8)),
                                   width=mt.floor(float(self.default_x) * (1 / 8)))
        self.menu_frame.grid(column=1, row=0, sticky='wens', rowspan=2)

        # Button display frame
        self.button_frame = tk.Frame(self.root, bg='red',
                                     height=mt.floor(float(self.default_y) * (1 / 8)),
                                     width=mt.floor(float(self.default_x) * (3 / 8)))
        self.button_frame.grid(column=0, row=1, sticky='wens')
        #
        display_image = disp(self.image_frame)
        display_menu = disp(self.menu_frame)
        display_buttons = disp(self.button_frame)
        self.root.mainloop()
