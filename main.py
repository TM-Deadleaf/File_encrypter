#encrypting the file


from cryptography.fernet import Fernet
key=Fernet.generate_key()# used for gen the key
with open("keyfile.txt","wb") as keyfile: #used for writing a key into file
    keyfile.write(key)
with open("keyfile.txt","rb") as keyfile:
    key=keyfile.read()
fernet=Fernet(key)#using fernet to use this key
with open("filee.txt","rb") as file:#reading the original file
    original=file.read()

encrypted=fernet.encrypt(original)
with open("encrypted.txt","wb") as enc: #writing the encrypted file
    enc.write(encrypted)



