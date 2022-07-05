import base64
import sys
import pyaes

# A secret with 17 characters in Base64
KEY = b"00000000000000000"
KEY = base64.b64encode(KEY)


def decrypt(filename, key):
    try:
        with open(filename, "rb") as encfile:
            content = encfile.read()
            decrypted = pyaes.AESModeOfOperationCTR(key).decrypt(content)
            new_filename = str(filename).replace(".enc", "")

            with open(new_filename, "wb") as decfile:
                decfile.write(decrypted)


    except Exception as e:
        print("<<<< Error in decrypt")
        print("<<<< {}".format(e))


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Few Arguments is Nedeed.")
            print("Use: $ python3 .\Decryptor.py file Secret_Key(optional)")

        if len(sys.argv) >= 2:
            FILENAME = sys.argv[1]
            if len(sys.argv) == 3:
                KEY = base64.b64encode(sys.argv[2].encode())

            decrypt(FILENAME, KEY)


    except Exception as e:
        print("Error:", e)
