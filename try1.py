#libraries
import hashlib
from cryptography.fernet import Fernet
import rsa

# #input file
# filename = input('Enter the file:'+" ")
#
# #input public key
# Public_key = input('Enter public key file name:'+" ")

def Encrypt(filename, public_key):
    #hasing
    def hash_file(filename):
        h = hashlib.sha256()
        with open(filename,'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(65536)
                h.update(chunk)
        return h.hexdigest()

    hash = hash_file(filename)
    # print(hash)

    #saving hased file
    with open('hashed.txt', 'w') as file:
        file.write(hash)

    #key generation
    key = Fernet.generate_key()

    #saving keys
    with open('Symmetric_key.key', 'wb') as file:
        file.write(key)

    #symmetric encription
    def Symmetric_Encryption(filename, key):
        data =''
        with open(filename, 'rb')as file:
            data = file.read()

        f = Fernet(key)
        encrypted_data = f.encrypt(data)

        with open('Symmetric.txt', 'wb')as file:
            file.write(encrypted_data)

    Symmetric_Encryption(filename, key)

    #public key
    with open('public.pem', 'rb') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())

    #asymmetric encryption
    def Asymmetric_Encryption(filename, public_key):
        data = filename
        # with open(filename, 'rb')as file:
        #     data = file.read()

        with open('public.pem', 'rb') as file:
            public_key = rsa.PublicKey.load_pkcs1(file.read())

        encrypted_data = rsa.encrypt(data, public_key)

        with open('Asymmetric.txt', 'wb') as file:
            file.write(encrypted_data)

    Asymmetric_Encryption(key, public_key)


