*****************************
Ingeniería de requerimientos
*****************************

.. _relevamiento:

Relevamiento de la versión preexistente
=======================================

Aspectos históricos
--------------------

La versión previa de GPEC es una aplicación para entornos Microsoft Windows (Windows 2000, Windows XP 
o superior) desarrollada en una arquitectura de dos bloques funcionales:

1.  **Cálculos e implementación de algoritmos numéricos**, desarrollados en Fortran
2.  **Interfaz de usuario, validación y graficación** (*frontend*), desarrollado en Visual Basic

Esta arquitectura respondió a dos cuestiones principales: 

* La preexistencia de los programas de cálculo (ejecutables sin interfaz de usuario) que desarrolló 
  el Dr. Martín Cismondi como tésis doctoral y mantiene hasta la actualidad, con la colaboración del 
  Dr. Marcelo Sabaloy y la supervisión del Dr. Esteban Brignole, 

* La necesidad pragmática de separar el desarrollo del *"Gpec visual"*, trabajo realizado 
  por Diego Nuñez, del mantenimiento e implementación de nuevos algoritmos y 
  ecuaciones de estado. 

La labor de Diego Nuñez se produjo en el marco de su pasantía en 
:abbr:`PLAPIQUI (Planta Piloto de Ingeniería Química`_ durante los años 
2004 y 2005, cuando el Dr. Cismondi regreso 

Descripción general
--------------------

La interfaz visual de GPEC presenta al usuario una GUI para interactuar con los 
distintos parámetros del diagrama elegido, envía los parámetros a los algoritmos
de cálculo y procesa las salidas de estos generando y mostrando los 
diferentes diagramas. 

.. figure:: images/visual_gpec1.png
   :width: 80%
   
   Interfaz principal de *Visual Gpec*. Definiendo un sistema Methane-Methanol
   con la EoS RK-PR. 


La comunicación con los algoritmos implementados en Fortran se realiza mediante
archivos de texto plano en un formato cuya estructura *ad hoc* es comprendida por 
las dos partes (ver `API`_). Asimismo, los datos de salida que producen los algoritmos, son 
leídos por Visual Gpec desde archivos de texto para su posterior graficación. 

Dicha graficación se realiza mediante rutinas desarrolladas *ad hoc* para esta 
implementación: los gráficos se generan a un nivel de abstracción muy bajo 
(punto a punto, sobre un widget tipo canvas). 

El resultado de esto, si bien es aceptable y funcional, implicó muchas horas de 
desarrollo, con gráficos poco configurables y de baja calidad visual.  


Aspectos de ingeniería de software
-----------------------------------

Durante su desarrollo anterior, GPEC no adoptó ninguna metodología de 
desarrollo particular, salvo la concerniente a la separación  
funcional de la aplicación como se explica más arriba. 

.. figure:: images/visual_gpec2.png
   :width: 80%
   
   Visualizacion de un diagrama P-T para el sistema Methane-Methanol
   con modelo RK-PR. 


Un problema manifestado por el equipo de desarrollo es el del versionamiento,
ya que era incontrolable la coherencia entre los cambios realizados 
por más de un colaborador. Las modificaciones y los archivos circulan por email
entre uno y otro, pero sin lograr sistematización y control sobre *quién cambió qué*.
y a *qué versión de GPEC corresponde un determinado código fuente*. 



Problemas detectados
---------------------


.. figure:: images/visual_gpec3.png
   :width: 80%
   
   Ventanas abiertas para obtener un nuevo compuesto desde la base de datos, 
   para que sea listado y utilizable en el sistema. Poco usable. 


.. _metodologia:

Metodología
===========


.. _requerimientos:

Requerimientos 
===============

Requerimientos funcionales
---------------------------

1. 
1. Diagramas 3Dmaqueta de estructura
    * Modelos
    * Gestión de base de datos
    * etc ...

Requerimientos No Funcionales
==============================
