import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import time as ti


class ImageDisplay:

    def __init__(self, master_element):
        self.path = 'GUI/costam.png'
        # Frame dimensions
        self.width = 100
        self.height = 100
        self.panel_x_to_y_ratio = 1
        self.set_dimensions(master_element)

        # Open Image
        self.raw_image = Image.open(self.path)

        # Image dimensions initialization
        self.im_width = 100
        self.im_height = 100
        self.im_x_to_y_ratio = 1
        self.set_im_dimensions()

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
        self.set_im_dimensions()
        self.image = ImageTk.PhotoImage(self.raw_image.resize((int(self.im_width), int(self.im_height)), Image.ANTIALIAS))
        self.panel.configure(image=self.image)

    def set_dimensions(self, master_element):
        master_element.update()
        self.width = master_element.winfo_width()
        self.height = master_element.winfo_height()

    def set_im_dimensions(self):
        # Image x to y ratio
        self.im_x_to_y_ratio = self.raw_image.size[0] / self.raw_image.size[1]

        # Image x to y to panel x to y ratio
        if (self.raw_image.size[0] / self.raw_image.size[1]) <= (self.width / self.height):
            self.im_height = self.height
            self.im_width = self.im_height * self.im_x_to_y_ratio
        else:
            self.im_width = self.width
            self.im_height = self.im_width / self.im_x_to_y_ratio

    def select_image(self):
        self.path = askopenfilename()
        self.raw_image = Image.open(self.path)
        self.set_im_dimensions()
        self.image = ImageTk.PhotoImage(self.raw_image.resize((int(self.im_width), int(self.im_height)), Image.ANTIALIAS))
        self.panel.configure(image=self.image)
