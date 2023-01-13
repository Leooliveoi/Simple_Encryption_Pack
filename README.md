# Simple_Encryption_Pack
A simple tool to encrypt and decrypt any file using AES256 encryption

This tool is python3 based.

## Usage

### Encryption

``` $ python3 Encryptor.py <filename> <Optional-Key> ```

> Be attention that the **Optional-Key** parameter is not mandatory but this means that by default the program will use **00000000000000000** as the key!

### Decryption

``` $ python3 Decryptor.py <filename> <Optional-Key> ```

> Be attention that the **Optional-Key** parameter is not mandatory but this means that by default the program will use **00000000000000000** as the key!
> If the key is different that the key used to encrypt the file, the will not decrypt properly.


## Important

### Save the Key used to Encrypt, without it the file will not be decrypted.

### After the encryption the original file will be deleted, be careful.
> You can change this changing the main code.

### The decryption will not delete de encrypted file, with this be careful with larger files.
