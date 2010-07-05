Diagramas y proyecciones
========================

*GPEC* permite el cálculo de múltiples diagramas n-dimensionales, que se 
grafican en proyecciones bidimensionales. 
Esta documentación define cuales son los gráficos que se deben presentar 
al usuario y cómo se obtienen. 


Diagrama Global
---------------

El diagrama de equilibrio de fase global es el más general y utilizado
de los que se obtienen que el software. 
Toda la información para los gráficos se obtiene de los distintos datos 
tabulados de ``GPECOUT.DAT``. 

Proyección Presión-temperatura (P-T)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. image:: images/projection-p-t.jpg
    :align: center
 
Representa curvas de presión (bar) en función de la temperatura (K). 
La siguiente tabla describe la ubicación de los datos para cada curva.

 ==============  =======================================  ===  ===  ========
 Identificador   Tipo de curva                            X    Y    Cantidad
 ==============  =======================================  ===  ===  ========
 ``VAP``         Línea de presión vapor (compuesto puro)  0    1    2
 ``CRI``         Línea crítica                            0    1    2
 ``CEP``         Punto crítico                            0    1    1         
 ``LLV``         Línea Liquido-Vapor                      0    1    0 o 1
 ``AZE``         Línea Azeotropica                        -    -    0 o 1
 ==============  =======================================  ===  ===  ========


Proyección Temperatura-composición (T-x)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Representa las curvas de temperatura en función de la proporción de uno de los 
compuestos. 

Para composición del compuesto 1 

 .. image:: images/projection-t-x1.jpg
    :align: center

 ==============  =======================================  ===  ===  ========
 Identificador   Tipo de curva                            X    Y    Cantidad
 ==============  =======================================  ===  ===  ========
 ``CRI``         Línea crítica                            3    0    2
 ``LLV``         Línea Liquido-Vapor                      0    1    0 o 1


 
Para composición del compuesto 2

 .. image:: images/projection-t-x2.jpg
    :align: center

 ==============  =======================================  ===  ===  ========
 Identificador   Tipo de curva                            X    Y    Cantidad
 ==============  =======================================  ===  ===  ========
 ``CRI``         Línea crítica                            4    0    1
 ``CEP``         Punto crítico                            0    1    1         
 ``LLV``         Línea Liquido-Vapor                      0    1    0 o 1
 ``AZE``         Línea Azeotropica                        -    -    0 o 1
 ==============  =======================================  ===  ===  ========


 

Proyección Presión-composición (P-x)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para composición del compuesto 1 


 .. image:: images/projection-p-x1.jpg
    :align: center
 
Para composición del compuesto 2

 .. image:: images/projection-p-x2.jpg
    :align: center
  

Proyección Temperatura-Densidad (T-Rho)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. image:: images/projection-t-rho.jpg
    :align: center
 

Proyección Presión-Densidad (P-Rho)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. image:: images/projection-p-rho.jpg
    :align: center


