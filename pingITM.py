import os
hostname = "200.33.171."
prendidas=0
for i in range(254):
 respuesta = os.system("ping " + hostname+repr(i))
 if respuesta == 0:
  
  
  prendidas+1
  print (hostname+repr(i) + "En funcionamiento: !"+repr(prendidas))

 else:
  print (hostname+repr(i) + "no esta funcionamiento!")


  
