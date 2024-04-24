# #import lib
# import hashlib
# from cryptography.fernet import Fernet
# import rsa
#
# # #encrypted files inputs
# # Symmetric_data = input('Enter the file:'+" ")
# # Asymmetric_data = input('Enter the file:'+" ")
# # # Hased = input('Enter the file:'+" ")
# #
# # #inputs private key
# # Private_key = input('Enter private key file name:'+" ")
#
# def Decrypt (Symmetric_data, Asymmetric_data, Private_key):
#     #reading private key
#     with open('private.pem', 'rb') as file:
#         private_key = rsa.PrivateKey.load_pkcs1(file.read())
#
#     #decryption of symeetric key
#     def Asymmetric_Decryption(filename, private_key):
#         data =''
#         with open(filename, 'rb') as file:
#             data = file.read()
#         decrypted_data = rsa.decrypt(data, private_key)
#         with open('Symmetric_Secret.key', 'wb') as file:
#             file.write(decrypted_data)
#
#     Asymmetric_Decryption(Asymmetric_data, private_key)
#     try:
#         #decryption of file
#         def Symmetric_Decreption(filename ,secret_key_file):
#             key =''
#             with open(secret_key_file, 'rb') as key_file:
#                 key = key_file.read()
#
#             data =''
#             with open(filename, 'rb')as file:
#                 data = file.read()
#
#             f = Fernet(key)
#             decrypted_data = f.decrypt(data)
#
#             original_filename, _, original_format = filename.rpartition(".")
#             original_filename = original_filename.rpartition(".")[0]  # Remove encryption extensions
#             output_filename = original_filename + "." + original_format  # Construct original filename
#
#             with open(output_filename, 'wb') as file:  # Use original filename
#                 file.write(decrypted_data)
#
#         Symmetric_Decreption(Symmetric_data, "Symmetric_Secret.key")
#
#     except:
#         #decryption of file
#         def Symmetric_Decreption(filename ,secret_key_file):
#             key =''
#             with open(secret_key_file, 'rb') as key_file:
#                 key = key_file.read()
#
#             data =''
#             with open(filename, 'rb')as file:
#                 data = file.read()
#
#             f = Fernet(key)
#             decrypted_data = f.decrypt(data)
#
#             original_filename, _, original_format = filename.rpartition(".")
#             original_filename = original_filename.rpartition(".")[0]  # Remove encryption extensions
#             output_filename = original_filename + "." + original_format  # Construct original filename
#
#             with open(output_filename, 'wb') as file:  # Use original filename
#                 file.write(decrypted_data)
#
#         Symmetric_Decreption(Symmetric_data, "Symmetric_Secret.key")
#
#     #to hash file
#     # def hash_file(filename):
#     #     h = hashlib.sha256()
#     #     with open(filename,'rb') as file:
#     #         chunk = 0
#     #         while chunk != b'':
#     #             chunk = file.read(65536)
#     #             h.update(chunk)
#     #     return h.hexdigest()
#     #
#     # hash = hash_file(Hased)
#     #
#     # #reading hashed file
#     # hash_comp =""
#     # with open("hashed.txt", 'rb') as file:
#     #     hash_comp = file.read()
#     #
#     # #comparing hashed file
#     # if hash == hash_comp:
#     #     print("There is no alteration in the files")
#     # else:
#     #     print("There is alteration")
#
#
#

#
# import gzip
# import shutil
# from cryptography.fernet import Fernet
# import rsa
# import os
#
# def Decrypt(compressed_files_dir, private_key_path):
#     # Read the private RSA key
#     with open(private_key_path, 'rb') as file:
#         private_key = rsa.PrivateKey.load_pkcs1(file.read())
#
#     # Decompress the files within the specified directory
#     decompress_directory(compressed_files_dir, compressed_files_dir)
#
#     # Asymmetric decryption of the symmetric key
#     symmetric_key_file = os.path.join(compressed_files_dir, "Symmetric_key.key")  # Adjust path
#     Asymmetric_Decryption(symmetric_key_file, private_key)
#
#     # Symmetric decryption of the original files
#     for filename in os.listdir(compressed_files_dir):
#         if filename.endswith(".aes"):  # Target only encrypted files
#             Symmetric_Decryption(os.path.join(compressed_files_dir, filename), "Symmetric_Secret.key")
#
# def decompress_directory(src_dir, dst_dir):
#     for filename in os.listdir(src_dir):
#         src_path = os.path.join(src_dir, filename)
#         dst_path = os.path.join(dst_dir, filename.replace(".gz", ""))
#         if filename.endswith(".gz"):  # Only decompress compressed files
#             with gzip.open(src_path, 'rb') as src, open(dst_path, 'wb') as dst:
#                 shutil.copyfileobj(src, dst)  # Efficient decompression
#             os.remove(src_path)  # Remove compressed file after decompression
#
# def Asymmetric_Decryption(filename, private_key):
#     with open(filename, 'rb') as file:
#         encrypted_data = file.read()
#     decrypted_data = rsa.decrypt(encrypted_data, private_key)
#     with open('Symmetric_Secret.key', 'wb') as file:
#         file.write(decrypted_data)
#
# def Symmetric_Decryption(filename, secret_key_file):
#     with open(secret_key_file, 'rb') as key_file:
#         key = key_file.read()
#
#     with open(filename, 'rb') as file:
#         encrypted_data = file.read()
#
#     f = Fernet(key)
#     decrypted_data = f.decrypt(encrypted_data)
#
#     original_filename, _, original_format = filename.rpartition(".")
#     original_filename = original_filename.rpartition(".")[0]  # Remove encryption extensions
#     output_filename = original_filename + "." + original_format  # Construct original filename
#
#     with open(output_filename, 'wb') as file:  # Use original filename
#         file.write(decrypted_data)
#
# # Example usage (replace with actual paths):
# # Decrypt("CompressedFiles", "private.pem")


