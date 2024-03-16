import  rsa

(pubkey, privkey) = rsa.newkeys(1024)



with open('public.pem', 'wb') as file:
    file.write(pubkey.save_pkcs1("PEM"))

with open('private.pem', 'wb') as file:
    file.write(privkey.save_pkcs1("PEM"))


#noice