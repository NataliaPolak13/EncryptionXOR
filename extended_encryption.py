from photo_processor import PhotoProcessor
import os

class ExtendedEncryption(PhotoProcessor):
    def __init__(self, script_path):
        super().__init__(script_path)

# ulepszony XOR, ponieważ używa dynamicznego klucza (bajty w bajtach)
    def encryption(self, data):
        tmp2 = data[0][0]  # Ustawienie klucza do kodowania drugiego bajtu
        data[0] = bytes([data[0][0] ^ 0xB2])  # Kodowanie pierwszego bajtu XORem z wartością 0xB2
        for i in range(1, len(data)):
            tmp = data[i][0]  # Przypisanie zmiennej tmp wartości pierwszego bajtu danej komórki
            data[i] = bytes([data[i][0] ^ tmp2])  # Zakodowanie aktualnego bajtu przez wykonanie operacji XOR z wartością tmp2
            tmp2 = tmp  # Ustawienie klucza do kodowania następnego bajtu
        return data

    # przechodzi przez dwie tablice

    def decryption(self, data):
        decrypted_results = []

        for possible_key in range(256):
            decrypted_data = b'' # pusty bajtowy string

            for byte in data: # Iteracja po każdym bajcie danych
                decoded_bytes = [] # przechowuje odszyfrowane bajty
                for b in byte: # Iteracja po każdym bajcie danych
                    decoded_byte = b ^ possible_key # Odszyfrowanie bajtu za pomocą XOR z aktualnym kluczem
                    decoded_bytes.append(decoded_byte) # Dodanie odszyfrowanego bajtu do listy

                decrypted_byte = bytes(decoded_bytes) # Konwersja listy odszyfrowanych bajtów do obiektu typu bytes
                decrypted_data += decrypted_byte # Dodanie do odszyfrowanych danych

            decrypted_results.append(decrypted_data) # Dodanie do listy wyników

        return decrypted_results


    def extended_algorithm(self):
        output_path = os.path.join(self.script_path, "ZaszyfrowaneZdjeciaALgorytmemRozszerzonym")
        second_output_path = os.path.join(self.script_path, "OdszyfrowaneZdjeciaAlgorytmemRozszerzonym")
        # Zmienna przechowująca lokalizację folderu, w którym znajdują się zdjęcia, za pomocą funkcji join dodajemy nazwę
        # folderu do ścieżki
        photos_path = os.path.join(self.script_path, "ZdjeciaDoSzyfrowania")
        images_before_encryption = self.get_photo_binary(photos_path)
        for i, photo in enumerate(images_before_encryption):
            encrypted = self.encryption([photo])
            if not os.path.exists(os.path.join(self.script_path, output_path)):
                os.mkdir(os.path.join(self.script_path, output_path))
            self.save_photo(encrypted, [os.path.join(output_path, f"zaszyfrowane_zdjecie_{i + 1}.jpg")])

        for i, photo in enumerate(images_before_encryption):
            decrypted = self.decryption([photo])
            if not os.path.exists(os.path.join(photos_path, second_output_path)):
                os.mkdir(os.path.join(photos_path, second_output_path))
            try:
                print(f'You can decrypt {i + 1} photo')

                # Sprawdź, czy zdeszyfrowany obraz ma oczekiwany nagłówek
                if self.check_image_header(decrypted[0]):
                    self.save_photo(decrypted, [os.path.join(second_output_path, f"odszyfrowane_zdjecie_{i + 1}.jpg")])
                else:
                    print(f"Invalid image header for decrypted image or image type{i + 1}")

            except Exception as e:
                print(f"Error {i + 1} photo: {e}")