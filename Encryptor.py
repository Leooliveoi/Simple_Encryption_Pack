import base64
import pyaes
import os
import sys

# A secret with 17 characters in Base64
KEY = b"00000000000000000"
KEY = base64.b64encode(KEY)


def encrypt(filename, key):
    try:
        with open(filename, "rb") as file:
            content = file.read()
            crypt_data = pyaes.AESModeOfOperationCTR(key).encrypt(content)

        with open(filename+".enc", "wb") as file:
            file.write(crypt_data)
            os.remove(filename)
    except Exception as e:
        print("<<<< Error in File manipulation...\n<<<< {}".format(e))



if __name__ == "__main__":
    try:
        if len(sys.argv) < 2 :
            print("Few Arguments is Nedeed.")
            print("Use: $ python3 .\Encryptor.py file Secret_Key(optional)")
            print("Use 17 characters in Secret_Key")

        if len(sys.argv) >= 2:
            FILENAME = sys.argv[1]
            if len(sys.argv) == 3:
                KEY = base64.b64encode(sys.argv[2].encode())

            encrypt(FILENAME, KEY)


    except Exception as e:
        print("Error:", e)

