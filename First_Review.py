from try1 import *
from decrypt_try1 import *
import time

#mode
print("PLEASE SELECT THE MODE OF OPERATION FROM BELOW:")
time.sleep(1)
print("TYPE 1 FOR ENCRYPTION AND TYPE 2 FOR DECRYPTION")
time.sleep(2)
match int(input("ENTER YOUR CHOISE: ")):
    case 1:
        try:
            filename = input("ENTER THE FILE NAME: ")
            Public_key =input("ENTER THE PUBLIC KEY: ")
            Encrypt(filename, Public_key)
            print("SUCCESSFULLY ENCRYPTED THE FILE")
        except:
            print("SOME ERROR OCCURRED DURING ENCRYPTION")

    case 2:
        try:
            symmetric_data = input("ENTER SYMMETRIC DATA FILE: ")
            asymmetric_data = input("ENTER ASYMMETRIC DATA FILE: ")
            private_key = input("ENTER THE PRIVATE KEY: ")
            Decrypt(symmetric_data, asymmetric_data, private_key)
            print("SUCCESSFULLY DECRYPTED THE FILE")
        except:
            print("SOME ERROR OCCURRED DURING DECRYPTION")

    case _:
        print("INVALID INPUTS")
