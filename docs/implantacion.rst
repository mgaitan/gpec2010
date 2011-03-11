.. _implantacion:

Implantación
************

Empaquetado para sistemas Windows
---------------------------------

Como requisito, se especificó que GPEC debía ser capaz de ejecutarse en 
plataformas Windows® y Linux. Para satisfacer esta condición la tecnología 
utilizada se eligió intrínsecamente multiplataforma, aunque el 
:term:`ambiente de desarrollo` principal haya estado basado en Linux. 

Por supuesto, para realizar pruebas de compatibilidad y asegurar el 
funcionamiento en windows, se debió instalar un ambiente análogo con
versiones para este sistema operativo. 


Sin embargo, la distribución del software para usuarios Windows no puede 
basarse en la reproducción de un ambiente de desarrollo, es decir, la 
instalación por separado del lenguaje Python (intérprete) y las diversas 
bibliotecas necesarias para la ejecución del software. Esto, en primer lugar, 
porque complica la utilización al usuario inexperto, y en segundo lugar 
porque resulta ineficiente en términos de tamaño teniendo en cuenta que sólo parte 
(algunos módulos)  de las bibliotecas intrísecas de Python y las bibliotecas 
de terceros son utilizadas en GPEC. 

Por poner un ejemplo, la biblioteca de graficación *Matplotlib* incluye 
soporte para la integración con otras bibliotecas para interfaces gráficas 
(como Qt, GTK, etc ) que no son utilizadas en GPEC al estar basada, como se ha 
especificado, en *WxWidget*. 



Py2exe: separar sólo lo necesario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para realizar el estudio de cuáles son los módulos (y sus respectivas 
dependencias) unívocamente necesarios  se utilizó el software `py2exe 
<http://www.py2exe.org/>`_

*py2exe* es una extensión a las Python Distribution Utilities 
(“Distutils”) que convierte scripts de Python en aplicaciones ejecutables 
en windows (.exe) sin requerir la instalación por separado del intérprete o 
bibliotecas. 

Partiendo de un ambiente de desarrollo Windows con todos los requerimientos 
satisfechos, *py2exe* realiza un **árbol de dependencias** y genera una 
carpeta incluyendo únicamente los módulos estrictamente necesarios, así 
como una copia de las librerías dinámicas (.dll) necesarias para la 
ejecución. Además, puede realizar la conversión del código python a 
*bytecode* (formato binario más rápidamente interpretable por Python) y 
agregar una cierta compresión, de manera de optimizar el tamaño del paquete 
resultante. 

.. figure:: images/py2exe_2.png
   :width: 671px
   
   Salida final de la ejecución de *py2exe* enumerando las librerías dinámicas
   complementarias que son necesarias para la ejecución del programa. Todas 
   estas son comunes en cualquier instalación por defecto de Windows. 
   
La configuración de *py2exe* se realiza a través de un 
módulo estándar de las *Distutils* denominado ``setup.py``. 
Allí se especifican variables y directrices necesarias, como el nivel de 
compresión, cuál es el módulo principal (que será convertido en el 
".exe"), datos extra que deben ser incluídos (por ejemplo, la base de datos), 
etc. 

El ``setup.py`` de GPEC es el siguiente:: 


    from distutils.core import setup
    import py2exe
    import matplotlib
     
    data = matplotlib.get_py2exe_datafiles() 

    data += ['LICENSE.txt']

    includes = ['numpy.core.umath']
    excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
                'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                'Tkconstants', 'Tkinter']
    packages = []
    dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                    'tk84.dll']

    setup(
        data_files = data, 
        options = {"py2exe": {"compressed": 2,
                              "optimize": 0, #2,
                              "includes": includes,
                              "excludes": excludes,
                              "packages": packages,
                              "dll_excludes": dll_excludes,
                              "bundle_files": 3,
                              "dist_dir": "dist",
                              "xref": False,
                              "skip_archive": False,
                              "ascii": False,
                              "custom_boot_script": '',
                             }
                  },
        windows=['aui.py']
    )

El resultado de *py2exe* es una carpeta ``./dist`` que incluye todo el código 
fuente de la aplicación en formato *bytecode* con todas las 
bibliotecas necesarias así como el intérprete de Python empaquetado como 
biblioteca dinámica. 