# import gzip
# from cryptography.fernet import Fernet
# import rsa
# import os
# import shutil
#
# def Decrypt(compressed_files_dir, private_key_path):
#     # Read the private RSA key
#     with open(private_key_path, 'rb') as file:
#         private_key = rsa.PrivateKey.load_pkcs1(file.read())
#
#     def create_output_directory(directory_name):
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#     # Get user input for output directory
#     output_dir = input("Enter the directory to save decrypted files: ")
#     if not output_dir:
#         # Use current working directory as default
#         output_dir = os.getcwd()
#     create_output_directory(output_dir)  # Ensure output directory exists
#
#     # **Corrected path for decompressing files**
#     decompress_directory(compressed_files_dir, output_dir)  # Decompress to output directory
#
#     # **Corrected path for the symmetric key file**
#     symmetric_key_file = os.path.join(output_dir, "Symmetric_key.key.rsa")  # RSA-encrypted key
#     Asymmetric_Decryption(symmetric_key_file, private_key)
#
#     # Symmetric decryption of the original files
#     for filename in os.listdir(output_dir):
#         if filename.endswith(".aes"):
#             Symmetric_Decryption(os.path.join(output_dir, filename), "Symmetric_Secret.key")
#
#     # Remove temporary files (optional)
#     try:
#         os.remove(symmetric_key_file)
#         os.remove("Symmetric_Secret.key")
#         print("Temporary files removed successfully.")
#     except Exception as e:
#         print(f"Error removing temporary files: {e}")
#
# def decompress_directory(src_dir, dst_dir):
#     for filename in os.listdir(src_dir):
#         src_path = os.path.join(src_dir, filename)
#         dst_path = os.path.join(dst_dir, filename.replace(".gz", ""))
#         if filename.endswith(".gz"):  # Only decompress compressed files
#             with gzip.open(src_path, 'rb') as src, open(dst_path, 'wb') as dst:
#                 shutil.copyfileobj(src, dst)  # Efficient decompression
#             os.remove(src_path)  # Remove compressed file after decompression
#
# def Asymmetric_Decryption(filename, private_key):
#     with open(filename, 'rb') as file:
#         encrypted_data = file.read()
#     decrypted_data = rsa.decrypt(encrypted_data, private_key)
#     with open('Symmetric_Secret.key', 'wb') as file:
#         file.write(decrypted_data)
#
# def Symmetric_Decryption(filename, secret_key_file):
#     with open(secret_key_file, 'rb') as key_file:
#         key = key_file.read()
#
#     with open(filename, 'rb') as file:
#         encrypted_data = file.read()
#
#     f = Fernet(key)
#     decrypted_data = f.decrypt(encrypted_data)
#
#     original_filename, _, original_format = filename.rpartition(".")
#     original_filename = original_filename.rpartition(".")[0]  # Remove encryption extensions
#     output_filename = original_filename + "." + original_format  # Construct original filename
#
#     with open(output_filename, 'wb') as file:  # Use original filename
#         file.write(decrypted_data)


# Decrypt("/home/saurabh-singh/Downloads/CompressedFiles", "private.pem")



import gzip
import shutil

from cryptography.fernet import Fernet
import rsa
import os

def create_output_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def Decrypt(directory):
    # Load the private RSA key
    def find_file(filename, start_dir):
        for dirpath, dirnames, filenames in os.walk(start_dir):
            if filename in filenames:
                filepath = os.path.join(dirpath, filename)
                #print(f"File found: {filepath}")
                # Read the file content here (replace with your reading logic)
                with open(filepath, 'rb') as file:
                    private_key = rsa.PrivateKey.load_pkcs1(file.read())
                return  private_key # Exit the function after finding the file

    pfile = "private.pem"
    start_dir = "/home/saurabh-singh/"
    # with open(private_key_file, 'rb') as file:
    #     private_key = rsa.PrivateKey.load_pkcs1(file.read())
    private_key = find_file(pfile, start_dir)

    # Decompress the encrypted files within the directory
    decompress_directory(directory, directory)

    # Decrypt the symmetric key
    with open(os.path.join(directory, "Symmetric_key.key.rsa"), 'rb') as file:
        encrypted_key = file.read()
    decrypted_key = rsa.decrypt(encrypted_key, private_key).decode()

    # Decrypt the files using the decrypted symmetric key
    for filename in os.listdir(directory):
        if filename.endswith(".aes"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'rb') as file:
                encrypted_data = file.read()

            f = Fernet(decrypted_key)
            decrypted_data = f.decrypt(encrypted_data)

            output_filename = os.path.splitext(filename)[0]  # Remove .aes extension
            output_directory = input("Enter the directory to save decrypted files: ")
            create_output_directory(output_directory)
            output_filepath = os.path.join(output_directory, output_filename)
            with open(output_filepath, 'wb') as file:
                file.write(decrypted_data)

            os.remove(filepath)

    os.remove(os.path.join(directory, "Symmetric_key.key.rsa"))
    os.remove(os.path.join(directory, "Symmetric_key.key"))


def decompress_directory(src_dir, dst_dir):
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.splitext(src_path)[0]  # Remove .gz extension
        if filename.endswith(".gz"):
            with gzip.open(src_path, 'rb') as src, open(dst_path, 'wb') as dst:
                shutil.copyfileobj(src, dst)
            os.remove(src_path)

# Example usage
# Decrypt("/home/saurabh-singh/Downloads/CompressedFiles", "private.pem")  # Replace with actual directory and private key file
