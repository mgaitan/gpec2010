Marco Teórico
**************

Debido a la naturaleza multidisplinaria de este trabajo, posiblemente sea leído
y evaluado por profesionales o interesados de/en las distintas áreas de incumbecia 
(química y computación). 

    .. seealso::

        :ref:`trabajo_interdisciplinario`.

Dado que no necesariamente se tiene un conocimiento
sólido fuera de la especifidad de la profesión, en este capitulo se presentarán 
conceptos generales (que no pretenten exhautividad pero sí precisión) de las dos áreas, 
útiles para la comprensión de este trabajo. Para definiciónes de términos puntuales, consulte el :ref:`glosario <glosario>`.


Conceptos de diagramas de fases en termodinámica
=================================================


Conceptos de orientación a objetos
==================================



Orientación a eventos
---------------------

Metodologías
============

Desarrollo por etapas
---------------------

Refactoring
-----------

Principios de diseño
====================


DRY
---
:abbr:`DRY (Don't Reapeat Yourself)` , "No te repitas" es un principi


Pareto
------

Loose Coupling
--------------

.. _tecnologias:

Tecnologías principales
========================

Python 
------

`Python <http://python.org>`_ es un avanzado lenguaje de programación de alto nivel, 
:term:`interpretado`, :term:`multiparadigma` y :term:`multiplataforma`. Además, 
la mayoría de sus implementaciones [#]_, permiten ejecutar código de manera :term:`interactiva <interactivo>`.

    .. glossary::

        interpretado
            Un lenguaje interpretado es un lenguaje de programación que está diseñado 
            para ser ejecutado por medio de un intérprete (o máquina virtual), 
            en contraste con los lenguajes compilados. En general, el proceso consiste en 
            traducción del código fuente a un *bytecode* que el interprete traduce a 
            su vez, en tiempo de ejecución y cuando lo necesita, a código máquina. 

        multiparadigma
            Python soporta múltiples paradigmas de programación. En vez de exigirle 
            al usuario (o forzar el problema para) que se ajuste a un estilo de 
            programación, el lenguaje permite diversos estilos o una mezcla de ellos. 
            Puede usarse con un paradigma estructurado e imperativo (como C o Pascal), 
            como orientado a objetos (como Java o C++). Además soporta características
            de programación funcional, orientada a aspectos (AOP), y de metaprogramación.
        
        multiplataforma
            Existen intérpretes de Python para distintas arquitecturas (x86, i64, powerpc, etc.)
            y sistemas operativos (Windows, Linux, OS/x, etc.) manteniendo el mismo 
            código y funcionalidades de alto nivel. Esto permite una altísima portabilidad
            del software, de manera que un mismo programa puede ser ejecutado en 
            diferentes plataformas. 

        interactivo
            Python incluye un modo interactivo, al estilo Matlab de manera que las 
            expresiones pueden ser introducidas una a una, pudiendo verse el resultado 
            de su evaluación inmediatamente. Esto resulta útil tanto para los principiantes
            que se están familiarizando con el lenguaje como para los programadores avanzados: 
            se pueden probar porciones de código en el modo interactivo antes 
            de integrarlo como parte de un programa.


Un sencillo programa *"Hola Mundo"* [#]_ en Python se ve así::

    print "¡Hola Mundo!"

Por diseño [#]_, Python tiene sintaxis muy clara que facilita la legibilidad del código. 
Esta característica es la razón por la que Guido van Rossum, su creador, 
lo compara con ":term:`pseudocódigo` ejecutable" [#]_. 

Intente comprender el siguiente programa, que aplica conceptos de programación orientada 
a objetos como herencia y polimorfismo::

    class Animal:
        """Superclase que define un constructor común y un método abstracto"""
        def __init__(self, nombre):   
            self.nombre = nombre
        def hablar(self):             
            raise NotImplementedError(u"La subclase no implementa el método")
     
    class Gato(Animal):     
        def hablar(self):   
            return 'Miau!'
     
    class Perro(Animal):
        def hablar(self):
            return 'Guau, guau!'
     
    #instanciación de 3 objetos dentro de una lista
    animales = [Gato('Michi'),          
                Gato('Felix'),
                Perro('Firulai')]
     
    for animal in animales:
        print animal.nombre + ': ' + animal.hablar()

    #Imprime lo siguiente:
    #
    #Michi: Miau!
    #Felix: Miau!
    #Firulai: Guau, guau!

Puede ver el artículo [WIKIPEDIA1]_ para una comparación (en particular la extensión y legibilidad)
de código equivalente en otros lenguajes de programación.

 
En Python el **tipado de datos es dinámico** (al igual que la asignación de memoria), 
es decir que el tipo de dato (entero, cadena, punto flotante u otros tipos de más alto nivel como listas o diccionarios) 
se determina automáticamente al momento de la asignación de la variable, a diferencia 
de los lenguajes de tipado estático  (como Java o C) que exigen la declaración de todas las varibles con sus tipos antes de 
ser utilizadas. Sin embargo, el **tipado es fuerte**,  ya que una vez que la variable 
adquiere un tipo (o sea, ha sido asignada), queda determinado su tratamiento. Por ejemplo la operación 
``+`` entre cadenas de texto retorna la concatenación de las cadenas, mientras 
que entre tipos numéricos retorna la suma. Intentar operar con ``+`` entre un 
número y una cadena dará un error sino se convierte una de las dos variables 
al otro tipo de manera explícita. 

El lenguaje incluye una **robusta biblioteca estándar** (se dice habitualmente que *"Python 
tiene con las baterías incluídas"*) con acceso a funcionalidades de todo tipo 
como protocolos de internet, funciones matemáticas, manejo de hilos y multiprocesos, 
pruebas unitarias y abstracción de llamadas al sistemas operativo subyacente, entre 
muchas otras.

Además de la incorporada, puede interfacear con diversas bibliotecas, por ejemplo
para para desarrollar interfaces gráficas de usuario (:term:`GUI`), y 
a la vez es extensible en C o C++. 

Esto facilidad de integración permite que frecuentemente sea utilizado 
como *"lenguaje pegamento"* (ver [GvR1998]_ ) para interconectar código que 
por razones históricas, de performance o arquitectura están desarrolladas
en otro lenguaje de más bajo nivel.

Python ha ganado popularidad no sólo entre programadores aficionados
sino en el mercado altamente competitivo de la industria del software. Como 
plantea Shannon Behrens en el prólogo de [TZ2008]_:
    
    Hubo un tiempo en el que las compañías me llamaban loco cuando insistía en usar Python. 
    En estos días, simplemente no hay suficientes programadores Python para todos. 
    Grandes empresas como Google, YouTube, VMware y DreamWorks están en una lucha 
    constante para contratar todo buen talento Python que puedan encontrar. [#]_


Python en el software científico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Como se afirma en [JH-FP]_ en la sección *Who is using Python?*, el uso de 
Python en la computación científica  es tan amplio como el campo mismo. 
Los autores destacan muchos usos en distintas universidades y centros de investigación 
del mundo:

* El *Jet Propulsion Laboratory* (JPL) de la :abbr:`NASA (National Aeronautics and Space Administration, EE.UU.)`
  usa Python como interfaz a bibliotecas Fortran y C++ que conforman una suite de 
  herramientas de visualización de trayectorias.

* El Space Telescope Science Institute (STScI) lo usa en muchos aspectos de su pipeline, 
  planificando la adquisición de datos del telescopio Hubble, administrando volúmenes
  de información y analizando imágenes atronómicas. 
  
* La *National Oceanic Atmospheric Administration* (NOAA) usa Python para 
  el análisis sintáctico de archivos, el prototipo de algoritmos computacionales, 
  la codificación de interfaces de usuario de escritorio y web y el desarrollo de 
  modelos. 
  
* La Enthought Corporation lo usa para adaptar a las necesidades de sus clientes aplicaciones
  para la exploración de petroleo. 


    .. seealso::
   
        Muchos otros casos de éxito son detallados en los dos volúmenes 
        *Python Success Stories* de la editorial O'Reilly's [#]_ y en 
        http://python.org/about/success/
   
        
Numpy
------

Matplotlib               
----------

WxPython
--------
            
Gestión de proyecto
===================

Control de versiones
--------------------

Documentación
-------------

Wiki
^^^^

restructuredText
^^^^^^^^^^^^^^^^

Sphinx
^^^^^^

.. [#]  Python es un lenguaje estandarizado que tiene distintas implementaciones. 
        La original y más utilizada es Cpython, implementada en C, pero existen
        implementaciones en Java (http://jython.org), .NET (http://www.ironpython.net/)
        y Python mismo (http://codespeak.net/pypy)

.. [#]  Un programa {"Hola Mundo!"} es el que imprime el texto «Hola Mundo!» en un 
        dispositivo de visualización (generalmente una pantalla de monitor). 
        Se suele usar como introducción al estudio de un lenguaje de programación, 
        siendo un primer ejercicio típico.

.. [#]  La hipótesis en la que se basó su creador es que el código fuente suele leerse 
        muchas más veces de las que se escribe, ya sea por el mismo autor tiempo 
        despues de haberlo escrito, o por otros programadores. 

.. [#]  *"Syntactically, Python code looks like executable pseudo code."*, [GvR1998]_

.. [#]  Traducción del inglés propia.

.. [#]  *Python Success Stories: 8 True Tales of Flexibility, Speed, and Improved Productivity* (2002) y 
        *Python Success Stories Volume II: 12 More True Tales* (2005), O'Reilly Associates

.. [GvR1998]  Rossum, Guido v (1998), *Glue it all together with Python*, 
              Workshop on Compositional Software Architecture in Monterey, 
              http://www.python.org/doc/essays/omg-darpa-mcc-position.html

.. [AM-IG2003]  Marzal, Andrés - Gracia, Isabel (2003), *Introducción a la programación con Python*, 
                Departamento de Lenguajes y Sistemas Informáticos, Universitat Jaume I,
                Castelló de la Plana
                                           
.. [TZ2008]  Ziadé, Tarek (2010),  *Expert Python programming*, Pack Publishing, Birmingham

.. [JH-FP]  Hunter, John D. - Pérez, Fernando, (n/d) *Practical Scientific Computing in Python*,
            
.. [WIKIPEDIA1]  Contribuidores varios, *Polymorphism in object-oriented programming*, 
                 Wikipedia, The Free Encyclopedia, visto el 16 de agosto de 20010, 
                 http://en.wikipedia.org/wiki/Polymorphism_in_object-oriented_programming

.. [HPL2004]  Langtangen, Hans P (2004), *Python Scripting for Computational Science*, 
              Simula Research Laboratory and Department of Informatics University of Oslo, Oslo

