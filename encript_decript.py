import random
import string

li=" "+ string.punctuation +string.digits+string.ascii_letters
chars=list(li)
keys=list(chars)
random.shuffle(keys)

plain_text=input("enter a the text :")
encrypted_text=""
for i in plain_text:
    index=chars.index(i)
    encrypted_text +=keys[index]
print("original text : ",plain_text)
print("encrypted text : ",encrypted_text)
encr =input("enter a the  encrypted text :")
decrypt_text=""
for i in encrypted_text:
    index=keys.index(i)
    decrypt_text +=chars[index]
print("encrypted text : ",encr)
print("decrypted text : ",decrypt_text)

