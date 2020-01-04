import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


class ImageProcessing:
    @staticmethod
    def open_image():
        path = askopenfilename()
