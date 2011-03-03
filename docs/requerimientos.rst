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
:abbr:`PLAPIQUI (Planta Piloto de Ingeniería Química)` durante los años 
2004 y 2005. 

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
las dos partes. Como se verá en breve, esta interfaz de comunicación se ha respetado
(ver `API`_). Asimismo, los datos de salida que producen los algoritmos, son 
leídos por Visual Gpec desde archivos de texto para su posterior 
graficación, que se realiza mediante rutinas desarrolladas *ad hoc* para esta 
implementación. Es decir, no se utiliza en ninguna biblioteca para estos fines. 
de modo que los gráficos se generan mediante el trazado punto a punto sobre un *widget* 
tipo canvas. El control de escala, segmentación y demás funcionalidades básicas 
debió programarse desde cero. 

.. figure:: images/visual_gpec2.png
   :width: 80%
   
   Visualizacion de un diagrama P-T para el sistema Methane-Methanol
   con modelo RK-PR. 

El resultado de esto, si bien es aceptable y funcional, implicó muchas horas de 
desarrollo, con gráficos sólo 2D, poco configurables, que no se pueden 
vectorizar ni exportar. 

Licenciamiento
---------------

*Visual GPEC* no tiene una licencia explicitada pero se trata de 
un *freeware**, es decir, un tipo de software que se distribuye  sin costo y 
está disponible para su uso por tiempo ilimitado. La última versión 
públicamente disponible era la 2.0. 

Hasta el momento, GPEC no es *Software Libre* ni *Open source*, ya que su código 
fuente no está  disponible. 


Aspectos de ingeniería de software
-----------------------------------

Durante su desarrollo anterior, GPEC no adoptó ninguna metodología de 
desarrollo particular, salvo la concerniente a la separación  
funcional de la aplicación como se explica más arriba. 

Un problema manifestado por el equipo de desarrollo es el del versionamiento,
ya que era incontrolable la coherencia entre los cambios realizados 
por más de un colaborador. Las modificaciones y los archivos circulan por email
entre uno y otro, pero sin lograr sistematización y control sobre *quién cambió qué*.
y a *qué versión de GPEC corresponde un determinado código fuente*. 


Problemas detectados
---------------------

Lenguaje
^^^^^^^^

Como se ha mencinado, el programa se codificó en Visual Basic 6, que es un 
lenguaje lanzado en 1998 y ya no es soportado por Microsoft, la empresa 
creadora, proponiendo en su reemplazo .Net, su tecnología más moderna 

