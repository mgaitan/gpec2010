.. header::
   Propuesta de Proyecto Integrador - Martín Gaitán

.. footer::
    ###Page###




*******************
Proyecto Preliminar
*******************

    :Fecha: 22-jun-2010
    :revision: 16
    :Autor: Martín Emilio Gaitán    
    :Email: gaitan@gmail.com



.. contents::

.. section-numbering::

.. raw:: pdf

   PageBreak oneColumn



Introducción 
============


GPEC, *Global Phase Equilibrium Calculations*, es un software científico que 
permite la obtención de curvas de equilibro global entre fases fluidas y otros diagramas 
termodinámicos para sistemas binarios, que se calculan mediante ecuaciones 
de estado termodinámicas. Es útil para fines educativos, académicos, científicos y de desarrollo industrial. 

GPEC fue desarrollado originalmente por el Dr. Martín Cismondi Duarte en el marco
de su tesis doctoral en Ingeniería Química por la Universidad Técnica de Dinamarca, 
en 2005, y luego ampliado y mantenido junto a Diego Nuñez.

Está basado en métodos numéricos y algoritmos desarrollados principalmente por Cismondi 
en colaboración con el Prof. Michael Michelsen, del Department of Chemical Engineering, 
DTU (Dinamarca),  y el Prof. Marcelo Zabaloy de la Universidad Nacional del Sur, 
(Argentina). 

Actualmente es un proyecto dirigido por el Prof. Esteban Brignole de `PLAPIQUI <http://www.plapiqui.edu.ar/>`_
(Conicet) en colaboración con el `IDTQ <http://idqt.efn.uncor.edu>`_, en la FCEFyN-UNC. 

Este documento explaya brevemente el relevamiento del software actual y los motivos
que determinan la necesidad de rediseñarlo y redesarrollarlo bajo una nueva
arquitectura, labor que se propone como Proyecto Integrador (PI) para final de carrera
de grado en Ingeniería en Computación.

Dirección y seguimiento del Proyecto Integrador
-----------------------------------------------

Este PI estará dirigido por el **Prof. Gustavo Wolfmann**, titular de la 
cátedra *Algoritmos y Estructuras de datos*  y *Paradigmas de Programación*, 
de Ingeniería en Computación, en el rol de **Director del Proyecto**, y por 
el Dr. `Martín Cismondi <http://idtq.efn.uncor.edu/Martin-Cismondi-Duarte>`_ , 
profesor de la cátedra *Termodinámica Química* de la carrera Ingeniería Química e investigador de Conicet, 
como Co-director. 


Relevamiento
============


Estado actual
-------------

La versión actual de GPEC es la 2.0  y que se encuentra disponible gratuitamente  
en http://gpec.efn.uncor.edu/, permite calcular y mostrar las siguientes curvas:

 * Diagrama de equilibrio de fase global en diferentes proyecciones
 * Diagramas Pxy para temperatura constante 
 * Txy para presión constante

Además, permite utilizar 6 ecuaciones de estado diferentes:

 * Soave-Redlich-Kwong EOS (Soave, 1972)
 * Peng-Robinson EOS (Peng and Robinson, 1976)
 * RK-PR EOS (Cismondi and Mollerup, 2005)
 * Simplified Perturbed Hard Chain Theory EOS (Kim et al., 1986)
 * Perturbed Chain Statistical Associating Fluid Theory (Gross
   and Sadowski, 2001)
 * Group Contribution Equation of State (Skjold Jørgensen, 1984)


Aspectos técnicos
-----------------

GPEC es una aplicación para entornos Microsoft Windows (Windows 2000, Windows XP 
o superior) desarrollada en una arquitectura de dos bloques funcionales:

#.  **Interfaz de usuario, validación y graficación**, desarrolla en Visual Basic
#.  **Cálculos e implementación de algoritmos numéricos**, desarrollados en Fortran

Esta arquitectura respondió a la necesidad de separar el desarrollo de un 
*"Gpec visual"* (que desarrolló principalmente el programador Diego Nuñez), 
aislado del desarrollo, mantenimiento e implementación de nuevos algoritmos y 
ecuaciones de estado, tarea en la que el Dr. Cismondi se ha desenvuelto hasta la actualidad

La interfaz visual de GPEC presenta al usuario una GUI para interactuar con los 
distintos parámetros del diagrama elegido, envía los parámetros a los algoritmos
de cálculo, y procesa las salidas de estos mostrando las curvas. 

