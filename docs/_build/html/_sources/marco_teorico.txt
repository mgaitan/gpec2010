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
útiles para la comprensión de este trabajo. Para definiciónes de términos puntuales, 
consulte el :ref:`glosario <glosario>`.


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
:term:`interpretado`, :term:`multiparadigma` y :term:`multiplataforma`. 

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

     
Un sencillo programa *"Hola Mundo"* [#]_ en Python se ve así::

    print "¡Hola Mundo!"

Además, la mayoría de sus implementaciones [#]_, permiten ejecutar código en  
modo interactivo al estilo Matlab® u *Octave*, 
de manera que las expresiones pueden ser introducidas una a una y ver el resultado 
de su evaluación inmediatamente::

    >>> 1+1
    2
    >>> a = range(10)
    >>> print a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Esto resulta útil tanto para los principiantes que se están familiarizando con el lenguaje 
como para los programadores avanzados: se pueden probar porciones de código en el modo interactivo antes 
de integrarlo como parte de un programa.

Por diseño [#]_, Python tiene sintaxis muy clara que facilita la legibilidad del código. 
Esta característica es la razón por la que Guido van Rossum, su creador, 
lo compara con ":term:`pseudocódigo` ejecutable" [#]_. El siguiente programa 
aplica conceptos de programación orientada  a objetos como :term:`herencia` y :term:`polimorfismo`::

    class Animal:
        """Superclase que define un constructor común y 
            un método abstracto"""
        def __init__(self, nombre):   
            self.nombre = nombre
        def hablar(self):             
            raise NotImplementedError(u"La subclase debe \
                                        implementar el método")
     
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
 
    .. note::

        Dar una introducción completa a las capacidades de Python como lenguaje
        de programación quedan fuera de los alcances de este trabajo. Para 
        ampliar los conceptos aquí vertidos puede ver [TUT-PSF]_ y [MP2001]_.
        

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
para desarrollar interfaces gráficas de usuario (:term:`GUI`) (ver :ref:`wxpython`), y 
a la vez es extensible en C o C++. 

Esta facilidad de integración permite que frecuentemente sea utilizado 
como *"lenguaje pegamento"* (ver [GvR1998]_ ) para interconectar código que 
por razones de diseño, de performance o históricas están desarrolladas
en otro lenguaje de más bajo nivel, permitiendo aprovechar las ventajas de Python.

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
   
        Muchos otros casos de éxito son detallados en el texto mencionado, en 
        los dos volúmenes de *Python Success Stories* de la editorial O'Reilly's [#]_ y en 
        http://python.org/about/success/
           
NumPy
------

Los tipos de datos incorporados con Python nativamente para contener otros tipos 
de datos u objetos (en particular listas y tuplas), son muy eficientes pero
están diseñados para ser multipropósito. Estos "contenedores" pueden albergar cualquier
tipo de objeto (incluso una mezcla de ellos) y las listas, en particular, pueden mutar
(agregar, modificar o borrar elementos) dinámicamente. 

Es decir, que si bien pueden usarse listas o tuplas como un :term:`vector` de datos, no están 
especialmente concebidas para tal fin. 

    .. note:: 

        Los siguientes párrafos descriptivos han sido tomados, en modo
        de paráfrasis y traducido por el autor, del capitulo *What is NumPy?* de
        [NumPy-UG]_.

`NumPy <http://numpy.org>`_ es una biblioteca que extiende Python para complementar
este aspecto, proveyendo un tipo de objeto vector multidimensional (``narray``) y 
varios objetos derivados (como vectores enmascarados o matrices), 
además de rutinas optimizadas para la operación sobre estos vectores, incluyendo 
operaciones matemáticas y lógicas, manipulación de dimensiones, álgebra lineal, 
operaciones estadísticas básicas, simulación aleatoria, etc. 

Considere el código siguiente que dado dos secuencias unidimensionales ``a`` y ``b`` de igual
longitud y con todos sus elementos numéricos, multiplica elemento por elemento 
y dispone el resultado en una nueva lista ``c``::

    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])

El resultado será correcto, pero considerando que las secuencias ``a`` y ``b``
pueden tener millones de elementos, se pagará el precio de una iteración ineficiente. 

Esta operación, siendo ``a`` y ``b`` objetos *ndarray* de NumPy, resultaría en::

    c = a * b

Dicho código funcionaría siempre que ``a`` y ``b`` tengan las mismas dimensiones, 
independientemente que sean uni o multidimensionales. 

El ejemplo ilustra dos características de NumPy que son gran parte de las bases 
de su poder: *vectorización* y *broadcasting* 

La *vectorización* describe la ausencia de iteraciones explícitas e indización
(que toman lugar, por supuesto, "detrás de escena", en un optimizado y precompilado
código C). La vectorización tiene muchas ventajas:

    * El código vectorizado es más conciso y fácil de leer. 
    * Menos líneas de código habitualmente implican menos errores. 
    * El código se parece más a la notación matemática estándar (por lo que es más fácil, 
      por lo general, corregir código asociado a construcciones matemáticas
    * La vectorización redunda en un código más "pythónico" [#]_

El *broadcasting* o *difusión* es el término que describe el comportamiento 
elemento "elemento por elemento" de las operaciones. En general, en NumPy todas 
las operaciones adoptan por defecto un comportamiento de este tipo (no sólo las operaciones 
aritméticas sino las lógicas, las funcionales y las de nivel de bits). 

Matplotlib               
----------

`Matplotlib <http://matplotlib.sourceforge.net/>`_ es una biblioteca para Python, 
liberada como software libre, que permite la generación de diferentes tipos de gráficos en 2D y 3D con calidad 
de publicación. Se pueden generar gráficos cartesianos, polares, de barras, 
histogramas, de superficie, etc. 

    .. figure:: images/matplotlib_examples.png
    
        Ejemplos de gráficos logrados con Matplotlib

Aunque tiene su origen en la emulación de los comandos gráficos de Matlab® , 
es totalamente independiente y puede usarse de una manera pythónica y orientada
a objetos. Está principalmente escrito en Python, aunque se basa fuertemente
en NumPy y otras extensiones para proveer buena performance incluso con 
arreglos grandes. 

Sin bien existen otras bibliotecas libres con prestaciones similares [#]_, Matplotlib 
se destaca por las siguientes características: 

    * Cuenta con una extensa y clara documentación (ver [MPLDOC]_)
    * Es orientado a objetos: se puede heredar, extender y sobrecargar cada tipo de objeto 
      que define
    * La calidad de los gráficos es excepcional, permitiendo la exportación
      a muchos formatos gráficos, incluyendo :abbr:`PS (PostScript)` y 
      :abbr:`SVG (Scalable Vector Graphic)`
    * Es empotrable dentro de las bibliotecas para :term:`GUI` más utilizadas
      permitiendo realizar aplicaciones de escritorio sin la funcionalidades. 
    * Incorpora muchos paquetes que extienden las posibilidades: el 
      muy logrado paquete para graficación 3D, graficación sobre mapas geográficos, 
      utilidades para la interacción con Microsoft Excel®, etc. 


.. _wxpython:

WxPython
--------

`wxWidgets <http://www.wxwindows.org/>`_ es una biblioteca en C++ que permite 
desarrollar interfaces gráficas para aplicaciones multiplataforma que corren
en Microsoft Windows, OS X, GNU/Linux o UNIX de 32 o 64 bits. 

`wxPython <http://www.wxpython.org/>`_ es un :term:`wrapper` de la biblioteca wxWidgets 
para el lenguaje de programación Python. Junto a Python permite el desarrollo 
rápido de aplicaciones gráficas de escritorio multiplataforma.

Una de las características sobresalientes de wxWidgets es su uso nativo de 
las API gráficas de cada entorno de ventanas, brindando una apariencia y experiencia
de uso nativa para cada ambiente. Esto significa la misma aplicación, sin modificaciones
(al menos significativas), adopta las características gráficas definidas por el 
usuario en el entorno de escritorio. En concreto: se ve como *una aplicación Windows* 
si se corre en Windows®, como una *aplicación GNOME* si se corre sobre el gestor 
de escritorio GNOME en Linux, y como una aplicación OS/X en platafomas Mac:

       .. figure:: images/wxpython_example.png
    
          El mismo programa wxPython ejecutado en Windows, Linux y Mac

   
La guia [NR-RD2006]_ escrita por dos de los desarrolladores de la biblioteca
es un material de refencia obligado para el desarrollo con wxPython. 
Allí se exponen como características relevantes es la orientación 
a objetos y la orientación a eventos.

    .. attention::
        
        En la bibliografía de wxPython se denomina *window* a cualquier elemento
        gráfico que ocupa espacio visual y puede ser contenido por otro. Lo que 
        comunmente se denomina *window* (ventana) en otros escenarios, en wxPython
        es un *frame*, es decir, una ventana de programa. 

Se expondrán estos conceptos con un ejemplo::

    import wx

    class MyFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None, -1, "Ventana", size=(300, 300))

            panel = wx.Panel(self, -1)
            wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
            self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))
        
            panel.Bind(wx.EVT_MOTION, self.OnMove)

        def OnMove(self, event):
            pos = event.GetPosition()
            self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

    if __name__ == '__main__':
        app = wx.PySimpleApp()
        frame = MyFrame()
        frame.Show(True)
        app.MainLoop()


La subclase ``MyFrame`` hereda de la clase ``wx.Frame`` y extiende su 
constructor incluyendo un objeto ``Panel`` (elemento contenedor de otros 
objetos gráficos), una línea de texto estática y una caja de texto 
denominada ``self.posCtrl``. 

Además se realiza un *binding*, es decir, 
la asociación de un evento identificable a una acción, un método o función 
que indica como responde el programa ante el acaecimiento del evento. 
En este caso se asocia el evento ``wx.EVT_MOTION`` en el objeto ``panel`` 
(que ocurre cuando se mueve el puntero sobre el objeto) al método ``OnMove``. 

Como resultado, cada vez que se mueve el puntero sobre el panel, la caja
de texto será actualizada con las coordenadas donde este se encuentra.

    .. figure:: images/wxpython_ventana.png

        Captura del ejemplo de marras




            
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

.. [#]  El código que sigue los principios de legibilidad y transparencia propuestos 
        por Python se dice que es "pythonico". Contrariamente, el código opaco u ofuscado es 
        bautizado como "no pythonico". Ver [PEP8]_ y [PEP20]_.

.. [#]  `Chaco <http://code.enthought.com/chaco/>`_ y `GNUplot-Py <http://gnuplot-py.sourceforge.net/>`_ 
        son las más notables alternativas. 

.. [GvR1998]  van Rossum, Guido (1998), *Glue it all together with Python*, 
              Workshop on Compositional Software Architecture in Monterey, 
              http://www.python.org/doc/essays/omg-darpa-mcc-position.html

.. [AM-IG2003]  Marzal, Andrés - Gracia, Isabel (2003), *Introducción a la programación con Python*, 
                Departamento de Lenguajes y Sistemas Informáticos, Universitat Jaume I,
                Castelló de la Plana
                                           
.. [TZ2008]  Ziadé, Tarek (2008),  *Expert Python programming*, Pack Publishing, Birmingham

.. [JH-FP]  Hunter, John D. - Pérez, Fernando, (n/d) *Practical Scientific Computing in Python*,

.. [TUT-PSF] van Rossum, Guido (2010), *The Python Tutorial v2.7*, Python Software Foundation, 
             http://docs.python.org/tutorial/ . Existe una traducción al español en  realizada
             por la comunidad Python Argentina en http://python.org.ar/pyar/Tutorial

.. [MP2001]  Pilgrim, Mark (2001), *Dive into Python*, liberado bajo los términos 
             de GNU Free Documentation License, http://diveintopython.org/. Existe 
             una traducción al español disponible en http://www.gulic.org/almacen/diveintopython-5.4-es/
            
.. [WIKIPEDIA1]  Contribuidores varios, *Polymorphism in object-oriented programming*, 
                 Wikipedia, The Free Encyclopedia, visto el 16 de agosto de 2010, 
                 http://en.wikipedia.org/wiki/Polymorphism_in_object-oriented_programming

.. [HPL2004]  Langtangen, Hans P (2004), *Python Scripting for Computational Science*, 
              Simula Research Laboratory and Department of Informatics University of Oslo, Oslo

.. [PEP8]  van Rossum, Guido - Warsaw, Barry (2001), *Python Enhancement Proposals (PEP) #8: 
           Style Guide for Python Code*, Python Software Foundation, http://www.python.org/dev/peps/pep-0008/

.. [PEP20]  Peters, Tim (2004) *Python Enhancement Proposals (PEP) #20: The Zen of Python*,
            Python Software Foundation, http://www.python.org/dev/peps/pep-0020/

.. [NumPy-UG] Scipy community, *NumPy User Guide*,  http://docs.scipy.org/doc/numpy

.. [TO2006]  Oliphant, Travis (2006) *Guide to NumPy*, Trelgol Publishing, http://www.trelgol.com

.. [MPLDOC]  Hunter, J - Dale, D - Droettboom, M (2010), *Matplotlib documentation v1.0.0*, 
             http://matplotlib.sourceforge.net/contents.html

.. [NR-RD2006] Rappin, Noel - Dunn, Robin (2006) *wxPython in Action*, Manning Publications, 
               Greenwich
