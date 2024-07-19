import os
from typing import Dict, List

import fitz

from hyper import hp


def delete_files_in_folder(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        os.remove(file_path)


def pdf2images(file_path, zoom_x=hp.zoom_x, zoom_y=hp.zoom_y):
    """
    inputs:
        file_path: str
            pdf file path
        zoom_x: float,
            zoom in x direction, default is 4
        zoom_y: float
            zoom in y direction, default is 4
    example:
        pdf2images("example.pdf")
    """

    with fitz.open(file_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            image = page.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))
            image.save(hp.images_saved_path + f"{page_num}.png")
