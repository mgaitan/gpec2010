*******
GPEC v2
*******

Introducción para Gustavo
=========================

GPEC es un software científico de uso gratuito que permite la obtención de diagramas de equilibro 
entre fases fluídas y otros diagramas termodinámicos para sistemas binarios, que se calculan mediante 
ecuaciones de estado. Es útil para fines educativos, académicos y de 
desarrollo industrial. 

GPEC fue desarrollado originalmente por el Dr. Martín Cismondi Duarte en el marco
de su tésis doctoral en la Universidad Técnica de Dinamarca, en 2005, y luego
ampliada y mantenida junto a Diego Nuñez.

Está basado en métodos y algoritmos desarrollados principalmente por Cismondi 
en colaboración con el Prof. Michael Michelsen y el Prof. Marcelo Zabaloy de 
la UNS-PLAPIQUI. 

Actualmente es un proyecto dirigido por el Prof. Esteban Brignole de PLAPIQUI
(Conicet) en colaboración con el `IDTQ <http://idqt.efn.uncor.edu>`_, en la FCEFyN-UNC. 


Relevamiento
============

Estado actual
-------------

La versión de GPEC v2.0 `disponible públicamente <http://gpec.efn.uncor.edu/spip.php?page=download>`_
, a la fecha permite calcular y mostrar los siguientes diagramas:

 * Diagrama de equilibrio de fase global en diferentes proyecciones
 * Diagramas Pxy para temperatura constante 
 * Txy para presión constante

Además, permite utilizar 6 ecuaciones de estado diferentes:

 * SRK o Soave-Redlich-Kwong EOS (Soave, 1972)
 * PR o Peng-Robinson EOS (Peng and Robinson, 1976)
 * RK-PR EOS (Cismondi and Mollerup, 2005)
 * SPHCT o Simplified Perturbed Hard Chain Theory EOS (Kim et al., 1986)
 * PC-SAFT o Perturbed Chain Statistical Associating Fluid Theory (Gross
   and Sadowski, 2001)
 * GC-EOS o Group Contribution Equation of State (Skjold Jørgensen, 1984)



Aspectos técnicos
-----------------

GPEC es una aplicación para entornos Microsoft Windows (Windows 2000, Windows XP 
o superior) desarrollada en una arquitectura de dos bloques de funcionalidades

#.  **Interfaz de usuario, validación y graficación**, desarrolla en Visual Basic
#.  **Cálculos e implementación de algoritmos numéricos**, desarrollados en Fortran

Esta arquitectura respondió a la necesidad de separar el desarrollo de un 
*"Gpec visual"* (que desarrolló principalmente el programador Diego Nuñez), 
aislado del desarrollo, mantenimiento e implementación de nuevos algoritmos y 
ecuaciones de estado, tarea en la que el Dr. Cismondi se ha desenvuelto hasta la actualidad

Visual Gpec
^^^^^^^^^^^

La interfaz visual de GPEC presenta al usuario una GUI para interactuar con los 
distintos parámetros del digrama elegido, envía los parámetros a los algoritmos
de cálculo, y procesa las salidas de estos mostrando los diagramas. 

La comunicación con los algoritmos implementados en Fortran se realiza mediante
archivos de texto plano en un formato cuya estructura es comprendida y decodificada por las 
dos partes. Asimismo, los datos de salida que producen los algoritmos, son 
leídos por Visual Gpec desde archivos de texto para su posterior graficación. 

Dicha graficación se realiza con procedimientos realizados *ad hoc* para esta 
implementación, habiendo programado rutinas para realizar los gráficos a un nivel
de abstracción muy bajo (punto a punto, sobre un widget tipo canvas).

El resultado de esto, si bien es aceptable y funcional, implicó muchas horas de 
desarrollo, con gráficos poco configurables y de baja calidad visual.  


Aspectos de Ingeniería de Software
----------------------------------
Gpec no ha adotado ninguna metodología de desarrollo hasta el momento, 
salvo la concerniente a la separación  funcional *ad hoc* de la aplicación. 

Un problema manifestado por el equipo de desarrollo es el del versionamiento,
ya que era incontrolable la coherencia entre los cambios realizados 
por más de un colaborador. Las modificaciones y los archivos circulan por email
entre uno y otro, pero sin lograr sistematización y control sobre *quién cambió qué*.
y a *qué versón de GPEC corresponde un determinado código fuente*. 

Aspectos de licenciamiento
--------------------------

La versión actual de GPEC no tiene una licencia explicitada pero se trata de 
un *freeware**, es decir, un tipo de software de computadora que se distribuye 
sin costo y está disponible para su uso por tiempo ilimitado. 

Hasta el momento, GPEC no es Software Libre ni Opensource, ya que su código 
fuente no está  disponible. 


*********
GPEC 2010
*********

La necesidad de rediseñar GPEC
==============================

Gpec es un software que goza de cierta popularidad en el ambiente científico 
e industrial. 

Hasta el momento no se conoce ningún otro software con capacidades iguales o equivalentes, por lo que 
GPEC cuenta con una creciente comunidad de usuarios,  en la mayor parte de Europa, 
EEUU, Asia y América Latina, pertenecientes  no sólo a instituciones académicas 
y de investigación, si no también a industrias.

Aunque las potencialidades técnicas, científicas e incluso comerciales son muy grandes, 
dos factores han sido determinantes para el virtual congelamiento de su desarrollo: 