La comunicación con los algoritmos implementados en Fortran se realiza mediante
archivos de texto plano en un formato cuya estructura *ad hoc* que es comprendida 
y decodificada por las dos partes. Asimismo, los datos de salida que producen los algoritmos, son 
leídos por Visual Gpec desde archivos de texto para su posterior graficación. 

Dicha graficación se realiza con procedimientos realizados específicamente para esta 
implementación, habiendo programado rutinas para realizar los gráficos a un nivel
de abstracción muy bajo (punto a punto, sobre un widget tipo canvas).

El resultado de esto, si bien es aceptable y funcional, implicó muchas horas de 
desarrollo, con gráficos poco configurables y de baja calidad visual.  


Aspectos de Ingeniería de Software
----------------------------------
GPEC no ha adoptado ninguna metodología de desarrollo hasta el momento, 
salvo la concerniente a la separación  funcional de la aplicación. 

Un problema manifestado por el equipo de desarrollo es el del versionamiento,
ya que era incontrolable la coherencia entre los cambios realizados 
por más de un colaborador. Las modificaciones y los archivos circulan por email
entre uno y otro, pero sin lograr sistematización y control sobre *quién cambió qué*.
y a *qué versión de GPEC corresponde un determinado código fuente*. 

Aspectos de licenciamiento
--------------------------

La versión actual de GPEC no tiene una licencia explicitada pero se trata de 
un *freeware**, es decir, un tipo de software que se distribuye  sin costo y 
está disponible para su uso por tiempo ilimitado. 

Hasta el momento, GPEC no es Software Libre ni Opensource, ya que su código 
fuente no está  disponible. 


La necesidad de rediseñar GPEC
==============================

GPEC es un software que goza de cierta popularidad en el ambiente científico 
e industrial. 

Hasta el momento no se conoce ningún otro software con capacidades iguales o equivalentes, por lo que 
GPEC cuenta con una creciente comunidad de usuarios,  en la mayor parte de Europa, 
EE.UU., Asia y América Latina, pertenecientes  no sólo a instituciones académicas 
y de investigación, si no también a industrias.

Aunque las potencialidades técnicas, científicas e incluso comerciales son muy grandes, 
dos factores han sido determinantes para el virtual congelamiento de su desarrollo: 

* La falta de recursos técnicos especializados en el desarrollo de software
* El diseño poco modularizado de su arquitectura, que vuelve ineficiente su mantenimiento
  y extensibilidad

Otros aspectos negativos a destacar tienen que ver con el uso del lenguaje:
Visual Basic es un lenguaje obsoleto, no sólo por discontinuación [1] por 
parte de Microsoft, sino por su carente orientación a objetos y su permisividad
para malas prácticas de programación. Además, las aplicaciones escritas en 
Visual Basic sólo corren sobre plataforma Windows. 

Proyectando un nuevo GPEC
=========================

Si bien las proyecciones y funcionalidades incorporables a GPEC son vastas, 
los requerimientos enmarcados dentro del proyecto integrador serán acotados a un 
*rediseño integral de la arquitectura*, manteniendo compatibilidad y separación funcional con los algoritmos
de cálculo numérico desarrollados en Fortran.  

Los requerimientos a implementar detallados aqui, son requerimientos *de mínima*, 
es decir, que podrán ser ampliados durante el desarrollo del nuevo sistema, en función 
de la disponibilidad de tiempo y los avances logrados. 


Requerimientos funcionales
--------------------------

* Gestión de Alta-Baja-Modificación de compuestos químicos. Se incluirá una base de datos 
  con el software que el usuario puede manipular. 
* Generación del sistema binario: selección de dos sustancias. 
* Parametrización automatizada y manual 
* Cálculo de seis ecuaciones de estado (modelos) de base molecular: 

     * Soave-Redlich-Kwong EOS 
     * Peng-Robinson EOS 
     * RK-PR EOS 
     * Simplified Perturbed Hard Chain Theory EOS
     * Perturbed Chain Statistical Associating Fluid Theory 
     * Group Contribution Equation of State 

* Generación de suite de gráficos 2-D: 

    * Gráficos de fase global en 5 distintos cortes: Presión vs. Temperatura, 
      Temperatura vs. Composición, Temperatura vs. Densidad, Presión 
      vs. Composición, Presión vs. Densidad 
    * Diagramas Pxy, Txy, isopletas para una variable fija

* Gestión de proyectos (manipulación múltiples casos de sistemas/modelo/gráfico) 
* Gestión de persistencia de datos (abrir, guardar, etc.)
* Ejecución multiplataforma: GPEC debe ser capaz de utilizarse en entornos Windows y Linux
* Exportación de datos. Los cálculos y gráficos efectuados por GPEC deben ser 
  exportables a múltiples formatos


