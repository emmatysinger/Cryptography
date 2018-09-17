"""
cryptography.py
Author: Emma Tysinger
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
While True:
    inpt=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if inpt=='q':
        print("Goodbye")
        break
    elif inpt=='e':
        m=input("Message: ")
        k=input("Key: ")
        mlist=[]
        klist=[]
        for i in m:
            mlist.append(associations.find(i))
        for i in k:
            klist.append(associations.find(i))
        times=len(mlist)/len(klist)+1
        klist=int(times)*klist
        encryption=[]
        for i in range(0,len(mlist)):
            encryption.append(mlist[i]+klist[i])
        new=[]
        for i in encryption:
            new.append(associations[i])
        new="".join(new)
        print(new)
    elif inpt=='d':
        m=input("Message: ")
        k=input("Key: ")
        mlist=[]
        klist=[]
        for i in m:
            mlist.append(associations.find(i))
        for i in k:
            klist.append(associations.find(i))
        times=len(mlist)/len(klist)+1
        klist=int(times)*klist
        decryption=[]
        for i in range(0,len(mlist)):
            decryption.append(mlist[i]-klist[i])
        new=[]
        for i in decryption:
            if i>=(len(association)-1):
                multiple=
            new.append(associations[i])
        new="".join(new)
        print(new)
    else:
        print("Did not understand command, try again")
        continue
