
import gzip
from cryptography.fernet import Fernet
import rsa
import os
import time


def create_output_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def Encrypt(filepath):

    try:
        def find_file(filename, start_dir):
            for dirpath, dirnames, filenames in os.walk(start_dir):
                if filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    # print(f"File found: {filepath}")
                    # Read the file content here (replace with your reading logic)
                    with open('public.pem', 'rb') as file:
                        public_key = rsa.PublicKey.load_pkcs1(file.read())
                    return public_key  # Exit the function after finding the file

        pfile = "public.pem"
        start_dir = "/home/saurabh-singh/"
    except:
        public_key, private_key = rsa.newkeys(1024)

        with open("public.pem", "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))

        with open("private.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

    # Get filename from filepath
    filename = os.path.basename(filepath)

    # Generate a Fernet key for symmetric encryption
    key = Fernet.generate_key()
    Directory_name = filename + "_CompressedFiles"

    # Get user input for compressed files destination
    compressed_dir = input("Enter the directory to save compressed files (or leave blank for default): ")
    if not compressed_dir:
        compressed_dir = Directory_name  # Use default if blank input

    # Create the output directory if it doesn't exist
    create_output_directory(os.path.join(compressed_dir, Directory_name))  # Create within user-provided path

    # Save the symmetric key securely within the created directory
    with open(os.path.join(compressed_dir, Directory_name, "Symmetric_key.key"), 'wb') as file:
        file.write(key)

    # Perform symmetric encryption
    def Symmetric_Encryption(filepath, key):
        data = ''
        with open(filepath, 'rb') as file:
            data = file.read()

        f = Fernet(key)
        encrypted_data = f.encrypt(data)

        # with open(filename, 'rb') as file:  # No longer needed as filepath is used
        #     file_size = os.path.getsize(filename)  # Get file size for progress bar
        #     with tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Encrypting {filename}") as pbar:
        #         for chunk in iter(lambda: file.read(16384), b""):
        #             pbar.update(len(chunk))  # Update progress bar for each chunk
        #             encrypted_data += f.encrypt(chunk)

        output_filename = os.path.join(compressed_dir, Directory_name, filename + ".aes")
        with open(output_filename, 'wb') as file:
            file.write(encrypted_data)

    Symmetric_Encryption(filepath, key)

    def find_file(filename, start_dir):
        for dirpath, dirnames, filenames in os.walk(start_dir):
            if filename in filenames:
                filepath = os.path.join(dirpath, filename)
                #print(f"File found: {filepath}")
                # Read the file content here (replace with your reading logic)
                with open('public.pem', 'rb') as file:
                    public_key = rsa.PublicKey.load_pkcs1(file.read())
                return  public_key # Exit the function after finding the file

    pfile = "public.pem"
    start_dir = "/home/saurabh-singh/"


    # Read the public RSA key
    # with open('public.pem', 'rb') as file:
    #     public_key = rsa.PublicKey.load_pkcs1(file.read())

    # Perform asymmetric encryption on the symmetric key
    def Asymmetric_Encryption(filename, public_key):
        data = filename
        with open(os.path.join(compressed_dir, Directory_name, filename), 'rb') as file:
            data = file.read()

        encrypted_data = rsa.encrypt(data, public_key)

        output_filename = os.path.join(compressed_dir, Directory_name, filename + ".rsa")
        with open(output_filename, 'wb') as file:
            file.write(encrypted_data)

    Asymmetric_Encryption("Symmetric_key.key",  find_file(pfile, start_dir))

    # Create the output directory if it doesn't exist (for default case)
    # create_output_directory(Directory_name)

    # Compress the encrypted files within the created directory
    compress_directory(os.path.join(compressed_dir, Directory_name), os.path.join(compressed_dir, Directory_name))
    remove_non_gz_files(os.path.join(compressed_dir, Directory_name))
    # Remove the original file after successful compression (assuming success)
    # original_file_path = filepath  # Filepath already available
    # try:
    #     os.remove(original_file_path)
    #     print(f"File '{filename}' compressed and removed successfully!")
    # except FileNotFoundError:
    #     print(f"Error: Could not locate file '{filename}' for removal.")


# Encrypt the file (replace with actual filepath and public key path)
# Encrypt("/path/to/your/file.txt", "public.pem")

# Compression functions

# Compression functions
def gzip_file(src_path, dst_path):
    start_time = time.time()
    with open(src_path, 'rb') as src, gzip.open(dst_path, 'wb') as dst:
        for chunk in iter(lambda: src.read(4096), b""):
            dst.write(chunk)
    end_time = time.time()
    compression_time = end_time - start_time
    print(f"Compression time: {compression_time:.2f} seconds")

def compress_directory(src_dir, dst_dir):
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename + ".gz")
        if os.path.isfile(src_path):  # Check if it's a file before compressing
            gzip_file(src_path, dst_path)

def remove_non_gz_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if not filename.endswith(".gz"):
            try:
                os.remove(filepath)
            except OSError as e:
                print(f"Error removing file '{filename}': {e}")