.. figure:: images/py2exe_3.png
   :width: 719px

   Resultado de la ejecución de *py2exe*

Ejecutando ``aui.exe`` se ejecutaría la aplicación distribuible. 

Generación de un instalador
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si bien la distribución de la carpeta ``./dist``, posiblemente en formato 
comprimido (``.zip``, ``.rar``, etc.), es suficiente para correr la 
aplicación y esta se encuentra optimizada, el usuario Windows 
está acostumbrado a la utilización de *instaladores* que disponen los 
archivos en un directorio para tal menester (``"windows/programs files"`` en 
general), realizan tareas como la "registración de la aplicación" y generan 
entradas de acceso rápido en el "Menú de Inicio", por ejemplo. 

Para realizar un instalador a partir del directorio generado por *py2exe* se 
utilizó la aplicación `NSIS (Nullsoft Scriptable Install System) 
<http://nsis.sourceforge.net/>`_, que es una software open source para la 
creación de instaladores Windows. 

.. figure:: images/py2exe_3.png
   :width: 615px

   Creando un instalador Windows a partir de un *zip* con el contenido 
   resultante de *py2exe*
 
Compatibilidad
^^^^^^^^^^^^^^^

La instalación de GPEC se ha probado satisfactoriamente en sistemas Windows 
XP, Windows Vista y Windows 7. 


Instalación en sistemas Linux
-----------------------------

Para entornos Linux, el empaquetado y la distribución se realiza mediante las 
nombradas *Python Distribution Utilities (“Distutils”)* . En términos 
generales, es un análogo al utilitario ``make`` muy común en flujos de 
desarrollo basadas en lenguaje C o C++, que permite la declaración de 
dependencias y la instalación de un paquete Python, ya sea esta una 
aplicación en sí, una extensión o un módulo de funciones auxiliares. 

La diferencia fundamental con el empaquetado para Windows es que no se 
distribuye el conjunto de dependencias, sino que estas son simplemente 
declaradas. El usuario (o el instalador automatizado, como *easy_install*) 
son los encargados de asegurar el cumplimiento de esta dependencia, ya sea 
verificando que está previamente instalada en el sistema o instalandola. 

Aunque esto genera cierto *overhead* en primera instancia, porque una 
dependencia (por ejemplo, *Matplotlib*) es instalada completamente, esta 
política permite una optimización cuando existen dependencias comunes en 
diversas aplicaciones. En nuestro ejemplo, si dos aplicaciones requieren 
*Matplotlib*, utilizan una única versión instalada en el sistema. Esta coincidencia de 
dependencias es altamente frencuente en sistemas Linux, heredada de la 
filosofía Unix que se resume en su famoso leitmotif:

    "Write programs that do one thing... and do it well" [#]_


Sin embargo, por falta de masa crítica y tiempo, al momento de la 
presentación no se realizaron instaladores ni paquetes especificos para una 
distribución Linux, aunque la instalación mediante el código fuente es 
trivial, dado que Python no reqiere compilacion. Los siguientes comandos son 
suficientes para la obstención de la última versión de GPEC y sus 
dependencias::


    $ sudo apt-get install python-matplotlib python-matplotlib-data python-numpy 
      python-wxgtk2.8 wine subversion
    $ svn checkout https://gpec2010.googlecode.com/svn/trunk/src gpec

Y para ejecutarlo, simplemente se invoca el script principal::


    $ python gpec/aui.py



  


Distribución y soporte
-----------------------

Dada la gratuidad de GPEC, cada nueva versión se deja disponible 
automáticmente en la sección de descargas del sitio de desarrollo, 
http://code.google.com/p/gpec2010/downloads/list
y también en su sitio oficial http://gpec.efn.uncor.edu

También se ha creado un grupo de correo , que intenta nuclear a la 
comunidad de usuarios e interesados en GPEC. Allí se remiten novedades del 
desarrollo, se contestan dudas y se recibe *feedback* de los usuarios. La 
dirección del grupo es http://groups.google.com.ar/group/gpec-discuss 







.. [#] "Escribe programas que hagan una cosa... y hazlo bien" 
       Ver http://en.wikipedia.org/wiki/Unix_philosophy
