import os
hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping " + hostname)
if respuesta == 0:
 print (hostname + "esta funcionamiento!")
else:
 print (hostname + "no esta funcionamiento!")