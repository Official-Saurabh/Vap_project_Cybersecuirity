#import lib
import hashlib
from cryptography.fernet import Fernet
import rsa

# #encrypted files inputs
# Symmetric_data = input('Enter the file:'+" ")
# Asymmetric_data = input('Enter the file:'+" ")
# # Hased = input('Enter the file:'+" ")
#
# #inputs private key
# Private_key = input('Enter private key file name:'+" ")

def Decrypt (Symmetric_data, Asymmetric_data, Private_key):
    #reading private key
    with open('private.pem', 'rb') as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())

    #decryption of symeetric key
    def Asymmetric_Decryption(filename, private_key):
        data =''
        with open(filename, 'rb') as file:
            data = file.read()
        decrypted_data = rsa.decrypt(data, private_key)
        with open('Symmetric_Secret.key', 'wb') as file:
            file.write(decrypted_data)

    Asymmetric_Decryption(Asymmetric_data, private_key)
    try:
        #decryption of file
        def Symmetric_Decreption(filename ,secret_key_file):
            key =''
            with open(secret_key_file, 'rb') as key_file:
                key = key_file.read()

            data =''
            with open(filename, 'rb')as file:
                data = file.read()

            f = Fernet(key)
            decrypted_data = f.decrypt(data)

            with open('test_result.pdf', 'wb')as file:
                file.write(decrypted_data)

        Symmetric_Decreption(Symmetric_data, "Symmetric_Secret.key")

    except:
        #decryption of file
        def Symmetric_Decreption(filename ,secret_key_file):
            key =''
            with open(secret_key_file, 'rb') as key_file:
                key = key_file.read()

            data =''
            with open(filename, 'rb')as file:
                data = file.read()

            f = Fernet(key)
            decrypted_data = f.decrypt(data)

            with open('test_result.pdf', 'wb')as file:
                file.write(decrypted_data)

        Symmetric_Decreption(Symmetric_data, "Symmetric_Secret.key")

    #to hash file
    # def hash_file(filename):
    #     h = hashlib.sha256()
    #     with open(filename,'rb') as file:
    #         chunk = 0
    #         while chunk != b'':
    #             chunk = file.read(65536)
    #             h.update(chunk)
    #     return h.hexdigest()
    #
    # hash = hash_file(Hased)
    #
    # #reading hashed file
    # hash_comp =""
    # with open("hashed.txt", 'rb') as file:
    #     hash_comp = file.read()
    #
    # #comparing hashed file
    # if hash == hash_comp:
    #     print("There is no alteration in the files")
    # else:
    #     print("There is alteration")



