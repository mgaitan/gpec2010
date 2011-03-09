Implementación
***************

Patrones de diseño
===================
        
Publish/Subscribe
-----------------

Un patrón de diseño (también catalogado como patrón de mensajería) de recurrente 
aplicación en GPEC ha sido *Publish/Subscribe*, frencuentemente abreviado *Pubsub*. 
Se trata de una arquitectura de paso de mensajes desacoplada (y en algunas implementaciones distribuída)
donde existen "remitentes" (o "publicadores") que envían mensajes ante el acaecimiento
de un suceso específico (por ejemplo, un evento originado por el usuario como 
el click sobre un botón) sin conocimiento alguno sobre "qué sucede despues" 
con el mensaje. Análogamente existen "receptores" (o "suscriptores") que en cuya inicialización
se define a qué tipo de mensajes se suscribirán (el tipo se define en función 
del "asunto" o "topic") y qué acción (un método o función) 
debe ejecutarse cuando un mensaje de tal tipo arribe. 

.. figure:: images/pubsub_concept.png
   :width: 60%

   Diagrama conceptual de la arquitectura *Pub/Sub*


Como se describe en [vdLaar2002]_ Pubsub facilita el desacople de componentes 
(*callables*, módulos, paquetes) dentro de una aplicación. Los conceptos involucrados son:


- Permitir que partes de un aplicación evien mensajes "al resto de la aplicación" 
  sin tener que conocer:
  
  - *si* el mensaje será manejado y usufructuado: 
  
    - puede suceder que el mensaje se ignore completamente
    - o que sea manejado en muchas partes diferentes de la aplicación
    
  - *cómo* será manejado el mensaje: 

    - al publicador no le importa qué se hará con el mensaje y su contenido;
    - tampoco hay control del orden en que un mensaje dado se enviará al resto
      de la aplicación (comportamiento no determinístico).   

- Permitiendo que partes de una aplicación reciban y manejen mensajes desde 
  "el resto de la aplicación" sin tener que conocer *quién* envió el mensaje.    


Un *receptor* (*listerner*) es "una parte de la aplicación que quiere 
recibir mensajes". Un receptor se suscribe a uno o más tópicos. Un *emisor*
(*sender*) es cualquier parte de la aplicación que envía (deposita en 
el intermediario) un mensaje con un tópico dado, y opcionalmente, cualquier información
adjunta. Este intermediario (a veces conocido como *broker*, o directamente 
*pubsub*) entrega este mensaje a todos los receptores suscriptos. 

Ventajas
^^^^^^^^

- **Acoplamiento débil**: la topología de Pubsub, basada en la intermediación y el 
  desconocimiento de identidades y comportamientos de los objetos que interactuan 
  permite un desacople de los componentes de la aplicación. Esto significa
  que las distintas "partes" de la aplicación son independientes entre sí, de modo 
  que pueden facilmente desactivarse componentes no críticos sin afectar al conjunto 
  de la aplicación. Esta estrategia es útil para realizar pruebas de seguridad. 


- **Funcionalidad configurable** : Dado que un emisor no tiene necesidad de conocer
  la existencia de un receptor, es fácil diseñar una arquitectura basada en "plugins"
  que permite mantener un núcleo y agregar funcionalidades extra con posterioridad  
  (incluso desarrolladas por terceros). Esto trae aparejada la posibilidad de 
  adaptar, mediante extensiones que se activan o no, las características 
  del software en función de las necesidades del usuario. 

- **Escalabilidad**: En las implementaciones distribuidas de demanda moderada (donde los mensajes
  se transmiten entre múltiples procesos o, incluso, equipos), PubSub provee
  una arquitectura mucho más simple y autogestionada que la típica topología
  *cliente/servidor* para tareas de procesamiento paralelo o  
  Sin embargo, la eficiencia no suele ser proporcional en sistemas de alta
  demanda computacional.  

Python Pubsub
^^^^^^^^^^^^^