* La falta de recursos técnicos especializados en el desarrollo de software
* El diseño poco modularizado de su arquitectura, que vuelve ineficiente su mantenimiento
  y ampliación

Otros aspectos negativos a destacar tienen que ver con el uso del lenguaje:
Visual Basic es un lenguaje obsoleto, no sólo por discontinuación [1] por 
parte de Microsoft, sino por su carente orientación a objetos y su permisividad
para malas prácticas de programación. Además, las aplicaciones escritas en 
Visual Basic sólo corren sobre plataforma Windows. 

Proyectando un nuevo GPEC
=========================

En el marco del Proyecto Integrador para la obtención del título de grado 
en Ingeniería en Computación, me he sumado al desarrollo de GPEC. 

Si bien las proyecciones sobre GPEC son vastas, los requerimientos enmarcados
dentro del proyecto integrador serán acotados a un rediseño integral de la arquitectura
del *GPEC Visual*, manteniendo compatibilidad y separación funcional con los algoritmos
de cálculo numérico desarrollados en Fortran.  

Requerimientos funcionales
--------------------------
Para una primera etapa, se prevén los siguientes requerimientos

- Seis ecuaciones de estado (modelos) de base molecular: SRK, PR, RK-PR, SPHCT, ESD, PC-SAFT.
- Tanto QMR (Quadratic Mixing Rules) como CMR (Cubic Mixing Rules) para los tres primeros modelos.
- Diagramas globales en 2-D: P-T, T-x, P-x…
- Diagramas Pxy, Txy, isopletas. 
- Funcionalidades genéricas (abrir, guardar, deshacer, etc)

Para etapas posteriores 


Requerimientos no funcionales
-----------------------------

- La nueva arquitectura de GPEC requiere  “flexibilidad modular” que permita
  la personalización de las funcionalidades provistas. 
- Usabilidad  
- Calidad visual de los digramas


Rediseño y refactorización
==========================

Se propone un rediseño de la arquitectura de GPEC que mantenga la separación lógica
entre los algoritmos de cálculo numérico desarrollados e implementados en Fortran
por el Dr. Cismondi, pero que satisfaga los requerimientos y la modularidad 
deseada. 

Patrón de diseño
----------------

La nueva arquitectura de GPEC estará basada en un patrón de diseño 
`Modelo Vista Controlador <http://es.wikipedia.org/wiki/Modelo_Vista_Controlador>`_
que separa los datos de una aplicación, la interfaz de usuario, y la lógica de 
control en tres componentes distintos. 

..  image:: images/mvc.png
    :align: center



Técnologías a utilizar
=======================

Lenguaje de programación 
------------------------

`Python <http://www.python.org>`_ es un lenguaje de programación interpretado, 
interactivo y orientado a objetos. Incorpora módulos, excepciones, tipado dinámico, tipos de datos dinámicos de 
muy alto nivel, y clases.  Python combina un remarcable poder con una sintáxis muy clara. 
Tiene interfaces a muchas llamadas al sistema y bibliotecas, así como tambien a 
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
desarrollar interfaces gráficar para aplicaciones multiplataformas que corren
en Windows, OS X, Linux o UNIX de 32 o 64 bits. 

`wxPython <http://www.wxpython.org/>`_ es un binding de la biblioteca wxWidgets 
para el lenguaje de programación Python. Junto a Python permite el desarrollo 
rápido de aplicaciones gráficas multiplataforma.

Una de las caracteristicas sobresalientes de wxWidgets es su uso nativo de 
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


Metologías a implementar
========================

El desarrollo de GPEC estará basado en práctica comunes en el paradigma denominado 
`Metologías ágiles <http://es.wikipedia.org/wiki/Desarrollo_%C3%A1gil_de_software>`_. Esto incluye el prototipado, desarrollo guiado por pruebas, autodocumentación, simplicidad y modularización.

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
- Relevamiento del estado actual (*realizado*) 
- Estudio de factibilidad (*realizado*)
- Rediseño arquitectónico (*realizado*)
- Informe de proyecto (*realizado*)
- Lectura de bibliografía (en curso)

Semana 5 - 7
^^^^^^^^^^^^

- Estudio de la API de comunicación (archivos de entrada y salida)
- Parser de datos de salida y rutinas de conversión a arrays de NumPy 
- Prototipo de graficación (sin GUI) de archivos de salida para algunos digramas 
  de fase
- Prototipo elemental de interfaz GUI
- Testing estático


Semana 8 - 10
^^^^^^^^^^^^^
- Mejora de interfaz GUI
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


Bibliografía a consultar
========================

- *Matplotlib for Python Developers, Build remarkable publication 
  quality plots the easy way*, Sandro Tosi, Pack Publishing, 2009
- *El testing como parte del proceso de calidad del software*, Departamento de 
  Testing del Instituto Nacional de Tecnología Industrial - Sede Córdoba, INTI, 2010
- *wxPython in Action*, Noel Rappin and Robin Dunn, Manning Publications, 2006
- *Tutorial wxPython + wxGlade*, John Alexis Guerra Gómez
- *Expert Python programming*, Tarek Ziadé,  Pack Publishing, 2009
- *The Python Standard Library Documentation*, Python Foundation, http://docs.python.org/library/
- *Learning Python 4th edition*, Mark Lutz, O'Really, 2009
- *Matplotlib documentation*, John Hunter, Darren Dale and Michael Droettboom, http://matplotlib.sourceforge.net/contents.html
  
