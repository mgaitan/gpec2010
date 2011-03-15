Arquitectura
************* 

En este capitulo se describe el diseño arquitectónico general de la aplicación

Modelo conceptual
=================

La siguiente infografía describe conceptualmente, de manera simplificada, 
el flujo de procesamiento de la información.

.. figure:: images/workflow.png
   :width: 70%

   Diagrama conceptual del flujo de información entre las distintas capas 

El frontend, objeto de este trabajo, se compone de la interfaz de usuario, 
la gestión de base de datos, los algoritmos de procesamiento de 
la información y la graficación.

:abbr:`API (Application Programming Interface` refiere a la interfaz de 
comunicación definida para la comunicación entre ambas partes, que está basada
en archivos de texto plano con un formato particular. El relevamiento de esta interfaz 
formó parte del desarrollo, y se describe exhaustivamente en :ref:`api`. 
Una librería basada en ese relevamiento se programó para dar soporte a la comunicación. Se describe
en :ref:`backend`. 

El backend refiere al conjunto de programas desarrollados en Fortran que implementan
los algoritmos de cálculo. Estos programas leen uno o varios archivos de entrada
y producen un archivo de salida con la los vectores de números 
reales resultantes de los cálculos (la información a graficar) junto a otras 
informaciones relativas al contexto de cálculo

Los algoritmos de procesamiento analizan y extraen sólo la información útil, 
haciendo una conversión de texto a un tipo de dato numérico y con esa información
se realizan los gráficos correspondientes. 


Componentes y capas de software 
================================

El siguiente diagrama, diseñado con la intención de favorecer la compresión
por sobre el apego al estándar UML, describe las capas y componentes de software
involucrados en la aplicación. 

.. figure:: images/arquitectura.png
   :width: 70%

   Arquitectura Frontend - Middleware - Backend      

Este diagrama complementa al anterior brindando más detalles sobre la forma 
la estructura jerárquica de las capas de software. 







