import fitz

from hyper import hp


def pdf2img(file_path, zoom_x=4, zoom_y=4):
    """
    inputs:
        file_path: str
            pdf file path
        zoom_x: float,
            zoom in x direction, default is 4
        zoom_y: float
            zoom in y direction, default is 4
    """

    with fitz.open(file_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            image = page.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))
            image.save(hp.splited_images_path + f"page-{page_num+1}.png")


if __name__ == "__main__":
    pdf2img("example.pdf")
