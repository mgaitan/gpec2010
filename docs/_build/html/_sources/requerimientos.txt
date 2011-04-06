Ingeniería de requerimientos
*****************************

Metodología de relevamiento
===========================

Para el relevamiento de requerimientos se realizaron entrevistas informales 
con el comitente, una evaluación exhaustiva de la versión preexistente y, 
basado en el modelo de :ref:`desarrollo` (que se explica 
en :ref:`marco`), sucesivas presentaciones de prototipos que se 
fueron adaptando según las observaciones de la parte interesada. 

Además se utilizó un *issue tracker* para permitir que los usuarios 
adviertan de errores en la versión en desarrollo o propongan mejoras o nuevas 
funcionalidades. 

El proceso de relevamiento incluyó entrevistas con el desarrollador de *Visual 
Gpec* y con investigadores de :abbr:`PLAPIQUI` involucrados, como 
desarrolladores o usuarios, en GPEC. 

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
  Dr. Marcelo Zabaloy y la supervisión del Dr. Esteban Brignole, 

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
archivos de texto plano en un formato cuya estructura *ad hoc* es bien conocida por 
las dos partes. Como se verá en breve, esta interfaz de comunicación se ha respetado
(ver :ref:`api`). Asimismo, los datos de salida que producen los algoritmos, son 
leídos por Visual Gpec desde archivos de texto para su posterior 
graficación, que se realiza, segun manifestó el comitente, mediante rutinas desarrolladas *ad hoc* para esta implementación. Es decir, no se utiliza en ninguna biblioteca para estos fines, 
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

Según surge de las entrevistas realizadas, durante su desarrollo anterior, GPEC no adoptó ninguna metodología particular, salvo la concerniente a la separación  
funcional de la aplicación como se explicó anteriormente. 

Un problema manifestado por el equipo de desarrollo es el del versionamiento,
ya que era incontrolable la coherencia entre los cambios realizados 
por más de un colaborador. Las modificaciones y los archivos circulaban por email
entre uno y otro, pero sin lograr sistematización y control sobre *quién cambió qué*.
y a *qué versión de GPEC corresponde un determinado código fuente*. 

.. _problemas:

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

Esto acarrea la imposibilidad de exportar la imagen si no es a través de una 
"captura de pantalla", requiriendo al menos un mínimo tratamiento de 
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
   para que sea listado y utilizable en el sistema. 


A primera vista, la pantalla principal ofrece muchísimas opciones que tienden 
a abrumar al usuario inexperto. Muchos componentes de la interfaz, como la 
lista de compuestos, no son necesarios permanentemente, y aun así, sin razón objetiva 
justificable, no todos los compuestos presentes en la base de datos se 
exponen en este selector. En caso de necesitar un compuesto que no esté allí 
listado, el proceso de obtención requiere interacturar con 3 formularios 
distintos. 

Por poner otro ejemplo, el botón principal para el inicio del cálculo 
(|play| ) se encuentra en una barra de herramientas con otras funciones no 
obligatorias para la ejecución. Es decir, las herramientas carecen de un contexto
que facilite la ubicuidad. 

.. |play| image:: images/play.png

Base de datos
^^^^^^^^^^^^^

