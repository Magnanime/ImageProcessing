import tkinter as tk
import sys
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import time as ti


class MenuDisplay:

    def __init__(self, master_element, image_display_element):
        # Frame dimensions
        self.width = 100
        self.height = 100
        self.set_dimensions(master_element)

        # Main display panel
        self.panel = tk.Frame(master_element, bg='grey')
        self.panel.pack(fill='both', expand=1)
        self.panel.rowconfigure(0, weight=1)
        self.panel.columnconfigure(0, weight=1)
        self.panel.columnconfigure(1, weight=1)

        # Display buttons
        # Open image
        self.open_btn = tk.Button(self.panel, text='Open', command=lambda: self.open_image(image_display_element))
        self.open_btn.grid(row=1, column=1, padx=5, pady=5, sticky='we')
        # Save image
        self.save_btn = tk.Button(self.panel, text='Save')
        self.save_btn.grid(row=1, column=0, padx=5, pady=5, sticky='we')
        # About button
        self.about_btn = tk.Button(self.panel, text='About')
        self.about_btn.grid(row=2, column=0, padx=5, pady=5, sticky='we')
        # Quit button
        self.quit_btn = tk.Button(self.panel, text='Quit', command=self.quit)
        self.quit_btn.grid(row=2, column=1, padx=5, pady=5, sticky='we')

        # Bind to panel for dynamic resolution change
        master_element.bind('<Configure>', self.update)

    def update(self, event):
        if self.width > event.width + 10 or self.width < event.width - 10:
            self.width = event.width
        if self.height > event.height + 10 or self.height < event.height - 10:
            self.height = event.height

    def set_dimensions(self, master_element):
        master_element.update()
        self.width = master_element.winfo_width()
        self.height = master_element.winfo_height()

    def open_image(self, image_display_element):
        image_display_element.select_image()

    def quit(self):
        sys.exit(1)