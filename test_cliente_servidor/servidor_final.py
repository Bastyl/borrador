import socket
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)


while True:
    print('Esperando una coneccion')
    connection, client_address = sock.accept()
    try:
        print('coneccion de', client_address)

        while True:
            data = connection.recv(16)
            print('recibido {!r}'.format(data))
            if data:
                print('generando y enviando clave publica')

                key = RSA.generate(2048) #llave privada
                public_key = key.publickey()
                f = open('private.pem','wb')
                f.write(key.export_key('PEM'))  #OPCION DE ELIMINAR QUE SE GUARDE EN PUBLIC.PEM en este punto y hacerlo en cliente_final
                f.close()
                f = open('public.pem','wb')
                f.write(public_key.export_key('PEM'))
                f.close()

                f = open('public.pem','r')
                connection.sendall(bytes(f.read(), 'utf-8'))
                f.close()
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()