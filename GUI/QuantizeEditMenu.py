import tkinter as tk
from ImageProcessing import ImageProcessing
import math as mt
import time
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


class QuantizeEditMenu:

    def __init__(self, master_element, image_display_element):
        # Frame dimensions
        self.width = 100
        self.height = 100
        self.set_dimensions(master_element)

        # Main display panel
        self.panel = tk.Frame(master_element, bg='grey')
        self.panel.pack(fill='both', expand=1)
        self.panel.rowconfigure(0, weight=1)
        self.panel.rowconfigure(1, weight=1)
        self.panel.columnconfigure(0, weight=1)
        self.panel.columnconfigure(1, weight=2)
        self.panel.columnconfigure(2, weight=1)

        # Buttons initialization
        # Redo button
        self.redo_btn = tk.Button(self.panel, text='Undo')
        self.redo_btn.grid(row=0, column=0, pady=5, padx=5, sticky='we')

        # Undo button
        self.undo_btn = tk.Button(self.panel, text='Redo')
        self.undo_btn.grid(row=1, column=0, pady=5, padx=5, sticky='we')

        # Apply changes button
        self.apply_btn = tk.Button(self.panel, text='Apply Changes')
        self.apply_btn.grid(row=0, column=2, pady=5, padx=5, sticky='we')

        # Cancel changes button
        self.cancel_btn = tk.Button(self.panel, text='Cancel', command=lambda: self.cancel_changes(image_display_element))
        self.cancel_btn.grid(row=1, column=2, pady=5, padx=5, sticky='we')

        # Quantization level slider
        # Level storing variable
        self.quant_level_var = 0
        self.quant_level_sld = tk.Scale(self.panel, variable=self.quant_level_var,
                                        orient='horizontal', command=lambda x: self.quantize(image_display_element, x))
        self.quant_level_sld.grid(row=1, column=1, pady=5, padx=5, sticky='we')

        # Bind to panel for dynamic resolution change
        master_element.bind('<Configure>', self.update)

    def set_dimensions(self, master_element):
        master_element.update()
        self.width = master_element.winfo_width()
        self.height = master_element.winfo_height()

    def update(self, event):
        if self.width > event.width + 10 or self.width < event.width - 10:
            self.width = event.width
        if self.height > event.height + 10 or self.height < event.height - 10:
            self.height = event.height

    @staticmethod
    def quantize(image_display, level):
        if str(level) == '0':
            ImageProcessing.cancel_changes()
            image_display.update_image()
        else:
            ImageProcessing.quantize_image(mt.ceil((1 - (float(level) / 100)) * 256) + 1)
            image_display.update_image()

    def cancel_changes(self, image_display):
        self.quant_level_sld.set(0)
        ImageProcessing.cancel_changes()
        image_display.update_image()
