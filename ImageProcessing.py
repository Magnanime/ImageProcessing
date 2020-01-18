import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import numpy as np


class ImageProcessing:
    path = 'GUI/costam.png'
    original_image = Image.open(path)
    image = original_image
    numpy_array_image = np.array(image)

    @staticmethod
    def open_image():
        ImageProcessing.path = askopenfilename()
        ImageProcessing.original_image = Image.open(ImageProcessing.path)
        ImageProcessing.image = ImageProcessing.original_image

    @staticmethod
    def quantize_image(x):
        ImageProcessing.image = ImageProcessing.original_image.quantize(colors=x, method=2, kmeans=0, palette=None)

    @staticmethod
    def apply_changes():
        ImageProcessing.original_image = ImageProcessing.image

    @staticmethod
    def cancel_changes():
        ImageProcessing.image = ImageProcessing.original_image

    @staticmethod
    def image_to_numpy_array():
        ImageProcessing.numpy_array_image = np.array(ImageProcessing.original_image)

