from PIL import Image, ImageOps
import os
from datetime import datetime


class ImageProcessor:
    def __init__(self, input_folder: str):
        self.input_folder = input_folder
        self.output_folder = os.path.join(
            "dataset", datetime.now().strftime("%Y%m%d%H%M%S")
        )
        os.makedirs(self.output_folder, exist_ok=True)

    def process_folder(self, size: int):
        for filename in os.listdir(self.input_folder):
            image_path = os.path.join(self.input_folder, filename)
            if os.path.isfile(image_path):
                self.process_image(image_path, size)

    def process_image(self, image_path: str, size: int):
        with Image.open(image_path) as img:
            img = self.resize_image(img, size)
            img = self.add_padding(img, size)
            output_path = os.path.join(
                self.output_folder, os.path.basename(image_path)
            )
            img.save(output_path)

    def resize_image(self, img: Image.Image, size: int) -> Image.Image:
        aspect_ratio = img.width / img.height
        if aspect_ratio > 1:
            new_width = size
            new_height = int(size / aspect_ratio)
        else:
            new_width = int(size * aspect_ratio)
            new_height = size
        return img.resize((new_width, new_height))

    def add_padding(self, img: Image.Image, size: int) -> Image.Image:
        padding_color = (114, 114, 144)
        width, height = img.size

        if width == height:
            return img

        if img.mode != "RGB":
            img = img.convert("RGB")

        if width < height:
            # Ajouter à droite
            padding = (0, 0, size - width, 0)
        else:
            # Ajouter en bas
            padding = (0, 0, 0, size - height)

        return ImageOps.expand(img, border=padding, fill=padding_color)
