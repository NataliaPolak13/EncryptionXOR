import os
from extended_encryption import ExtendedEncryption
from basic_encryption import BasicEncryption

class ImageEncryptionProgram:
    def __init__(self):
        self.invalid_choice_message_displayed = False
        self.exit_program = False  # Dodana flaga informująca o zakończeniu programu

    def display_menu(self):
        print(
            "Witaj w programie do szyfrowania i deszyfrowania zdjęć z folderu. Wybierz czy chcesz działać na folderze z:"
            "\n 1. Lokalizacją skryptu "
            "\n 2. Wybraną lokalizacją na komputerze"
            "\n 3. Chcę wyjść z programu")

    def get_path_choice(self):
        while True:
            path_choice = input("Podaj, którą opcję wybierasz: ")
            if path_choice in ('1', '2', '3'):
                return path_choice
            else:
                print("Podałeś/aś błędną wartość. Spróbuj ponownie.")

    def execute_option(self, path_choice, location=None):
        if path_choice == '1':
            script_path = os.path.normpath(os.path.join(os.path.dirname(__file__)))
            self.execute_option_1(script_path)
        elif path_choice == '2':
            location = input("Podaj lokalizację, w której znajduje się folder ze zdjęciami: ")
            if location and os.path.exists(location) and os.path.isdir(location):
                self.execute_option_2(location)
            else:
                print(f"Lokalizacja '{location}' nie istnieje lub nie jest katalogiem.")
        elif path_choice == '3':
            self.exit_program = True  # Ustawienie flagi na zakończenie programu

    def execute_option_1(self, script_path):
        print("Rozpoczynam działanie..."
              "\n 1. Szyfrowanie zdjęć przy użyciu ulepszonego algorytmu XOR"
              "\n 2. Szyfrowanie zdjęć przy użyciu podstawowego algorytmu XOR")

        xor_choice = input("Podaj, który algorytm XOR wybierasz: ")
        if xor_choice == '1':
            extended_encryption = ExtendedEncryption(script_path)
            extended_encryption.extended_algorithm()
        elif xor_choice == '2':
            basic_encryption = BasicEncryption(script_path)
            basic_encryption.basic_algorithm()
        else:
            print("Wybrałeś/aś nieprawidłową opcję. Powracasz do wyboru folderu. ")

    def execute_option_2(self, localization):
        print("Rozpoczynam działanie..."
              "\n 1. Szyfrowanie zdjęć przy użyciu ulepszonego algorytmu XOR"
              "\n 2. Szyfrowanie zdjęć przy użyciu podstawowego algorytmu XOR")

        xor_choice = input("Podaj, który algorytm XOR wybierasz: ")
        if xor_choice == '1':
            extended_encryption = ExtendedEncryption(localization)
            extended_encryption.extended_algorithm()
        elif xor_choice == '2':
            basic_encryption = BasicEncryption(localization)
            basic_encryption.basic_algorithm()
        else:
            print("Wybrałeś/aś nieprawidłową opcję. Powracasz do wyboru folderu. ")

    def run(self):
        while not self.exit_program:
            self.display_menu()
            path_choice = self.get_path_choice()
            self.execute_option(path_choice)





