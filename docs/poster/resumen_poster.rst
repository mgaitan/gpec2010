Frontend GPEC 2010
==================

El nuevo frontend desarrollado para el software GPEC está desarrollado en 
lenguaje `Python <http://python.org/>`_, basado principalmente en la 
biblioteca para graficación `Matplotlib 
<http://matplotlib.sourceforge.net/>`_, y el toolkit para interfaces gráficas 
de usuario `wxPython <http://wxpython.org/>`_. Esta combinación de 
tecnologías permiten un software íntegramente basado en Software Libre, 
capaz de ejecutarse en sistemas Windows, Linux o Mac y heredero de las 
ventajas de un lenguaje simple, potente y elegante. 

El desarrollo de este trabajo ha sido enmarcado en el uso de *metodologías 
ágiles de desarrollo de software*, que sumado a las características de 
Python configuran una alta capacidad de adaptación al cambio e incorporación 
de requerimientos y un rápido prototipado de funcionalidades. Más aún, se 
ha utilizado una arquitectura basada en paso de mensajes (patrón *pub/sub*) 
que mantiene un acoplamiento bajo entre las distintas partes del programa, 
permitiendo flexibilidad y extensibilidad. 

El nuevo frontend interactúa con los ejecutables que implementan los 
algoritmos de cálculo numérico (desarrollados en Fortran) de la misma manera 
que su versión precedente. Es decir, se ha respetado la interfaz de 
comunicación existente basada en archivos de texto plano. A través de un  
análisis sintáctico (parsing) de los archivos de salida, los datos 
numéricos se convierten a vectores de punto flotante manipulables en Python y graficables con Matplolib. Además de producir gráficos con calidad de publicación exportables a múltiples formatos, esta biblioteca permite realizar gráficos en 3D, funcionalidad aprovechada en esta nueva versión como la más significativa mejora. 

Por último, un aspecto especialmente estudiado ha sido la usabilidad y 
ergonomía del programa. El objetivo ha sido clarificar la interfaz para que 
su uso sea intuitivo manteniendo accesible toda la información y soportando a 
su vez múltiples casos [#]_ en la misma sesión de trabajo. Esto permite 
comparar y/o superponer lo resultados y acceder a los datos numéricos cuando 
es necesario. 

.. [#] Conjunción de un sistema binario y un modelo de cálculo


