#!/usr/bin/python

n= int (raw_input ("Introduzca el numero de intervalos: "))

suma =0.0
for i in range(1,n+1):
  x_i= float ((i-0.5)/n) 
  print "Subintervalo: ",[(i-1)/float(n), i/float(n)]
  fx_i= float (4./(1+x_i**2))
  print "El valor es: ", fx_i
  suma = suma + fx_i
pi = float (1/float(n) * suma)
print "El valor aproximado de pi es: ", pi
print "El valor de pi con 35 decimales es:%.35f" % pi