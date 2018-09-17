"""
cryptography.py
Author: Emma Tysinger
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

input=input("Enter e to encrypt, d to decrypt, or q to quit: ")
m=input("Message: ")
k=input("Key: ")
message=list(m)
index=[]
#for i in message:
#    index.append(associations.find(i))
#print(index)
