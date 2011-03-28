Arquitectura
************* 

En este capitulo se describe, de manera conceptual, el diseño arquitectónico
de la aplicación.

.. _modelo:

Modelo conceptual
=================

La siguiente infografía describe conceptualmente, de manera simplificada, 
el flujo de procesamiento de la información.

.. figure:: images/workflow.png
   :width: 70%

   :index:`Diagrama conceptual` del flujo de información entre las distintas capas 

El frontend, objeto de este trabajo, se compone de la interfaz de usuario, 
la gestión de base de datos, los algoritmos de procesamiento de 
la información y la graficación.

:abbr:`API (Application Programming Interface)` refiere a la interfaz de 
comunicación definida para la comunicación entre ambas partes, que está basada
en archivos de texto plano con un formato particular. El relevamiento de esta interfaz 
formó parte del desarrollo, y se describe exhaustivamente en :ref:`api`. 
Una librería modularmente independiente, basada en ese relevamiento se 
programó para dar soporte a la comunicación. Se describe en :ref:`backend`. 

El backend refiere al conjunto de programas desarrollados en Fortran que implementan
los algoritmos de cálculo. Estos programas leen uno o varios archivos de entrada
y producen un archivo de salida con los vectores de números 
reales resultantes de los cálculos (la información a graficar) junto a otras 
informaciones relativas al contexto de cálculo

Los algoritmos de procesamiento analizan y extraen sólo la información útil, 
haciendo una conversión de texto a un tipo de dato numérico y con esa información
se realizan los gráficos correspondientes. 


Componentes y capas de software 
================================

El siguiente diagrama, diseñado con la intención de favorecer la comprensión
por sobre el apego a la especificación :term:`UML`, describe las capas y 
:index:`componentes` de software involucrados en la aplicación. 

.. figure:: images/arquitectura.png
   :width: 60%

   Arquitectura Frontend - Middleware - Backend      

Este diagrama complementa al anterior brindando más detalles sobre la 
vinculación de los componentes y las capas de software. Por simplicidad, 
se ha obviado la descripción de los componentes Matplotlib y Numpy, asumiéndolos 
tácitamente como parte de la aplicación. 

Los componentes de :term:`middleware` de conexión a la base de datos 
:py:mod:`sqlite3` (un :term:`wrapper` sobre ``Sqlite``) y el módulo que permite 
la ejecución de procesos hijos 
(o "subprocesos") :py:mod:`subproccess`` forman parte de las versiones 
2.5 y 2.4 de Python respectivamente. Es decir, no son componentes de software 
que se requieran por separado. 

La llamada a los procesos del backend a través de :py:mod:`subproccess`` está 
intercedida por el emulador *Wine* en todas las plataformas diferentes 
a Windows. Esto se describe ampliamente en :ref:`wine`.

Un componente que se representa intrínsecamente vinculado al frontend es 
Pub/Sub. La explicación de la importancia estructural de este componente
se describe en :ref:`uso-pubsub`.

 


