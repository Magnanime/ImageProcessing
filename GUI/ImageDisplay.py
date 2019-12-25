import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import time as ti


class ImageDisplay:
    global path

    def __init__(self, master_element):
        path = 'GUI/costam.png'
        # Frame dimensions
        self.width = 100
        self.height = 100
        self.set_dimensions(master_element)

        # Open Image
        self.raw_image = Image.open(path)
        self.image = ImageTk.PhotoImage(self.raw_image.resize((self.width, self.height), Image.ANTIALIAS))

        # Image dimensions initialization
        self.im_width = 100
        self.im_height = 100
        self.set_im_dimensions()

        # Display image
        self.panel = tk.Label(master_element, image=self.image)
        self.panel.pack(fill='both', expand=1)

        # Bind to panel for dynamic resolution change
        self.panel.bind('<Configure>', self.update)

    def update(self, event):
        if self.width > event.width + 10 or self.width < event.width - 10:
            self.width = event.width
        if self.height > event.height + 10 or self.height < event.height - 10:
            self.height = event.height
        self.image = ImageTk.PhotoImage(self.raw_image.resize((self.width, self.height), Image.ANTIALIAS))
        self.panel.configure(image=self.image)

    def set_dimensions(self, master_element):
        master_element.update()
        self.width = master_element.winfo_width()
        self.height = master_element.winfo_height()

    def set_im_dimensions(self):
        print(self.image.width())

    def select_image(self):
        path = askopenfilename()
        self.raw_image = Image.open(path)
        self.image = ImageTk.PhotoImage(self.raw_image.resize((self.width, self.height), Image.ANTIALIAS))
        self.panel.configure(image=self.image)
