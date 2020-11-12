import socket
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

public_key = b''
try:

    message = b'Dame una llave publica.'
    print('sending {!r}'.format(message))
    sock.sendall(message)
    amount_received = 0

    while amount_received != 1 :  #recibe la llave
        data = sock.recv(16)
        print('received {!r}'.format(data))
        public_key += data
        
        if(data == b'--'):
            public_key += data
            amount_received = 1

    #____________ CIFRA ___________
    message = b'You can attack now!'

    key = RSA.importKey(public_key)
    # HACER QUE EN ESTA PARTE SE GUARDE LA KEY EN public_KEY 
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)

    print(ciphertext)

finally:
    print('closing socket')
    sock.close()

print(key)