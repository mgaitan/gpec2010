.. _test:

Verificación
************

Este capítulo describe el trabajo realizado para la verificación del correcto
funcionamiento de la aplicación. 

En particular se ha *"testeado"* la librería de comunicación, es decir 
la clase :py:class:`ApiManager` del módulo :py:mod:`apimanager`

   
Conceptos de pruebas unitarias
==============================

*Unit Testing* o pruebas unitarias son test en donde cada parte (módulo, clase, función) 
del programa es testeado por separado (de alló lo de *unitario*). 
Idealmente, se pone a prueba todas las funciones y todos los casos posibles para cada 
una de ellas.

Según [ZULBERTI2010]_, el unit testing tiene varias ventajas:

    * Permite probar que el programa funciona correctamente. En Python, los tests 
      también permiten identificar variables que no existen o tipos esperados en 
      las funciones (en otros lenguajes eso se hace en tiempo de compilación).

    * Permite identificar en caso de que se haga una modificación que siga 
      funcionando correctamente todas las parte del programa. Tanto las cosas 
      modificadas como las cosas que dependen de las modificadas. Esto es muy 
      importante cuando se trabaja en grupo (con algún sistema de control de versiones) 
      ya que permite asegurar que el código que usa el resto del grupo y que uno 
      modifico sigue funcionando.

    * Permiten documentar el código. Esto no es en forma directa, pero como los 
      tests indican como es que se tiene que comportar el programa, viendo los 
      tests uno puede fijarse cuál es el resultado esperado para ciertas entradas 
      del programa. Esto no excluye que se tenga que escribir la documentación del código.

Es muy importante que un test cumpla las siguientes reglas:

*  Tiene que poder correr sin interacción humana. Es decir, los tests no deben pedir que el usuario ingrese valores en ningún caso. Para esto, es en el test mismo cuando se pasan los valores a la función.
    
* Tienen que poder verificar el resultado de la ejecución sin interacción humana. De nuevo, para  saber si esta bien o no el resultado no tiene que pedirle al usuario que verifique el resultado. Para esto, se tiene que saber de antemano el resultado del test con los valores que se pasaron.
    
* Un test tiene que ser independiente del otro. Es decir, el resultado de un test no debería depender del resultado anterior.


Unit testing en Python 
-----------------------

