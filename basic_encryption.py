import os
from photo_processor import PhotoProcessor
import random

class BasicEncryption(PhotoProcessor):
    def __init__(self, script_path):
        super().__init__(script_path)

    def encryption(self, data):
        key = random.randint(0, 255)
        encrypted_data = bytearray()
        for byte in data:
            encrypted_byte = byte ^ key
            encrypted_data.append(encrypted_byte)
        return bytes(encrypted_data)

    def decryption(self, data):
        decrypted_results = []

        def check_image_header(partial_data, possible_key, image_type):
            # dla pliku JPEG
            jpeg_expected_header = b'\xFF\xD8\xFF'
            # dla PNG
            png_expected_header = b'\x89PNG\r\n\x1a\n'

            # deszyfrowanie nagłówka i porównanie z oczekiwanym
            decrypted_header = b''  # pusty nagłówek
            for byte in partial_data:
                # każdy bajt nagłówka jest deszyfrowany przy użyciu XOR z kluczem
                decrypted_byte = byte ^ possible_key
                # dodanie zdeszyfrowanego bajtu do nagłówka
                decrypted_header += bytes([decrypted_byte])

            if image_type == 'JPEG':
                return decrypted_header.startswith(jpeg_expected_header)
            elif image_type == 'PNG':
                return decrypted_header.startswith(png_expected_header)
            print(f"Inny typ obrazu: {image_type}")
            return False

        for possible_key in range(256):
            # Sprawdzanie tylko nagłówka dla pliku JPEG
            header_length_jpeg = len(b'\xFF\xD8\xFF')
            partial_data_jpeg = data[:header_length_jpeg]

            if check_image_header(partial_data_jpeg, possible_key, 'JPEG'):
                decrypted_data = b''.join(bytes([byte ^ possible_key]) for byte in data)
                decrypted_results.append(decrypted_data)

            # Sprawdzanie tylko nagłówka dla pliku PNG
            header_length_png = len(b'\x89PNG\r\n\x1a\n')
            partial_data_png = data[:header_length_png]

            if check_image_header(partial_data_png, possible_key, 'PNG'):
                decrypted_data = b''.join(bytes([byte ^ possible_key]) for byte in data)
                decrypted_results.append(decrypted_data)

        return decrypted_results

    def basic_algorithm(self):
        photos_path = os.path.join(self.script_path, "ZdjeciaDoSzyfrowania")
        images_before_encryption = self.get_photo_binary(photos_path)
        output_path = os.path.join(self.script_path, "ZaszyfrowaneZdjeciaAlgorytmemPodstawowym")
        second_output_path = os.path.join(self.script_path, "OdszyfrowaneZdjeciaAlgorytmemPodstawowym")
        for i, photo in enumerate(images_before_encryption):
            encrypted = self.encryption(photo)
            if not os.path.exists(os.path.join(self.script_path, output_path)):
                os.mkdir(os.path.join(self.script_path, output_path))
            self.save_photo([encrypted], [os.path.join(output_path, f"zaszyfrowane_zdjecie_{i + 1}.jpg")])

        for i, photo in enumerate(images_before_encryption):
            decrypted = self.decryption(photo)
            if not os.path.exists(os.path.join(photos_path, second_output_path)):
                os.mkdir(os.path.join(photos_path, second_output_path))

            try:
                print(f'You can decrypt {i + 1} photo')

                # Sprawdzam, czy zdeszyfrowane zdjęcie ma oczekiwany nagłówek
                if self.check_image_header(decrypted[0]):
                    self.save_photo(decrypted, [os.path.join(second_output_path, f"odszyfrowane_zdjecie_{i + 1}.jpg")])
                else:
                    print(f"Invalid image header for decrypted image or image type {i + 1}")

            except Exception as e:
                print(f"Error {i + 1} photo: {e}")


