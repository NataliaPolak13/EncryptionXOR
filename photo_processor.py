from PIL import Image
import os
import io

class PhotoProcessor:
    def __init__(self, script_path):
        self.script_path = script_path

    # Pobieranie zdjęć binarnie do zakodowania
    def get_photo_binary(self, photos_path):
        binary_data_list = []
        for image_file in os.listdir(photos_path):
            image_path = os.path.join(photos_path, image_file)
            try:
                with Image.open(image_path) as image:
                    binary_buffer = io.BytesIO()
                    image.save(binary_buffer, format='JPEG')
                    binary_data = binary_buffer.getvalue()
                    binary_data_list.append(binary_data)
            except Exception as e:
                print(f"Error processing {image}: {e}")

        return binary_data_list

    # Zapisywanie binarne zdjęć do nowego katalogu
    def save_photo(self, images, output_paths):
        saved = []
        for image, output_path in zip(images, output_paths):
            try:
                with open(output_path, 'wb') as file:
                    file.write(image)
                saved.append(output_path)
            except Exception as e:
                print(f"Error saving to {output_path}: {e}")
        return saved

    # Automatyczna detekcja czy deszyfrowany obraz jest poprawnym plikiem - sprawdzanie nagłówka
    def check_image_header(self, image):
        try:
            # Nagłówek pliku JPEG
            jpeg_signature = b'\xFF\xD8\xFF'
            if image.startswith(jpeg_signature):
                print("Decrypted image has a JPG header.")
                return True

            # Nagłówek pliku PNG
            png_signature = b'\x89PNG\r\n\x1a\n'
            if image.startswith(png_signature):
                print("Decrypted image has a PNG header.")
                return True

        except Exception as e:
            print(f"Error checking image header: {e}")
            return False

