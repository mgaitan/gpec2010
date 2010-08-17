*******************
Contexto de trabajo
*******************

.. _trabajo_interdisciplinario:

Trabajo interdisciplinario
===========================

Como se describe en la :ref:`introducción <intro>`, la computación ha revolucionado
todas las áreas de la cultura y la investigación moderna, incluyendo, por supuesto,
a la ingeniería en todas sus formas. 

Puede decirse que la ingeniería en computación (complementada con la ingeniería en sistemas) 
se ha constituido en una *meta ingeniería* requerida por todas las demás áreas. 
Es aceptable pensar que, en general, un ingeniero en computación puede 
desenvolverse  profesionalmente sin conocimientos de termodinámica, pero un ingeniero químico o mecánico
avocado a esa área tendrá dificultades para progresar si no tiene cierta destreza
en programación y sistemas de información. 

No obstante, cuando se quieren alcanzar objetivos
más altos a nivel de software, la capacidad y formación media en un profesional
de otra área se vuelve escasa: el desarrollo de software es una ingeniería por sí misma,
que va mucho más allá de la destreza en programación. 

Es saludable entonces que profesionales idóneos sean los encargados de ese 
aspecto específico del proyecto, interactuando y consultando cuestiones que conciernen
al ámbito de aplicación, aportando ideas, desarrollando una acabada *ingeniería de requerimientos* 
y explicando de manera didáctica cuando estos exceden o complejizan innecesariamente
la implementación. 

