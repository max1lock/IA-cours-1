from src.image_processor import ImageProcessor


def main():
    input_folder = "input_images"
    image_processor = ImageProcessor(input_folder)
    image_processor.process_folder(640)


if __name__ == "__main__":
    main()