La base de datos está implementada en formato Microsoft Jet [#]_ y su diseño de tablas 
es complejo innecesariamente, realizando diversas relaciones *One-to-One* con 
una misma clave principal. Por ejemplo, los nombres y las propiedades de un 
compuesto químico se encuentran en tablas separadas. 

.. figure:: images/bbdd.png
   :width: 80%

   Visualización de algunas estructuras y datos de la base de Visual 
   GPEC mediante el utilitario *gmdb2*. 

Sumado a esto, dada la ineficiencia del formato, el archivo de base de datos 
estándar (sin datos extras agregados por el usuario) ocupa *45.2Mb* 
de espacio en disco. 



.. _requerimientos:

Especificación de requerimientos 
==================================

Requerimientos funcionales
---------------------------

Todas las funcionalidades de la versión preexistente de GPEC deben igualarse y 
en lo posible mejorarse. Se detallan a continuación:


* Generación del sistema binario: selección de dos sustancias. 
* Gestión de base de datos de constantes de compuestos químicos. Se incluirá una base de datos 
  con el software que el usuario puede manipular.
* Adecuación del formulario y archivo de entrada de parámetros para 
  diferentes ecuaciones de estado (modelos) de base molecular [#]_ : 

     * Soave-Redlich-Kwong 
     * Peng-Robinson
     * RK-PR
     * Simplified Perturbed Hard Chain Theory
     * Perturbed Chain Statistical Associating Fluid Theory (PC-SAFT)

* Generación de suite de gráficos 2-D: 

    * Diagrama global de equilibrio de fases:

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

* GPEC requiere flexibilidad que permita la extensibilidad de funcionalidades. 
  Para esto se apunta a una arquitectura lógica modularizada que permita 
  incorporar o extender funcionalidades de manera accesible. 
* Manipulación de gráficos accesible: zoom, rotación, desplazamiento, ocultación de curvas, etc.
* Calidad y formatos de gráficos válidos para publicaciones científicas
* Configurabilidad de aspecto de los gráficos
* Usabilidad y claridad de las interfaces: debe poder usarse intuitivamente


Requerimientos especiales
==========================

Se especifican en esta sección, de manera no formal, un conjunto de requerimientos 
de especial interés para el diseño del software. 

Un proyecto, muchos casos
-------------------------

Una tarea frecuente del usuario (investigador) es la comparación entre 
distintos "casos" de estudio. Esto puede ser, un mismo sistema binario con 
aplicando diferentes coeficientes, las mismas condiciones con diferentes 
modelo de cálculo, o bien directamente distintos sistemas. 

Es decir que debe existir el concepto de **proyecto** como un conjunto de 
múltiples **casos**, gestionados desde una misma interfaz de usuario. 


    .. note:: 
      
       Dado que se presta a confusión, vale reiterar que **caso** en el contexto 
       es la conjunción de un sistema binario, un 
       modelo de cálculo (ecuación de estado) y sus respectivos 
       parámetros, y **caso de uso** refiere al ámbito de la 
       ingeniería de software y se trata de una técnica para 
       dilucidad requerimientos y comportamientos esperados del sistema. 
            

Gráficos en 3D
---------------

La información resultante de los cálculos brinda conjuntos (vectores) de datos para 
múltiples variables (presión, temperatura, composición, densidad, etc) 
Tomando tres vectores de datos en vez de dos, pueden graficarse diagramas 3D, 
(por ejemplo *P-T-composición*) sin necesidad de alterar el backend de manera 
alguna. Esta funcionalidad debe soportarse en la nueva implementación.

Superposición automática
------------------------

Dada la visualización 3D, es común que el investigador desee 
superponer diagramas de línea de contorno (isobaras, isopletas, etc.) sobre 
el diagrama de fase global del mismo caso para ver su disposición tridimensional. 

Este comportamiento debe ser automático. Es decir, cualquiera sea el diagrama 
solicitado, debe generar un diagrama 2D independiente y trazar estas mismas 
curvas sobre un diagrama 3D común para todo el caso. 

Superposición manual
--------------------

El usuario puede necesitar superponer visualmente diagramas 2D, ya sean estos 
del mismo caso (por ejemplo, un diagrama P-T global con una isopleta) o bien 
de distintos casos (por ejemplo, diagramas PT correspondientes a distintas 
mezclas)

Validación de orden del sistema
-------------------------------

En la definición de un sistema binario el usuario puede elegir cualesquiera
dos compuestos de la base de datos, sin importar el orden. 
A los fines del cálculo, es necesario disponer el compuesto más liviano, 
en términos termodinámicos, para que el resultado sea válido. La determinación 
de esta condición debe validarse, y en caso necesario, invertir el orden de compuestos
dado por el usuario. El sistema es válido si se cumple que la "función peso" [#]_
del compuesto 1 es menor a la del compuesto 2, es decir: 

    .. math::

       \frac{T_{c_{1}}^{14}}{P_{c_{1}}} < \frac{T_{c_{2}}^{14}}{P_{c_{2}}} 



Casos de uso
=============

Se describen a continuación los casos de uso más relevantes del sistema. 
Basado en lo expuesto en la sección :ref:`anti-uml` no se realiza una enumeración minuciosa 
de las condiciones de contexto, flujos alternativos, etc. y en cambio 
se describen en un formato asociado a *historias de usuario* [#]_


Definir caso de estudio
-----------------------

El usuario define un caso (Figura :ref:`defcaso-num`) mediante la conjunción de la definición de un sistema 
químico binario (dos compuestos), la definición de un modelo de cálculo (de 
las 5 disponibles) y el cálculo o definición de los parámetros. 

.. _defcaso-num:

.. figure:: images/uc-DefinirCaso.png
   :width: 80%

   Caso de uso: definición de un caso de estudio en GPEC

Graficar diagramas
------------------

Una vez definido el sistema el usuario solicita la graficación 
de los diagramas (Figura :ref:`grafdiag-num`) para lo cual el sistema los calcula. 
Independientemente de la suite de diagramas solicitados por el usuario 
el cálculo de los diagramas globales es precedente. 

.. _grafdiag-num:

.. figure:: images/uc-GraficarDiagramas.png
   :width: 80%

   Caso de uso: graficación de diagramas

Definir sistema
---------------

En este caso de uso se produce la interacción del usuario con la base de datos. 
Como se observa en el diagrama de la figura :ref:`uc2-num`, el usuario puede elegir compuestos previamente definidos para la conformación del sistema binario o bien crear nuevos compuestos. 

.. _uc2-num:

.. figure:: images/uc-DefinirSistema.png
   :width: 80%

   Caso de uso: definición del sistema binario


Cálculo Global
---------------
    
El backend se modela como un actor lógico (subsistema)
que interactua con el software desarrollado realizando el cálculo de los 
distinto diagramas. Se observa en la figura :ref:`uc3-num`. 

.. _uc3-num:

.. figure:: images/uc-CalcularGlobal.png
   :width: 80%

   Caso de uso: graficación de diagramas

Cálculo de parámetros 
---------------------

Definidas las constantes de los compuestos (obtenidas de la definición del sistema)
se calculan los parámetros del modelo elegido a través del backend o bien 
se ajustan las constantes de los compuestos en función de los parámetros definidos
manualmente por el usuario. Se representa en el diagrama de la figura :ref:`uc4-num`.


.. _uc4-num:

.. figure:: images/uc-CalcularParametros.png
   :width: 80%

   Caso de uso: Cálculo de parámetros






.. [#]  Este problema es conocido como *DLL Hell* (infierno de las DLL). Ver 
        http://es.wikipedia.org/wiki/DLL_Hell

.. [#]  Microsoft Jet Database Engine es un motor de base de datos utilizado por 
        el gestor Microsoft Access, entre otros productos. Ver 
        http://en.wikipedia.org/wiki/Microsoft_Jet

.. [#]  Para la parametrización de los datos de entrada para cada ecuación de 
        estado fue menenester documentar la :ref:`api`.

.. [#]  La validación de los rangos dinámicos (que dependen de las constantes críticas
        de los compuestos del sistema) la realizan los algoritmos de cálculo. El frontend
        se limita a reportar un error en la obtención de los datos de salida. 

.. [#]  La validez de esta función fue comprobada de manera empírica por 
        Cismondi.

.. [#]  Ver http://es.wikipedia.org/wiki/Historias_de_usuario

