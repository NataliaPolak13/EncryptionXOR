# Image Encryption Program

This program allows you to encrypt and decrypt images from a folder using two different XOR encryption algorithms: basic and extended.

## Usage

1. Clone this repository to your local machine.
2. Make sure you have images in the `ZdjeciaDoSzyfrowania` folder.
3. Run the program using the following command:
    ```bash
    python main.py
    ```
4. Follow the on-screen instructions to choose the location of the image folder and the encryption algorithm.
5. Encrypted images will be saved in the `ZaszyfrowaneZdjeciaAlgorytmemPodstawowym` or `ZaszyfrowaneZdjeciaALgorytmemRozszerzonym` folder, depending on the chosen algorithm.
6. Decrypted images will be saved in the `OdszyfrowaneZdjeciaAlgorytmemPodstawowym` or `OdszyfrowaneZdjeciaAlgorytmemRozszerzonym` folder.

## Folder Structure

- `ZdjeciaDoSzyfrowania`: Contains images to be encrypted.
- `ZaszyfrowaneZdjeciaAlgorytmemPodstawowym` or `ZaszyfrowaneZdjeciaALgorytmemRozszerzonym`: Contains encrypted images.
- `OdszyfrowaneZdjeciaAlgorytmemPodstawowym` or `OdszyfrowaneZdjeciaAlgorytmemRozszerzonym`: Contains decrypted images.

### Description

The program is designed to encrypt and decrypt images using two different XOR algorithms: basic and extended.

#### Program Functions:

1. **Image Encryption**: Users can select a folder location containing images to encrypt. Then, they choose the encryption algorithm (basic or extended). 
2. **Image Decryption**: The program automatically detects the encryption algorithm and decrypts the images, saving them in a new folder in the previously chosen location.

#### Encryption Algorithms:

1. **Basic XOR**: Utilizes a randomly generated key for encrypting and decrypting data. Each byte of the image is transformed using XOR operation with the key.

2. **Extended XOR**: An enhanced version of the XOR algorithm that employs a dynamic key. The encryption and decryption process is based on XOR operation between consecutive bytes of the image and the key.

#### Folder Structure:

- `ZdjeciaDoSzyfrowania`: Contains images to be encrypted.
- `ZaszyfrowaneZdjeciaAlgorytmemPodstawowym` or `ZaszyfrowaneZdjeciaALgorytmemRozszerzonym`: Contains encrypted images.
- `OdszyfrowaneZdjeciaAlgorytmemPodstawowym` or `OdszyfrowaneZdjeciaAlgorytmemRozszerzonym`: Contains decrypted images.

Author Natalia Polak
