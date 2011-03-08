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

Implementación en GPEC
^^^^^^^^^^^^^^^^^^^^^^^^

En GPEC se ha utilizado el paquete `Python Pubsub <http://pubsub.sourceforge.net/>`_
de Oliver Schoenborn, en su versión 1 [#]_ . Esta implementación es muy sencilla
y se basa en la existencia de un objeto único (Ver :ref:`singleton`), ``pub``
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


Singleton
---------

Ejemplos de implementación
^^^^^^^^^^^^^^^^^^^^^^^^^^^

        
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




.. [#]  En 2010 el autor de este software reescribió completamente la :term:`API`, 
        agrengando una orientación a objetos del paso de mensajes más poderosa, 
        a la que llamó *version 3*. 


.. [vdLaar2002]  van de Laar, F. (2002).  *Publish/Subscribe as architectural style 
                 for component interaction (Mater's thesis)*, Phillips Research
                 Laboratories, Eindhoven