En GPEC se ha utilizado el paquete `Python Pubsub <http://pubsub.sourceforge.net/>`_
de Oliver Schoenborn, en su versión 1 [#]_ . Esta implementación es muy sencilla
y se basa en la existencia de un objeto único (Ver :term:`singleton`), ``pub``, 
que controla el envío y las suscripción a los mensajes. Se describe en el siguiente 
código::



    from pubsub import pub      

    # declaración de la  función "destino" 

    def destino(arg1, arg2=None):
        print 'Mensaje con argumentos arg1="%s"\n  arg2="%s"' % (arg1, arg2)

    # declaración de suscripción

    pub.subscribe(destino, 'asuntoParticular')

    # función que envía un mensaje 

    def hacer_algo_y_avisar():
        print 'Se enviará un mensaje'
        pub.sendMessage('asuntoParticular', arg1=123, arg2=dict(a='abc', b='def'))
    
    if __name__ == '__main__':

        hacer_algo_y_avisar()


Cuyo diagrama de secuencia es el siguiente:


.. figure::images/uml_sec_pubsub.png
   :width: 80%

   Diagrama de secuencia para una interacción sencilla entre emisor y receptor
   via *Pub/Sub*


Ejemplos de uso
^^^^^^^^^^^^^^^

Panel de mensajes
+++++++++++++++++

Como se ha dicho, PubSub constituye el patrón principal y toda la *orientación
a eventos* se basa en una comunicación vía esta biblioteca. 

El ejemplo canónico es el **panel de log** (registro de mensajes de usuario), donde
se registra una crónica de eventos de interés para el usuario, denotados en 
su categoría con un símbolo y la hora del suceso. 

.. figure:: images/log_msg.png
   :width: 80%

   A través de PubSub, cualquier parte del programa envía avisos que el panel
   (un *receptor*) mostrará al usuario. 

En la incialización del panel se realiza la subscripción a los mensajes con 
tópico ``'log'``, y asigna como acción el método ``OnAppendLog()``::


    class LogMessagesPanel(wx.Panel):
        def __init__(self, parent, id):
            wx.Panel.__init__(self, parent, id)

            self.list = wx.ListCtrl(self, -1,  style=  wx.LC_REPORT|wx.SUNKEN_BORDER)
            self.setupList()

            sizer = wx.BoxSizer()
            sizer.Add(self.list, 1, wx.EXPAND)
            self.SetSizerAndFit(sizer)
        
            pub.subscribe(self.OnAppendLog, 'log')


Ante la recepción de un mensaje se produce la invocación del método
adjuntando como parámetro un *objeto mensaje* (``msg``) en cuyo atributo ``data``
se almacena la información enviada por el remitente::


    def OnAppendLog(self, msg):
        ico = self.icon_map[msg.data[0]]

        message = msg.data[1]
        index = self.list.InsertImageStringItem(sys.maxint, message, ico)
        self.list.SetStringItem(index, 1, time.strftime('%H:%M:%S'))
        self.list.EnsureVisible(index) #keep scroll at bottom

        if msg.data[0] == 'error':
            wx.Bell()

La información en ``msg.data`` es, por convención de diseño, una tupla
de la forma ``(asunto, mensaje de usuario)``. Los asuntos posibles están asociados 
al icono que los representan: 

    =============  ============= =========================
     Asunto         Símbolo       Descripción  
    =============  ============= =========================
      *ok*          |ok|          Acción existosa               
      *info*        |info|        Información importante
      *warning*     |warning|     Advertencia  
      *error*       |error|       Error
    =============  ============= =========================


.. |ok| image:: images/ok.png
.. |info| image:: images/info.png
.. |warning| image:: images/warning.png
.. |error| image:: images/error.png

Como se observa en el código, en caso de un mensaje del tipo "error", además
de agregar el mensaje se ejecuta ``wx.Bell()`` que produce una alerta sonora. 

El *remitente* de mensajes de log se realiza desde múltiples puntos. Por ejemplo
ante la carga de la aplicación, cuando se define un sistema, cuando se realiza
un cálculo (mediante la invocación a un ejecutable del *backend*), etc. 
Por ejemplo, en el código de ejecución de la aplicación, en ``aui.py`` se 
observa::


    (...)
    main_frame.Show()
    pub.sendMessage('log', ('ok', 'GPEC is ready. Define a system to begin') )
    app.MainLoop()


Generación de gráficos
++++++++++++++++++++++

Otro uso de PubSub es la generación de gráficos. Se resume en el siguiente 
diagrama de secuencia:


.. figure:: images/uml_sec_makeplot.png
   :width: 100%


Esto significa que el panel de definición de casos está independizado del 
panel contenedor de los gráficos generados a traves de PubSub. 
El mencanismo invocación del backend (desde donde se obtienen los datos a graficar) 
se verá más adelante. 

Exposición de archivos de datos
+++++++++++++++++++++++++++++++

Cada invocación a un ejecutable del backend dependen de una entrada 
y produce una salida [#]_ en un archivo de texto. Para usuarios avanzados que conocen 
la estructura y significado de estos archivos (descriptos en :ref:'api'), es 
deseable que tengan un acceso al contenido desde la propia aplicación, para 
encontrar información numérica puntual cuya precisión se pierde en un gráfico. 

.. figure:: images/inpout.png
   :width: 80%

Esta tarea se hace a través de PubSub. El emisor envía un mensaje con tópico
``add_txt`` adjuntando como información una tupla con la ruta al archivo 
y el caso al que este cálculo pertenence. 

Por ejemplo, la función que escribe el archivo de entrada para el cálculo de 
parámetros es la siguiente:


.. literalinclude:: ../src/apimanager.py
   :pyobject: ApiManager._write_conparin


El atributo :py:attr:`path_temp` está definido en el constructor de la clase 
:py:class:`API` y se trata de una ruta a un subdirectorio en la carpeta temporal, 
abstraída del sistema operativo subyacente mediante el módulo :py:mod:`tempfile`

El receptor de este mensaje es :py:class:`IOPanel` que maneja el mensaje con el 
método :py:meth:`OnAddItem` .



.. literalinclude:: ../src/panels.py
   :pyobject: IOPanel.OnAddItem


Tabla de incidencias de mensajes
++++++++++++++++++++++++++++++++


  ==============  ======================  ========================= =================== 
   Tópico           Descripción             Emisor/es                 Receptor/es    
  ==============  ======================  ========================= ===================
   log              Mensaje al usuario      varios                    LogMessagesPanel
   add_txt          Expone archivo de       ApiManager.*              IOPanel
                    backend
   clone case       Crear un nuevo caso     CasePanel.Clone           TabbedCases
                    a partir del actual
   make.*           Invoca el cálculo y     CasePanel.OnMakePlots     SuitePlotsPanel
                    genera el gráfico
   refresh all      Refresca la interfaz    varios                    MainFrame
                    de usuario
   active page      Trae a primer           PlotsTreePanel            SuitePlotsPanel
                    plano una pestaña 
                    de los gráficos
  ==============  ======================  ========================= ===================

Para un listado completo puede analizar el código fuente ejecutando 
``grep -r "pub.sendMessage"`` sobre el directorio de código fuente raiz
de GPEC. [#]_ 


Algoritmo de análisis sintáctico
==================================

Como ya se ha hecho mención, la comunicación con los ejecutables del *backend* 
se realiza mediante archivos de texto. Los archivos de salida, en particular, 
contienen (en arreglos de columnas) los vectores de datos para cada variable
de una curva. 

La tarea de delimitar la información de un texto se denomina en la lingüistica
*Análisis sintáctico* y es también un área de la informática de utilidad en la 
implementación de diversos software (como ejemplo notorio, los compiladores). 

Este trabajo implementa un analizador sintáctico (denominado 
*parser*, en ingles) para extraer los vectores numéricos (ordenados como un arreglo
bidimensionales) de los archivos de salida, obteniendo así la información necesaria
para graficar cada curva.

.. note:: 

   Para una comprensión cabal del algoritmo, es necesario estár familiarizado
   con la definición de la interfaz. Una descripción exhaustiva se expone 
   en :ref:`api`. 

Descripción
------------

El algoritmo se basa en identificar *tokens* (marcas) que declaran el inicio y final
de información válida para un diagrama, determinando así la porción de texto 
(números flotantes en formato texto) que debe extraerse. Este texto se convierte
a un objeto array de :py:mod:`numpy`.

Las marcas de inicio son cadena de tres letras mayúsculas (``VAP``,``CRI``,``LLV``, etc.)
y un renglón vacío marca el final del bloque de información.

.. figure:: images/parser.png
   :width: 80%

   Topología de la información extractada

Una estructura de datos basadas en asociaciones clave-valor (diccionarios), 
define los tipos posibles de curvas y las columnas significativas que se deben 
extraer para cada una. Iterando sobre todas las líneas del archivo se obtiene 
un nuevo diccionario cuya clave es una tupla de la forma ``(inicio, fin)`` y el 
tipo de curva como valor. 

Con esta información simplemente se "recorta" el archivo fuente completo del cual 
se realiza una copia residente en memoria [#]_ para importarlo
y convertirlo a flotantes mediante la función :py:func:`numpy.loadtxt`


Código fuente
-------------

.. literalinclude:: ../src/apimanager.py
   :pyobject: ApiManager.output2array








        
Diagramas principales
=====================
        
Diagramas de componentes
------------------------

de clases
----------

de secuencia
-------------



Estilo de codificación
======================
    
PEP8       
----



Interfaz de Usuario
====================
        
Justificación de diseño
-----------------------

Pruebas de usabilidad
---------------------




.. [#]  En 2010 el autor de *Python PySub* reescribió completamente la :term:`API`, 
        agrengando una orientación a objetos del paso de mensajes más poderosa, 
        a la que llamó *version 3*. 


.. [#]  En realidad, la llamada está intercedida por una función decoradora (``memoize``)
        que realiza un *caché* de los resultados la primera vez que se invoca. Si en 
        sucesivas llamadas los parámetros coinciden, se devuelven los datos 
        almacenados en memoria, tarea mucho más rápida que recalcular. 
        
.. [#]  El comando ``grep -r`` busca de manera recursiva una cadena (o una expresión
        regular) sobre sobre los archivos de un directorio

.. [#]  El módulo :py:mod:`cStringIO` provee un tipo de *buffers* de cadenas
        de caractéres con la misma interfaz que un archivo de texto normal. 
        Las operaciones con la información en memoria son altamente eficientes.


.. [vdLaar2002]  van de Laar, F. (2002).  *Publish/Subscribe as architectural style 
                 for component interaction (Mater's thesis)*, Phillips Research
                 Laboratories, Eindhoven


