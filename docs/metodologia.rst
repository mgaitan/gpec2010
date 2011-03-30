.. _metodologia:

Metodología
***********

Este capitulo detalla el marco conceptual y la metodología de desarrollo adoptada.
Esta decisión ha sido rectora de subsecuentes decisiones de diseño y, de cierta manera,  
de la tecnología adoptada para la implementación.


Metodologías Ágiles
--------------------

Este proyecto integrador ha sido guiado por un conjunto de preceptos 
comunes a las *metodologías ágiles de desarrollo de software*. 
Sin necesariamente ajustarse a ninguna en particular, se comparte
la escala de valoración hecha en Agile Manifiesto [AG-MANIF]_ que declara:

    Estamos descubriendo formas mejores de desarrollar
    software tanto por nuestra propia experiencia como
    ayudando a terceros. A través de este trabajo hemos
    aprendido a valorar:

    * Individuos e interacciones sobre procesos y herramientas
    * Software funcionando sobre documentación extensiva
    * Colaboración con el cliente sobre negociación contractual
    * Respuesta ante el cambio sobre seguimiento (estricto) de un plan

    Esto es, aunque valoramos los elementos de la derecha,
    valoramos más los de la izquierda.

Las *implementaciones* del marco conceptual propuesto por el Manifiesto de 
desarrollo ágil (como *eXtremme Programming* o *Scrum*) están estructuralmente 
concebidas para el trabajo de un equipo de desarrollo abocado al mismo proyecto. 
Como el desarrollo  del software estuvo a cargo de una sola persona 
(con la colaboración y revisión de los directores) no se ajustó 
a un método estrictamente definido para un equipo como los mencionados. 

Sin embargo, muchas ideas propuestas por estos métodos han sido aplicadas, 
concibiendo un desarrollo evolutivo con énfasis en la adaptabilidad 
de los requerimientos. 

Algunas de las técnicas y procesos ágiles involucrados en este desarrollo 
han sido la utilización de un lenguaje de muy alto nivel (ver :ref:`tecnologias` ), 
la implementación de pruebas automatizadas, la utilización de bibliotecas 
probas para la implementación de aspectos específicos de la solución, entre 
otras.   

.. _desarrollo:

Desarrollo evolutivo adaptado
-----------------------------

Según [Sommerville2004]_, el desarrollo evolutivo se basa en la idea de 
una implementación inicial, exponiéndola a los comentarios del comitente o 
los usuarios, y refinándola a través de diferentes versiones preliminares 
(versiones *beta*) hasta obtener una versión que satisfaga el conjunto de 
requerimientos planteado. 

 .. figure:: images/desarrollo_evolutivo.png

    Esquema conceptual del desarrollo evolutivo

Las actividades de especificación, desarrollo y validación se entrelazan en 
vez de separarse, con una rápida y constante retroalimentación entre estas. 

Existen dos grandes tipos de desarrollos evolutivos: 

1.  *Desarrollo exploratorio* donde el objetivo del proceso es trabajar con el 
    cliente para explorar y precisar los requerimientos y obtener un sistema 
    final. Se comienza con las partes del sistema que más cabalmente se 
    comprenden y se evoluciona agregando nuevos atributos precisados por el 
    comitente, la comunidad de usuarios o el propio equipo de desarrollo. 

2.  *Prototipos desechables* donde el objetivo del proceso es comprender 
    mejor los requerimientos. Una vez evacuadas todas las incertidumbres, los 
    prototipos se desechan y se diseña e implementa el sistema final desde el 
    principio.

En este trabajo se aplicó un proceso evolutivo de tipo exploratorio, con activa
interacción con el comitente, basándose en estrategias de desarrollo ágil mencionadas previamente. 

    .. attention::

       La adopción de principios del desarrollo ágil y el desarrollo evolutivo
       implica que no se ha utilizado un proceso de ingeniería en software formal, más 
       frecuentemente impartido en la facultad. Esto es, el proceso de diseño e 
       implementación han sido mancomunados en vez de separados estrictamente.


.. [AG-MANIF]  Varios autores (2001), *Manifesto for Agile Software Development*, http://agilemanifesto.org/

.. [Sommerville2004] Sommerville, Ian (2004) *Software Enginnering, 7th edition*, Pretince Hall
            Traducción al español por el Departamento de Ciencias de la Computación e Inteligencia 
            Artificial de la Universidad de Alicante (2005). 
