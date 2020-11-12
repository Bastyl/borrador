from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048) #llave privada
public_key = key.publickey()

f = open('private.pem','wb')
f.write(key.export_key('PEM'))
f.close()

f = open('public.pem','wb')
f.write(public_key.export_key('PEM'))
f.close()


message = b'You can attack now!'
key = RSA.importKey(open('public.pem').read())
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)

#print(ciphertext)

private_key = RSA.importKey(open('private.pem').read())
cipher = PKCS1_OAEP.new(private_key)
message_2 = cipher.decrypt(ciphertext)

print(message_2)