Requerimientos no funcionales
-----------------------------

* GPEC requiere  “flexibilidad modular” que permita
  la extensibilidad de funcionalidades. Para esto se apunta a una arquitectura
  *pluggable* que permita incorporar módulos para nuevas ecuaciones de estado
* Configurabilidad de aspecto de los gráficos
* Usabilidad y claridad de las interfaces



Rediseño y refactorización
==========================

Se propone un rediseño de la arquitectura de GPEC que mantenga la separación lógica
entre los algoritmos de cálculo numérico desarrollados e implementados en Fortran
por el Dr. Cismondi, pero que satisfaga los requerimientos y la modularidad 
deseada. 

Patrones de diseño
-------------------

Aplicando técnicas propuestas por Joshua Kerievsky en su libro `Refactoring to Pattern 
<http://www.industriallogic.com/xp/refactoring/>`_ se propone refactorizar 
el diseño de la aplicación existente a la utilización de patrones de diseño de 
software. 

La nueva arquitectura de GPEC estará basada en un patrón de diseño 
`Modelo Vista Controlador <http://es.wikipedia.org/wiki/Modelo_Vista_Controlador>`_
que separa los datos de una aplicación, la interfaz de usuario, y la lógica de 
control en tres componentes distintos. 

..  image:: images/mvc.png
    :align: center

Asimismo, se pretende utilizar el patrón *Pluggable Adapter* como arquitectura
base para la extensibilidad del software. 


Tecnologías a utilizar
=======================

Lenguaje de programación 
------------------------

`Python <http://www.python.org>`_ es un lenguaje de programación interpretado, 
interactivo y orientado a objetos. Incorpora módulos, excepciones, tipado dinámico, 
tipos de datos dinámicos de muy alto nivel, y clases.  Python combina un remarcable poder con una sintaxis muy clara. 
Tiene interfaces a muchas llamadas al sistema y bibliotecas, así como también a 
varios gestores de ventanas, y es extensible en C o C++. 
También es utilizable como un lenguaje de extensión para aplicaciones que 
necesiten interfaces programables. Finalmente, Python es portable, 
corre en muchas variantes de Unix, Mac, y en PCs bajo MS-DOS, Windows, Windows NT, y OS/2.

Es software libre y un lenguaje muy popular y cada vez más adoptado en el mundo
académico y empresarial. 

Biblioteca de graficación en 2D
-------------------------------

`Matplotlib <http://matplotlib.sourceforce.net>`_ 
es una biblioteca para la generación de gráficos con calidad de publicación 
académica, en múltiples formatos de salida, y en diferentes entornos como 
un simple script python, en la consola interactiva (al estilo Matlab), en 
aplicaciones web del lado del servidor y a través de diferentes toolkits de 
interfaz gráfica.

Una galería de gráficos producidos con esta biblioteca puede encontrarse en 
`este vínculo <http://matplotlib.sourceforge.net/gallery.html>`_.

Matplotlib es software libre basado en la licencia GNU GPL v2

Toolkit de interfaz gráfica de usuario
--------------------------------------

`wxWidgets <http://www.wxwindows.org/>`_ es una biblioteca en C++ que permite 
desarrollar interfaces gr ficas para aplicaciones multiplataforma que corren
en Windows, OS X, Linux o UNIX de 32 o 64 bits. 

`wxPython <http://www.wxpython.org/>`_ es un binding de la biblioteca wxWidgets 
para el lenguaje de programación Python. Junto a Python permite el desarrollo 
rápido de aplicaciones gráficas multiplataforma.

Una de las características sobresalientes de wxWidgets es su uso nativo de 
las API's gráficas de cada entorno de ventanas, brindando una apariencia y experiencia
de uso nativa para cada ambiente. Es decir: la misma aplicación se ve como *una aplicación Windows*
si se corre en Windows o como un *aplicación GNOME* si se corre sobre el gestor 
de escritorio GNOME en Linux. 

Herramienta de documentación
----------------------------

Sphinx_ es una herramienta que permite la generación
de documentación de manera inteligente y visualmente agradable. 
Se basa en el lenguaje de marcado reStructuredText_ cuya principal ventaja es 
su exportación a diferentes formatos como html, latex, odf, etc. respetando
la semántica del documento mientras mantiene una alta legibilidad en formato 
fuente (texto plano). 

Como ejemplo, este documento ha sido escrito con Sphinx y exportado a PDF a través de Latex.

.. _Sphinx: http://sphinx.pocoo.org/ 
.. _reStructuredText: http://docutils.sourceforge.net/rst.html


