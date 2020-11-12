import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

key = b''
try:

    # Send data
    message = b'Dame una llave publica.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    #while amount_received < amount_expected:
    while amount_received != 1 :
        data = sock.recv(16)
        print('received {!r}'.format(data))
        key += data
        
        if(data == b'--'):
            key += data
            amount_received = 1


finally:
    print('closing socket')
    sock.close()

print(key)