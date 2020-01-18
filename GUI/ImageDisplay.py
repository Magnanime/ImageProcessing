import tkinter as tk
from ImageProcessing import ImageProcessing
from PIL import ImageTk, Image
import time as ti


class ImageDisplay:

    def __init__(self, master_element):
        # Frame dimensions
        self.width = 100
        self.height = 100
        self.panel_x_to_y_ratio = 1
        self.set_dimensions(master_element)

        # Open Image
        # This is only a image that will be displayed. The real image file is stored in ImageProcessing class.
        self.raw_image = ImageProcessing.image

        # Image dimensions initialization
        # Variables are used to set the right ratio and dimensions of displayed image
        self.im_width = 100
        self.im_height = 100
        self.im_x_to_y_ratio = 1
        self.set_im_display_dimensions()

        # Display image
        self.image = ImageTk.PhotoImage(self.raw_image.resize((int(self.im_width), int(self.im_height)), Image.ANTIALIAS))
        self.panel = tk.Label(master_element, image=self.image, bg='grey')
        self.panel.pack(fill='both', expand=1)

        # Bind to panel for dynamic resolution change
        master_element.bind('<Configure>', self.update)

    def update(self, event):
        if self.width > event.width + 10 or self.width < event.width - 10:
            self.width = event.width
        if self.height > event.height + 10 or self.height < event.height - 10:
            self.height = event.height
        self.set_im_display_dimensions()
        self.update_image()

    def set_dimensions(self, master_element):
        master_element.update()
        self.width = master_element.winfo_width()
        self.height = master_element.winfo_height()
        self.panel_x_to_y_ratio = self.width / self.height

    def set_im_display_dimensions(self):
        # Image x to y ratio
        self.im_x_to_y_ratio = self.raw_image.size[0] / self.raw_image.size[1]

        # Image x to y to panel x to y ratio
        if self.im_x_to_y_ratio <= self.panel_x_to_y_ratio:
            self.im_height = self.height
            self.im_width = self.im_height * self.im_x_to_y_ratio
        else:
            self.im_width = self.width
            self.im_height = self.im_width / self.im_x_to_y_ratio

    def select_image(self):
        ImageProcessing.open_image()
        self.raw_image = ImageProcessing.image
        self.set_im_display_dimensions()
        self.update_image()

    def update_image(self):
        self.raw_image = ImageProcessing.image
        self.image = ImageTk.PhotoImage(self.raw_image.resize((int(self.im_width), int(self.im_height)), Image.ANTIALIAS))
        self.panel.configure(image=self.image)