Python provee en su librería estándar un completo framework para realizar 
pruebas unitarias. Se trata de :py:mod:`unittest` [#]_ cuya arquitectura y 
:term:`api` está basada en el framework `Junit <http://www.junit.org/>`_ para 
el lenguaje Java.

    .. note::
        
       El *testing* en todas sus formas tiene amplio interés en la comunidad de 
       usuarios de Python y además del framework estándar existen gran cantidad 
       de herramientas para facilitar distintos aspectos de la. 
       Ver `The Python Testing Tools Taxonomy <http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy>`_
    
En particular, se utilizó el framework :py:mod:`unittest2` que forma parte estándar
de la versión 2.7 de Python, y existe como :term:`backport` para las
versiones 2.4 a 2.6 [#]_. 

:py:mod:`unittest` provee muchas clases y funciones utilitarias para realizar 
pruebas automatizadas de la cuales se utilizó la estructura más tradicional 
basada en la clase :py:class:`TestCase`. 

Todos los métodos de una subclase de :py:class:`TestCase`
cuyo prefijo es ``test_`` son ejecutados como una prueba, cuya estructura 
general es realizar una acción y comparar el resultado producido con el resultado
esperado. Dependiendo de la condición analizada, que se realiza mediante alguno
o varios de los métodos que comienzan con ``assert`` (``assertEqual``, 
``assertNotEqual``, ``assertGreatEqual``, etc,) todos heredados 
de la clase :py:class:`TestCase`, la prueba es exitosa o falla. 

Existen además dos métodos especiales :py:meth:`setUp()`` y :py:meth:`tearDown()`
que se ejecutan automáticamente (antes y despues, respectivamente) de ejecutar 
cada test. 


Pruebas realizadas
==================

Como se dijo, varias pruebas fueron realizadas sobre el controlador de la 
interfaz de comunicación. Por supuesto, en un sistema tan complejo como 
el desarrollado la cobertura de pruebas dista de ser total, pero se ha verificado
el módulo más complejo y por ende propenso a introducir errores. 

Se listan a continuación la batería de test realizados. 

.. autoclass:: test_apimanager.TestApiManager
   :members: 

Ejemplos de código de las pruebas
---------------------------------

El código de implementación de cada una de estas pruebas es muy descriptivo
pero por una cuestión de extensión, se muestran sólo algunos de ellos. 
Para el estudio completo ver el módulo :py:mod:`test_apimanager.py`

Ejemplo 1
^^^^^^^^^

.. literalinclude:: ../src/test_apimanager.py
   :pyobject: TestApiManager.test_write_conparin_1

Ejemplo 2
^^^^^^^^^

.. literalinclude:: ../src/test_apimanager.py
   :pyobject: TestApiManager.test_read_conpaout_1

Ejemplo 3
^^^^^^^^^

.. literalinclude:: ../src/test_apimanager.py
   :pyobject: TestApiManager.test_gpecout_1


Ejecución y validación
----------------------

Se muestra la ejecución automatizada de todas las pruebas y su resultado 
exitoso:

.. code-block:: bash

    tin@azulita:~/facu/pi/src$ python test_apimanager.py
    test_gpecout_1 (__main__.TestApiManager) ... ok
    test_read_conpaout_1 (__main__.TestApiManager) ... ok
    test_write_conparin_1 (__main__.TestApiManager) ... ok
    test_write_conparin_2 (__main__.TestApiManager) ... ok
    test_write_conparin_3 (__main__.TestApiManager) ... ok
    test_write_gpecin (__main__.TestApiManager) ... ok

    ----------------------------------------------------------------------
    Ran 6 tests in 0.808s

    OK


Pruebas de usabilidad
=====================

Para analizar la mejora  respecto a la versión precedente se realizaron pruebas con 
usuarios inexpertos con el objetivo de observar el éxito en la tarea encomendada. 

Las condiciones experimentales de estas pruebas fueron:

- Cuatro usuarios trabajando individualmente
- Se solicita la obtención de una suite de gráficos
- No se da ninguna otra intrucción y ayuda oral o escrita sobre cómo lograr el 
  resultado   

Si bien la muestra poblacional no fue representativa para una conclusión 
definitiva, los cuatro usuarios lograron el objetivo en menos de 2 minutos, 
aún sin comprender el significado de los diagramas obtenidos. Las tareas
de manipulación de los diagramas como rotar (en 3D), hacer zoom, desplazar, etc. 
fueron bien interpretadas mediate los íconos de la barra de herramientas. 

Como experiencia adicional, puede contarse con las clases prácticas realizadas 
en el marco de los laboratorio de *Termodinámica* (Ingeniería Química, UNC), 
dictador por el Dr. Cismondi, donde la gran mayoría de los alumnos lograron 
realizar los diagramas antes de que se dieran las instrucciones de procedimiento.

Análisis cuantitativo 
----------------------

Se describen algunos aspectos cuantitativos que dan muestra de la reducción 
de componentes de control y acciones necesarias para realizar una tarea, comparando 
la versión actual con la anterior.

- Panel de definición de un caso

    ==============================  ==================================
    Visual GPEC                     GPEC 2010
    ==============================  ==================================
    38 componentes simultáneos      19 componentes 
    3 grupos de opciones            2 menues de opciones
    Opciones secundarias visibles   Opciones secundarias desplegables
    100 % espacio pantalla          25% espacio de pantalla
    ==============================  ==================================

- Definición un sistema de componentes arbitrarios

    ===================  ==================
    Visual GPEC          GPEC 2010
    ===================  ==================
    3 ventanas modales   1 ventana modales  
    7 clicks             4 clicks       
    15 cajas de texto    5 cajas de texto
    ===================  ==================



.. [ZULBERTI2010]  Zulberti, Tomás (2010), *Introducción a Unit Testing con Python*, Revista
                   "PET: Python Entre Todos"* Nº 1 - Agosto 2010, Comunidad de Usuarios
                   Python Argentina. Disponible en http://revista.python.org.ar/1/html/unittest.html



.. [#]  La documentación completa de la versión utilizada se encuentra en 
        http://docs.python.org/library/unittest.html

.. [#]  El paquete *backported* se encuentra en la dirección 
        http://pypi.python.org/pypi/unittest2  y se puede instalar fácilmente 
        mediante el utilitario :program:`easy_install`.