Por otro lado, desde el contexto académico y de investigación, en la :abbr:`FCEFyN` 
no existe una notoria sinergia entre las  distintas disciplinas [#]_, cuyas ventajas
expone el magíster Antonio Rey Roque en [ARR2003]_:

    Hablar de interdisciplinaridad en el contexto académico significa lograr un 
    nivel adecuado de comunicación, la integración de paradigmas, la
    ruptura de concepciones reduccionistas, el desarrollo de una cultura de aprendizaje colectivo.
    Presupone implicación profesional, multiplicación (no suma) de ideas conceptuales,
    metodológicas, procedimentales; economización de esfuerzos, de carga profesional y evaluativa.
    Implica una proceso docente educativo ágil, económico y enriquecedor para los docentes;
    procesos de aprendizaje más significativos para los alumnos; relación profesional más rica y
    afectiva entre docentes. El escenario correspondiente a un trabajo interdisciplinario no implica,
    como algunos pueden pensar, un mayor trabajo, sino, mayor riqueza, variedad y aceptación de
    actividades; mayor equidad en la distribución de tareas y recibe los beneficios afectivos y
    profesionales del trabajo en equipo. El resultado del aprendizaje en tal escenario es un saber más
    coherente, se logra mayor capacidad para enfrentar problemas.

Desde ambos puntos de vista, estas han sido las ideas que, desde el principio,
guiaron este proyecto. Como se verá en :ref:`experiencia`, el resultado fue altamente 
satisfactorio. 


Software libre
===============


El :term:`Software Libre` (SL) es aquel que respeta la libertad  de los usuarios sobre su 
producto adquirido (independientemente de si se debe pagar por ello o no) y, por lo tanto, una 
vez obtenido puede ser usado, copiado, estudiado, cambiado y redistribuido libremente [#]_.  
Esto no implica que el/la autor/a o autores del software
pierdan los derechos de autoría intelectual que son inalienables e imprescriptibles.  

La definición de SL [FSFa]_ fue concebida originalmente por Richard Stallman
a mediados de los años 80, oponiéndose a las restricciones que imponía el modelo 
de :term:`software privativo` (SP) que muchas universidades empezaban a adoptar y que 
los :term:`hackers <hacker>` [#]_ no podían aceptar. 

Desde entonces, y en especial con la aparición del sistema operativo :term:`GNU/Linux`, 
el avance del SL ha sido arrollador, siendo eslabón escencial 
para el funcionamiento de Internet desde sus orígenes hasta nuestros días [#]_, 
de los :term:`clusters <cluster>` más poderosos [#]_ y núcleo propulsor
de los dos sitios más visitados y exitosos a nivel mundial: Google [#]_ [#]_ y Facebook [#]_ .

    .. figure:: images/top500so.png
       :figwidth: 50 %

       Familia de S.O. de los 500 supercomputadores 
       más rápidos del múndo. http://www.top500.org

De cierta manera, el SL ha excedido su condición de forma de licenciamiento de software 
erigiéndose en un marco de referencia moral, político y legal para la creación 
de conocimiento en sus diversas formas. Iniciativas como `Creative Commons <http://creativecommons.org/>`_ y 
`Wikipedia <http://wikipedia.org/>`_ nacieron como extensión conceptual aplicada
a otros tipos de creaciones intelectuales. 

Entre las muchos motivos que hacen al SL un modelo 
técnicamente viable, económicamente sostenible y socialmente justo [JMiH2005]_, 
sintéticamente se mencionarán los que justifican que el software desarrollado 
para este trabajo sea liberado bajo la licencia libre :abbr:`GPL (General Public License)` [#]_

 .. important::
        
        La liberación se limita al software desarrollado por el autor de este trabajo,
        siendo este dependiente del *backend GPEC* que no es libre. 
        Si bien la utilidad de un sofware libre que depende de otro no libre es parcial,
        (ver [RMS2004]_), queda fuera de la potestad del autor la determinación
        de una liberación total, aunque enfáticamente la promueva.



Justificación
--------------

Creación desde la Universidad Pública
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La formación del autor de este trabajo, así como la de su director y codirector, 
no obstante el esfuerzo personal, son fruto de la Universidad Pública Argentina, 
privilegio al que una ínfima  porción de la sociedad accede cuando es ella toda, a través del Estado, quien 
la sostiene. Más aún, el tiempo dedicado por los docentes para guiar y evaluar
este trabajo fue sostenido con recursos públicos [#]_.

Retribuir los conocimientos adquiridos en la formación universitaria 
para beneficio del conjunto del pueblo (y por extensión, de la humanidad), 
es una obligación ética basada en la concepción misma de la universidad pública y gratuita, 
y declarada en el artículo 2 del Estatuto de la Universidad Nacional de Córdoba [UNC1]_ que 
enumera dentro de sus fines:

    la promoción de la investigación científica(...), [el] libre desarrollo de 
    la cultura, (...) la efectiva integración del hombre en su comunidad, 
    (...) [el] promover la actuación del universitario en el seno del pueblo al que pertenece,
    (...) [y] la difusión del saber superior entre todas las capas de la población.

Desarrollo basado en software libre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. epigraph::

    Los buenos programadores saben qué escribir. Los mejores, que reescribir (y reutilizar)

    -- Eric Raymon, [ER1997]_

En ninguna disciplina creativa se es absolutamente original. Basarse 
en las creaciones o ideas previas, que han sido probadas con éxito, 
presume la posibilidad de llegar a más ambiciosos y seguros resultados. 

Es un precepto que el software libre comparte con la ciencia, expresada en la 
frase atribuía a Isaac Newton: *"Si he visto más lejos es porque 
me paré sobre hombros de gigantes"* [#]_

Eric Raymond, en su famoso ensayo *The Cathedral and the Bazaar* [ER1997]_, 
expresa la ventaja desde su experiencia como programador: 

    Aunque no pretendo ser un gran programador, trato de imitarlos. 
    Una característica importante de los grandes de verdad es la vagancia constructiva. 
    Saben que te darán un diez no por tu esfuerzo, sino por los resultados, 
    y es casi siempre más fácil empezar a partir de una buena solución parcial 
    que desde la nada más absoluta. 

El lenguaje y las bibliotecas que se usaron para el desarrollo
de este trabajo son libres [#]_ (ver :ref:`tecnologias`) y ampliamente probadas por 
numerosas aplicaciones que las utilizan. Además, gran cantidad de ejemplos
y buenas ideas aplicadas en este trabajo fueron extraídas de código libre 
disponible en internet.

Sin la existencia de SL este trabajo hubiera sido muchísimo más 
costoso, tanto en términos de horas de desarrollo como en el costo de licencias 
de software privativo equivalente al utilizado, y hubiese resultado 
inalcanzable en el contexto de un proyecto integrador de grado. 

Retribuir el resultado de los beneficios usufructuados para que otros puedan servirse 
resulta un evidente acto de justicia. 

Necesidad de transparencia en el software científico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dan Gezelter, mentor de la iniciativa `Open Science <http://www.openscience.org>`_
resume en [DG2009]_ los objetivos del proyecto:

    * Transparencia en metodología experimental, observación y recolección de datos
    * Disponibilidad pública y reusabilidad de los datos científicos
    * Accesibilidad pública y transparencia de la comunicación científica
    * Uso de herramientas basadas en web para facilidad la colaboración científica. 

Sobre el primer punto agrega:

    (...) Garantizar el acceso al código fuente es realmente equivalente a publicar su metodología
    cuando el tipo de ciencia que realiza implica experimentos numéricos. Soy 
    extremista en este punto, porque sin acceso a las fuentes de los programas que 
    usamos, nos apoyamos en la fe a las capacidades de codificación de otras personas
    para llevar a cabo nuestra experimentación. En algunos casos extremos, 
    (por ejemplo, cuando el código de simulación o archivos de parámetros son privativos
    u ocultados por sus dueños), la experimentación numérica ni siquiera es ciencia. 
    Un diseño experimental "secreto" no permite a los escépticos repetir (y con 
    suerte verificar) su experimento y lo mismo ocurre con experimentos numéricos. 
    La ciencia debe ser "verificable en práctica" tanto como "verificable en principio". [#]_

Si bien el software realizado por el autor no implementa los algoritmos de cálculos numéricos, 
es una buena práctica permitir la verificabilidad de que los resultados no se 
adulteran. 

Calidad del software
^^^^^^^^^^^^^^^^^^^^

La libertad de un software no garantiza su calidad *per se*, ni mucho menos 
la ausencia de errores,  pero aumenta enormemente las posibilidades de alcanzar 
cotas altas en este aspecto. 

Según Challet y Le Du en [CLD03]_ para hacer un software de código privativo 
de igual calidad que su equivalente libre hacen falta más y mejor calificados
desarrolladores. El artículo plantea, desde un modelo matemático, que en el SL la interacción 
entre los usuarios y desarrolladores logra que los fallos sean eliminados a 
una velocidad mucho mayor que la que un grupo de programadores de software privativo de elite 
puede lograr. 

Esto radica en dos aspectos: la libertad de estudiar el código permite a cualquiera
encontrar errores en el programa y reportarlos, y la dinámica de "comunidad"
que muchos proyectos de software libre logran, donde el *feedback* entre usuarios
y desarrolladores es constante y horizontal. 

Mejor estrategia comercial
^^^^^^^^^^^^^^^^^^^^^^^^^^

Un mito, muchas veces difundido por interés [#]_ o por ignorancia, 
es que no se puede lucrar con Software Libre, lo cual es falso. Por el contrario, 
en muchos escenarios, la adopción de software libre resulta beneficiosa para 
su maximización. 

Jordi Mas enumera en [JMiH2005]_ los principales modelos negocio
que se han puesto en práctica en el SL con éxito durante los últimos años.
En particular, es importante destacar el modelo de desarrollo software como 
servicio. Sobre este modelo mas comenta:

    (...) [son] empresas que se dedican a la consultoría, desarrollo a medida de
    soluciones, formación y soporte técnico (...)
    Su valor diferencial respecto a las empresas
    tradicionales de servicios son los beneficios que
    transmiten a sus clientes por el hecho de trabajar con
    tecnologías libres – como acceso al código fuente de
    las soluciones – (...) En general, las empresas que mejor funcionan de este
    tipo son aquellas que se especializan en un área
    concreta de conocimiento (...) Ser un especialista en un área y ser
    reconocido como experto en la misma es una buena estrategia. 

Si bien el derecho a realizar modificaciones es concedido a todo el mundo, 
dentro del universo de personas o empresas capaces de llevar a cabo adaptaciones
a medida (situación plausible en un nicho tan específico como
el de *GPEC*), los autores originales del software se encuentran en una 
ventaja competitiva obvia.

Por otro lado, en nichos de software específicos y pequeños, la posibilidad de difusión (y 
en consecuencia de tracción de usuarios) que tiene un software son mucho mayores 
aprovechando la *infraestructura comunicacional* de la que el SL goza:
por el mero hecho de ser libre (y resultar mínimamente interesante) se dará 
publicidad gratuita y, mejor aún, espontánea, en numerosos sitios de noticias y 
foros de internet, puede incluirse en repositorios de software accesibles 
fácilmente desde sistemas operativos libres que facilitan la instalación y la prueba, 
y ser albergado en sitios de referencia para código libre como `SourceForge <http://sourceforge.net>`_
`GitHub <http://github.com>`_ o `Google Code <http://code.google.com>`_ 
con cientos de miles de visitas diarias. 

Más y mejores usuarios repercute, como se ha visto, en más calidad y prestigio, 
que se realimentan en un bucle virtuoso ampliando posibilidades de lucro, 
fin que está fuera de los alcances de este trabajo por no por ello descartado 
a futuro. 

    .. seealso::
        
            :ref:`lineas_abiertas`



.. [#]  Salvo quizás las más cercanas, como electrónica y computación, pero en una medida
        muy inferior a la que podría lograrse. 

.. [#]  Refiere a las cuatro libertades esenciales del software libre descriptas en [FSFa]_

.. [#]  La definición de *hacker* que el común de la gente tiene es incorrecta. 
        Vea el :ref:`glosario <glosario>` para una definición correcta.

.. [#]  En 2010, el 73% de los servidores web funciona con software libre. 
        http://news.netcraft.com/archives/2010/02/22/february_2010_web_server_survey.html

.. [#]  Hasta junio de 2010, el 91% de los 500 supercomputadores más poderosos del mundo
        funcionaban con Linux o derivados. http://www.top500.org/charts/list/35/osfam

.. [#]  Sergey Brin en una entrevista de 2000 cuenta que dentro de Google 
        *"Linux se utiliza en todas partes... en los más de 6.000 servidores así 
        como en las máquinas de todos nuestros empleados técnicos (...)
        Es tan agradable poder adaptar cualquier parte del sistema siempre que quieras."*. 
        http://www.gazetadolinux.com/pr/lg/issue59/correa.html

.. [#]  Se estima que Google tiene en la actualidad más de `200 mil servidores 
        <http://www.googlelady.com/936/google-servers-googles-data-center/>`_ . 

.. [#]  *"Facebook has been developed from the ground up using open source software"*, 
        http://developers.facebook.com/opensource/    

.. [#]  *Licencia pública general versión 3*, http://www.gnu.org/licenses/licenses.html#GPL

.. [#]  Por supuesto, habiendo podido dedicar su tiempo a otras labores, 
        los docentes aceptaron dirigir este trabajo voluntariamente, 
        actitud por la que vale reiterar el agradecimiento del autor.
        

.. [#]  Particularmente, sus licencias no exigen que el software producido o derivado 
        deba ser liberado, como sí ocurre con *GPEC* al adoptar una licencia GPL.

.. [#]  Según `la entrada en Wikipedia <http://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants#Attribution_and_meaning>`_
        la cita corresponde a Bernard of Chartres.
        
.. [#]  Traducción del inglés propia del autor del trabajo.

.. [#]  Vea :term:`FUD` en el glosario



.. [UNC1]  Universidad Nacional de Córdoba, *Estatuto de la UNC -  Misión de la Universidad*: 
           http://www.unc.edu.ar/institucional/organizacion/estatutos/mision


.. [FSFa]  Free Software Foundation, *La definición de Software libre*,  
           http://www.gnu.org/philosophy/free-sw.es.html


.. [ARR2003]  Rey Roque, Antonio (2003), *Experiencias en el trabajo 
              Interdisciplinario desde una Disciplina Básica*,
              Departamento de Matemáticas, Facultad de Informática, Universidad de
              Cienfuegos “Carlos Rafael Rodríguez”, Cuba

.. [JMiH2005]  Mas i Hernàndez, Jordi  (2005), *Software Libre. Técnicamente viable, 
               económicamente sostenible y socialmente justo*, infonomia.com (Ed.), Barcelona


.. [ER1997]  Raymond, Eric S (1997),  *The Cathedral and the Bazaar*, Open Source Software Foundation,
             Traducción al español del Proyecto Lucas, http://es.tldp.org/Otros/catedral-bazar/cathedral-es-paper-00.html

.. [RMS2004]  Stallman, Richard M (2004), *Libre pero encadenado. La trampa del Java.*, 
              :abbr:`FSF (Free Software Foundation)`, http://www.gnu.org/philosophy/java-trap.es.html

.. [DG2009]  Gezelter, Dan (2009), *What, exactly, is Open Science?*, 
           http://www.openscience.org/blog/?p=269

.. [CLD03]  Challet, D - Le Du, Y (2003), *Microscopic model of software bug dynamics: closed source versus open source*, 
            International Journal of Reliability, Quality and Safety Engineering