Metodologías a implementar
==========================

El desarrollo de GPEC estará basado en práctica comunes en el paradigma denominado 
`Metodologías ágiles <http://es.wikipedia.org/wiki/Desarrollo_%C3%A1gil_de_software>`_. 
Esto incluye el prototipado, desarrollo guiado por pruebas, auto-documentación, 
simplicidad y modularización.

Se pretende poner énfasis en la adaptabilidad por sobre la previsibilidad del sistema. 

Gestión de proyecto
-------------------

Sistematizar la gestión del proyecto de software se hace imprescindible. Esto 
abarca los siguientes aspectos. 

Para esta tarea se utilizará el software `Trac <http://trac.edgewall.org/>`_
instalado en http://pi.nqnwebs.com .

Trac es un sistema web libre para la gestión de proyectos y seguimiento de errores
que se integra con el sistema de control de versiones Subversion


Documentación
^^^^^^^^^^^^^
Una sistematización del estado y evolución del nuevo desarrollo se hace imprescindible. 
Centralizar la documentación, relevamiento de requerimientos e información 
precisa del avance logrado en determinado momento. 

Trac cuenta con un sistema Wiki integrado que permite control de cambios y 
fácil formateo de la documentación

Control de versiones de código
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Es menester la utilización de un sistema de control de versiones que permita dilucidar con 
exactitud las modificaciones realizadas entre dos momentos del desarrollo y permita
*volver* a una versión anterior. 

Para un proyecto de la envergadura de GPEC, `Subversion <http://subversion.apache.org>`_
es suficiente, y facilita la integración con Trac.

Desarrollo dirigido por pruebas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Un desarrollo dirigido por pruebas se basa en la detección automatizada de bugs. 
Sistematizar esta detección y la posterior evolución hasta la eliminación del 
defecto es indispensable. 

Trac incorpora un sistema de seguimiento de bugs que permite categorización, comentarios,
vínculos cruzados con revisiones de código y múltiples posibilidades de filtrado. 

Plan de trabajo
===============

Cronograma tentativo
--------------------

Semana 1 a 4 
^^^^^^^^^^^^
- Relevamiento del estado actual
- Estudio de factibilidad 
- Rediseño arquitectónico 
- Informe de proyecto 
- Lectura de bibliografía

Semana 5 - 7
^^^^^^^^^^^^

- Estudio de la API de comunicación (archivos de entrada y salida)
- Parser de datos de salida y rutinas de conversión a arrays de NumPy 
- Prototipo de graficación (sin GUI) de archivos de salida para algunos digramas 
  de fase
- Prototipo de interfaz GUI
- Testing estático


Semana 8 - 10
^^^^^^^^^^^^^
- Mejora de interfaz GUI. Gestión de proyectos.
- Modelo de base de datos
- Arquitectura "enchufable" de módulos. Plugins. 
- Formularios de entrada
- Testing: pruebas unitarias automatizadas

Semana 11 - 13
^^^^^^^^^^^^^^
- Configuración y manipulación de gráficos
- Exportación de datos
- Implementación de otras ecuaciones de estado
- Revisión
- Testing

Semana 14 - 15
^^^^^^^^^^^^^^
- Testing y debugging
- Release Beta


Bibliografía
============

Python 
------

- *Expert Python programming*, Tarek Ziadé,  Pack Publishing, 2009
- *wxPython in Action*, Noel Rappin and Robin Dunn, Manning Publications, 2006
- *Matplotlib for Python Developers, Build remarkable publication 
  quality plots the easy way*, Sandro Tosi, Pack Publishing, 2009
- *The Python Standard Library Documentation*, Python Foundation, http://docs.python.org/library/
- *Learning Python 4th edition*, Mark Lutz, O'Really, 2009
- *Tutorial wxPython + wxGlade*, John Alexis Guerra Gómez
- *Matplotlib documentation*, John Hunter, Darren Dale and Michael Droettboom, http://matplotlib.sourceforge.net/contents.html

Ingeniería en Software
----------------------
- *Refactoring to Pattern*. Joshua Kerievsky, Addison Wesley, 2004
- *Engineering the User Interface From Research to Practice*, Miguel Redondo, Crescencio Bravo 
  y Manuel Ortega, Springer Science, 
- *El testing como parte del proceso de calidad del software*, Departamento de 
  Testing del Instituto Nacional de Tecnología Industrial - Sede Córdoba, INTI, 2010

Diseño de GUI
-------------
- *GUI Bloopers 2.0 Common User Interface Design Don'ts and Dos*,  Jeff Johnson, Morgan Kaufmann Publishers, 2008
-   


