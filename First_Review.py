from try1 import *
from decrypt_try1 import *


print("PLEASE SELECT THE MODE OF OPERATION FROM BELOW:")
print("TYPE 1 FOR ENCRYPTION AND TYPE 2 FOR DECRYPTION")
match int(input("ENTER YOUR CHOISE: ")):
    case 1:
        try:
            filename = input("ENTER THE FILE PATH TO ENCRYPT THE FILE: ")
            #Public_key =input("ENTER THE PUBLIC KEY: ")
            Encrypt(filename)
            print("SUCCESSFULLY ENCRYPTED THE FILE")
        except Exception as e:
            print("SOME ERROR OCCURRED DURING ENCRYPTION", {e})

    case 2:
        try:
            # symmetric_data = input("ENTER SYMMETRIC DATA FILE: ")
            # asymmetric_data = input("ENTER ASYMMETRIC DATA FILE: ")
            CompressedFiles_Dir = input("ENTER DIRECTORY PATH FOR DECRYPT: ")
            #private_key = input("ENTER THE PRIVATE KEY: ")
            Decrypt(CompressedFiles_Dir)
            print("SUCCESSFULLY DECRYPTED THE FILE")
        except Exception as e:
            print("SOME ERROR OCCURRED DURING DECRYPTION", {e})

    case _:
        print("INVALID INPUTS")