Visual Basic es un lenguaje limitado y de poca robustez (sufre un 
problema asociado con varias librerías dinámicas [#]_ ), y con un 
pobre soporte de orientación a objetos, que condiciona la arquitectura de 
cualquier software no trivial a ser engorrosa y poco fiable. 

Asimismo, queda zanjada la posibilidad de contar con una aplicación 
multiplataforma nativa, ya que el lenguaje sólo funciona sobre Windows. 

Calidad de los gráficos
^^^^^^^^^^^^^^^^^^^^^^^
Los gráficos generados, como se ha comentado, no se generan en ningun formato 
de archivo de imágenes (vectorial o mapa de bits), sino que simplemente 
se grafican por pantalla, con una proporción de 1 pixel por punto. La 
información faltante se completa con segmentos de recta. 

Esto acarrea la imposibilidad de exportar la imágen si no es a través de una 
"captura de pantalla", requiriendo al menos un minimo tratamiento de 
recortado y adaptación (por ejemplo del color de fondo, dependiente del "tema" 
de apariencia de Windows configurado por el usuario) con un programa de manipulación de gráficos.

El resultado de esta operación es un mapa de bits carente de calidad 
suficiente para la impresión o la inclusión en un artículo científico, por 
lo que, en general, los usuarios recurren a la obtención de los datos 
numéricos y realizan la graficación con otro software específico como 
Origin o Microsoft Excel. 


Diseño y Usabilidad
^^^^^^^^^^^^^^^^^^^^

Un aspecto poco cuidado de Visual Gpec es su usabilidad, ofreciendo una 
experiencia de usuario anti-intuitiva. 


.. figure:: images/visual_gpec3.png
   :width: 80%
   
   Ventanas abiertas para obtener un nuevo compuesto desde la base de datos, 
   para que sea listado y utilizable en el sistema. Poco usable. 


A primera vista, la pantalla principal ofrece muchisimas opciones que tienden 
a abrumar al usuario inexperto. Muchos componentes de la interfaz, como la 
lista de compuestos, no son necesarios permanentemente, y aun así, sin razón objetiva 
justificable, no todos los compuestos presentes en la base de datos se 
exponen en este selector. En caso de necesitar un compuesto que no esté allí 
listado, el proceso de obtención requiere interacturar con 3 formularios 
distintos. 

Por poner otro ejemplo, el botón principal para el inicio del cálculo 
(|play| ) se encuentra en una barra de herramientas con otras funciones no 
obligatorias para la ejecución. 

.. |play| image:: images/play.png

Base de datos
^^^^^^^^^^^^^

La base de datos está implementada en fomate MS Access y su diseño de tablas 
es complejo innecesariamente, realizando diversas relaciones *One-to-One* con 
una misma clave principal. Por ejemplo, los nombres y las propiedades de un 
compuesto químico se encuentran en tablas separadas. 

.. figure:: images/bbdd.png
   :width: 80%

   Visualización de algunas estructuras y datos de la base de datos de Visual 
   GPEC mediante el utilitario *gmdb2*. 

Sumado a esto, dada la ineficiencia del formato, el archivo de base de datos 
estándar (sin datos extra del usuario)  ocupa *45.2Mb* de espacio en disco. 


.. _metodologia:

Metodología
===========


.. _requerimientos:

Requerimientos 
===============

Requerimientos funcionales
---------------------------

Todas las funcionalidades de la versión preexistente de GPEC deben igualarse y 
en lo posible mejorarse. Se detallan a continuación:


* Generación del sistema binario: selección de dos sustancias. 
* Gestión de de base de datos de constantes de compuestos químicos. Se incluirá una base de datos 
  con el software que el usuario puede manipular.
* Adecuación del formulario y archivo de entrada de parámetros para 
  diferentes ecuaciones de estado (modelos) de base molecular [#]_ : 

     * Soave-Redlich-Kwong 
     * Peng-Robinson
     * RK-PR
     * Simplified Perturbed Hard Chain Theory
     * Perturbed Chain Statistical Associating Fluid Theory (PC-SAFT)

* Generación de suite de gráficos 2-D: 

    * Diagrama de equilibrio de fase global :

      * Presión - Temperatura (P-T)
      * Temperatura - Composición (T-x)
      * Temperatura - Densidad (T-ρ) 
      * Presión - Composición (P-x)
      * Presión - Densidad (P-ρ)

    * Isopletas: diagramas para composición ``Z`` constante (rango definible [0, 1] ):
        
        * Presión - Temperatura (P-T)
        * Temperatura - Composición (T-x)
        * Temperatura - Densidad (T-ρ)
        * Presión - Composición (P-x)
        * Presión - Densidad (P-ρ)

    * Diagramas isotérmicos (Pxy): diagramas para temperatura ``T [K]`` constante [#]_:

        * Presión - Composición (Pxy)
        * Presión - Densidad (P-ρ)

    * Diagramas isobáricos (Txy): diagramas para presión ``P [bar]`` constante :

        * Temperatura - Composición (Txy)
        * Temperatura - Densidad  (T-ρ)

* Generación de suite de gráficos 3-D: diagramas globales y de parámetros constantes 
  automáticamente superpuestos para cada caso:

        * Presión - Temperatura - Composición
        * Presión - Temperatura - Densidad
                
* Superposición de diagramas compatibles
* Gestión de proyectos (manipulación múltiples casos de sistemas/modelo/gráfico) 
* Gestión de persistencia de datos (abrir, guardar, etc.)
* Ejecución multiplataforma: GPEC debe ser capaz de utilizarse en entornos Windows® y Linux
* Exportación de gráficos 

Requerimientos no funcionales
-----------------------------

* GPEC requiere flexibilidad que permita
  la extensibilidad de funcionalidades. Para esto se apunta a una arquitectura 
  lógica modularizada que permita incorporar o extender funcionalidades de manera 
  accesible. 
* Manipulación de gráficos accesible: zoom, rotación, desplazamiento, ocultación de curvas, etc.
* Calidad y formatos de gráficos válidos para publicaciones científicas
* Configurabilidad de aspecto de los gráficos
* Usabilidad y claridad de las interfaces: debe poder usarse intuitivamente


.. [#]  Este problema es conocido como *DLL Hell* (infierno de las DLL). Ver 
        http://es.wikipedia.org/wiki/DLL_Hell

.. [#]  Para la parametrización de los datos de entrada para cada ecuación de 
        estado fue menenester documentar la :ref:`api`.

.. [#]  La validación de los rangos dinámicos (dependen de las constantes críticas
        de los compuestos del sistema) la realizan los algoritmos de cálculo. El frontend
        se limita a reportar un error en la obtención de los datos de salida. 
