import os
import bcrypt
#os.system('time hashcat -m 0 -a 0 --potfile-path=/Users/Bastian/desktop/tarea_4/archivo_1/my.pot.txt /Users/Bastian/desktop/tarea_4/archivo_1/archivo_1 /Users/Bastian/desktop/tarea_4/diccionario_2.dict')

f = open("my.pot.txt", "r")   #abre potfile, lee las contrasenas y las hashea 1 x 1.
f2 = open("salida_hasheada.txt", "a+")

a = f.read().split('\n')

for i in range(0, len(a)-1):
	b = a[i].split(':')
	print(b[1])
	
	c = bytes(b[1], 'utf-8')
	
	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(c, salt)

	f2.write(hashed.decode("utf-8") + '\n' )
	print(hashed)

f.close()
f2.close()