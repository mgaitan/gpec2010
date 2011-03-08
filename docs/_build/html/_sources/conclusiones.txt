Conclusiones
************


Logros
======

El desarrollo de este proyecto ha satisfecho los requerimientos planteados. 
El software obtenido constituye una mejora cualitativa y cuantitativa 
de funcionalidad y facilidad de uso respecto a la versión preexistente. 

Se consiguió una aplicación multiplataforma a partir de una única rama de código
que ha sido probada en sistemas Windows XP, Windows Vista, Windows 7 y 
las distribuciones con kernel Linux  Ubuntu y Red Hat.

Los gráficos producidos tienen alta calidad, con herramientas de manipulación 
accesibles desde la misma interfaz (barra de herramientas y menú contextual) 
que permiten el control de escala, el deslizamiento, el manejo del historial de visualización, 
ocultación de curvas, escala logarítmica, visualización de grilla, etc. 

La generación de diagramas 3D constituye una funcionalidad de alta repercusión,
sobre todo para la compresión y el estudio introductorio del comportamiento del 
equilibrio de fases. La naturaleza interactiva (rotación, superposición de diagramas)
permite complementar y asimilar el conocimiento, tarea compleja basándose
en diagramas 2D típicos de la bibliografía. 

Como ya se ha mencionado, un aspecto de especial interés fue la mejora 
en la usabilidad que ha sido estudiada mediante algunas pruebas (por ejemplo, el 
comportamiento de usuarios con conocimiento del dominio del problema que usan 
por primera vez la aplicación, o usuarios que no comprenden el dominio pero logran 
hacer "funcionar" el programa intuitivamente). La conclusión es que la 
interfaz es intuitiva y bien lograda aunque se trate de un aspecto sensible 
a un proceso de mejora continua. 

La calidad de la los gráficos, exportable en múltiples formatos aptos para 
la publicación científica (por ejemplo :abbr:`EPS (Encapsulated PostScript)`, 
incrustable en documentos generados con LaTeX) también es una característica 
superadora y bien recibida por los usuarios, ya que evita el procesamiento gráfico
de "capturas de pantalla" (con resultados de pobre calidad) o la graficación 
de los *sets* de datos mediante otras herramientas de software. 


Observaciones respecto a la tecnología empleada
================================================

La utilización de Python como lenguaje para la computación científica ha sido 
una práctica en constante crecimiento alrededor del mundo, tanto en ambientes 
académicos como de la industria. Prueba de esto es el éxito de la conferencia  
*"SciPy: Python for Scientific Computing Conference"* que durante 2011 tendrá 
su 10º edición [#]_ en Austin, Estados Unidos, mientras que en agosto se hará la 4º edición de
la versión europa, *"EuroScipy"*, en París, Francia. 
La edición de 2010 convocó a más de 200 profesionales (ingenieros, matemáticos, 
físicos, químicos, biólogos), 47 empresas involucradas y los auspicios destacadados 
de Dell, Microsoft y el gobierno de India. 

En este último pais, vanguardia mundial en la industria del desarrollo de software y en la calidad
de su educación superior técnica, en el año 2009 se ha puesto en marcha un programa denominado
:abbr:`FOSSE (Free and Open source Software for Science and Engineering Education)` 
con un presupuesto global de 1000 millones de dólares para que "los estudiantes 
de ciencias e ingenierías usen herramientas open source para todas sus necesidades 
computacionales, mejorando así la calidad de la enseñanza y el aprendizaje" [#]_ . 
Uno de las tres pilares programáticos es el uso de Python para la computación científica. 

Además, Python ha obtenido el premio a "mejor lenguaje de programación" 
durante 3 ediones consecutivas (2008-2010) en el programa 
*Readers' Choice Awards* de la revista especializada *Linux Journal* [#]_

Por otra parte, el conjunto de herramientas complementarias (Matplotlib y Numpy) constituyen
a esta altura casi un estándar de facto para el software científico con Python, 
con probado éxito de integración y cuyas comunidades de desarrolladores y 
usarios están intrínsecamente relacionadas 

En este contexto de creciente aceptación, la elección de Python y sus complementos
constituyó un acierto, no sólo por los resultados satisfactorios en relación 
a los objetivos y tiempos propuestos, sino porque se suma a una corriente de modernización 
tecnológica de los ámbitos científicos tecnológicos, en particular en lo relacionado 
con el desarrollo de software, aportando calidad, facilidad y potencia de prestaciones. 

Por último, si bien todavía no ha podido cuantificarse, la decisión de 
mantener el proyecto bajo una licencia libre permitirá no sólo mayor facilidad
para que la comunidad de usuarios reporte (y, eventualmente, resuelva) fallos, 
sino para potenciar sus posibilidades de disfusión, accediendo a circuitos a los 
que el software privativo (y comercial) no accede sin costosas campañas publicitarias. 


Tiempo de desarrollo 
=====================

Puede decirse que el tiempo insumido para su concreción fue mayor que el deseado 
[#]_, diversas métricas dan cuenta que se está dentro de los tiempos 
esperables para un proyecto de esta envegadura. 

Más aún, analizando el historial de revisiones del repositorio,  
puede notarse que durante algunas semanas se realizaron muchos avances 
(infiriendose esto, con cierto margen de error, desde la cantidad de 
*commits* realizados) mientras que en otras estuvo detenido. Puede concluirse de 
esto que el ritmo de desarrollo pudo haber sido más alto y, consecuentemente, 
haber alcanzado los objetivos propuestos con anterioridad, si hubieran existido 
las condiciones (económicas, académicas, laborales, etc.) para una dedicación fulltime. 

 
.. todo:: grafico historial de revisiones (tortoise)


Costo de desarrollo
===================

Según la herramienta de análisis de código `Ohloh <https://www.ohloh.net>`_  
que utliza el algoritmo COCOMO [#]_,  el código de GPEC se compone de 
aproximadamente 6700 líneas de código Python, lo que insume un esfuerzo estimado 
de 1 programador/año. Según un salario internacional estándar para un proyecto de software con 
esta complejidad y lenguaje, el costo del software (sin su documentación) se 
estima en **u$s 81,053**
    
Contemplando la escritura de la documentación (este reporte), el esfuerzo estimado 
se eleva a 3 desarrolladores/año y **u$s 151.358** de costo total [#]_. 

.. figure:: images/cocomo.png
   :width:  30%

Mediante la herramienta `SLOCCount <http://www.dwheeler.com/sloccount/>`_ 
de David Wheeler el conteo de líneas es de 5634, un esfuerzo de 14.74 meses y un 
costo total estimado de **$ 162,167**, debido a un factor de *overhead* (relacionado
con la complejidad) de 2.4 :: 
 

    tin@azulita:~/facu/pi/src$ sloccount --personcost 55000 ./
   
    (...)

    Totals grouped by language (dominant language first):
    python:        5627 (99.88%)
    xml:              7 (0.12%)

    Total Physical Source Lines of Code (SLOC)                = 5,634
    Development Effort Estimate, Person-Years (Person-Months) = 1.23 (14.74)
     (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
    Schedule Estimate, Years (Months)                         = 0.58 (6.95)
     (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
    Estimated Average Number of Developers (Effort/Schedule)  = 2.12
    Total Estimated Cost to Develop                           = $ 162,167
     (average salary = $55,000/year, overhead = 2.40).
    SLOCCount, Copyright (C) 2001-2004 David A. Wheeler


Impacto
=======

Si bien la publicación y difusión de las versiones públicas de este software
se han mantenido como versiones "beta" manteniendo en paralelo el acceso a descarga 
de la versión anterior como version "estable", esta nueva versión de GPEC ya ha 
tenido experiencias de uso. 

Durante el mes de noviembre de 2010, la cátedra *Termodinámica*, correspondiente al 
4º cuatrimestre de la carrera Ingeniería Química de la Facultad de Ciencias Exáctas, 
Físicas y Naturales (Universidad Nacional de Córdoba), utilizó la nueva versión
para su prácticas de laboratorio, con gran aceptación y buenos resultados por parte
de los alumnos. 

Con vista a la experiencia del corriente año, la cátedra de la asignatura tiene como plan 
preparar un artículo sobre la mejora pedagógica de la ensañanza de termodinámica
asistida con el uso de esta nueva versión de GPEC. 

Asimismo, este trabajo permitió la publicación de un *poster* titulado 
"Una nueva interfaz de usuario y mayores prestaciones para el software GPEC", 
con la firma del desarrollador y los directores Cismondi y Wolfmann, 
en las conferencias PyCon Argentina 2010 [#]_ y RITeQ 2010 [#]_

.. figure:: images/poster.jpg
   :width: 80%
    
   Poster expuesto en el congreso PyCon Argentina 2010. Fotografía de Elías
   Andrawos. 


.. _experiencia:

Experiencia de trabajo
======================

El trabajo interdisciplinario que ha involucrado profesionales del área de la ingeniería en 
computación y de la ingeniería química ha sido exitoso y abre las puertas a nuevas 
y más profundas colaboraciones.

Si bien GPEC en sí constituye el principal logro, la experiencia de trabajo y la 
*know how* adquirido repercute en beneficio no sólo del autor, sino de las distintas áreas, 
los docentes involucrados y futuros tesistas que se aboquen a un proyecto similar
o a la continuación de este mismo. 

Asimismo, en el mes de enero de 2011 se presentó un proyecto al programa "Córdoba Innovadora", 
impulsado por una articulación de Agencia para el Desarrollo Económico de la 
ciudad de Córdoba, el Gobierno de la Provincia de Córdoba y la Municipalidad de Córdoba
cuyo objeto es el cofinanciamiento de "la implementación de innovaciones que mejoren productos, procesos, 
sistemas de organización, marketing y/o comercialización" [#]_ . El proyecto lleva
como título "Adaptación, manipulación y graficación de datos utilizando el lenguaje
de programación Python", y se trata de un programa de capacitación para investigadores
de IDTQ, basado en la experiencia adquirida con las tecnologías involucradas en este 
proyecto. 


.. _lineas_abiertas:

Líneas de trabajo abiertas
==========================

Mejora y "refactorización" a patrones de diseño
-----------------------------------------------

Como se ha visto, GPEC se vale de diversos patrones de diseño de software y 
especialmente del patrón *Publisher/Subscriber*. No obstante, para garantizar
aspectos como mantenibilidad, escalabilidad y seguridad del software sería deseable
realizar un proceso de refactorización a patrones ([JK1999]), en particular en lo 
concerniente a una arquitectura de separación más acabado entre lógica e interfaz.


GPEC como aplicación Web
-------------------------

Con la popularización y el incremento de velocidad de los accesos a Internet, 
en los últimos años la "computación en la nube" (Cloud Computing) [#]_
se ha constituido como una tendencia para el desarrollo de software en general, 
excediendo los dominios de las *redes sociales*, los juegos y las aplicaciones
orientadas a la comunicación corporativa que dieron su origen. 

Esta tendencia se acentúa día a día con nuevos dispositivos que acceden a la red 
(como *smartphones*, *tablets* o *netbooks*) que sin importar cuanto poder de cálculo
tengan por sí mismos, pueden acceder información y solicitar procesamientos 
a servidores online. 

Aplicaciones en la "nube" como `Google Docs <http://docs.google.com>`_ virtualmente
reemplazan paquetes de software de escritorio para ofimática, con la ventaja de independizar al 
usuario del soporte físico de la información, las actualizaciones del software, 
y el características subyacentes de su equipo cliente. Se suman además las posibilidades "multiusuario" 
que brinda la red; por ejemplo, la edición simultánea de un documento entre distintos
usuarios. 

Intentos más osados (aunque algo inmaduros) como `eyeOS <http://eyeos.info/>`_ 
intentan constituirse en un reemplazo total del sistema 
operativo, integrando ofimática, almacenamiento de datos, comunicación, edición 
gráfica, ocio, etc. en un "escritorio virtual" accesible via web. 

Llevado al campo del software científico, donde el aspecto colaborativo es escencial
por génesis, el paradigma tiene especial asidero y de esto da cuenta, por ejemplo, 
la conferencia *Science Online London* realizada en 2010 [#]_ cuya pregunta
disparadora es *"¿Cómo la web está cambiando la ciencia?"*
Entre muchos aspectos considerables para una respuesta,  surge como ejemplo aplicado
la plataforma `Sage Notebook <http://www.sagenb.org/>`_,  que brinda una aplicación  
online, interactiva, colaborativa y abierta para el desarrollo matemático. 

Dado el desarrollo actual, este escenario es técnicamente viable al corto plazo. 
Es decir, es posible, sin demasiado trabajo, convertir (o complementar) GPEC como 
aplicación web, de manera que el usuario no tenga que bajar ni instalar ningun software en su equipo
y pueda generar diagramas directamente "online". 

Esta posibilidad implica una potencial estrategia de comercialización, en el marco
de lo que se conoce como :abbr:`SaaS (Software as a Service)` [#]_

Nuevas funcionalidades
----------------------

Durante el transcurso del proyecto surgieron muchas ideas de mejoras posibles. 
Se listan a continuación algunas de ellas: 

* Consola interactiva que permita la manipulación avanzada de gráficos y vectores
  de datos. Esta característica ha sido parcialemente implementada. 
 
* Métricas automáticas de los diagramas que indiquen rangos interfaciales y puntos críticos
  de manera más precisa

* Generación de videos de animación a partir de una rotación paso a paso de un diagrama 3D 
  y la correspondiente captura (exportación). 
  
* Configurabilidad de los parámetros de visualización, que permitan de manera no 
  programática cambiar colores, espesores, estilos y demás opciones de las curvas
  trazadas. Esto permitiría, por ejemplo, optimizar un diagrama para la presentación
  en escala de grises, donde el contraste de distintos colores muchas veces 
  se vuelve indistinguible. 

* Mejora en la interoperabilidad y exportación de datos. 





.. [#]  Sitio web: http://conference.scipy.org

.. [#]  Sitio web: http://fossee.in/

.. [#]  Sitio web: http://www.linuxjournal.com/content/readers-choice-awards-2010

.. [#]  Con cierta perspicacia puede observarse que el autor bautizó el nombre clave del proyecto 
        como ``GPEC 2010`` (tal es el nombre utilizado en *Google Code*) 
        donde se refleja que la expectativa era concluir el trabajo durante 
        dicho año. 

.. [#]  Cocomo es un algoritmo de estimación de costos de software que utiliza una regresión
        de la evolución del proyecto. Ver http://en.wikipedia.org/wiki/COCOMO . 

.. [#]  Una corrección no desestimable a este cálculo es que se calcula el costo de la 
        documentación fuente en *restructuredText* y la generada en HTML de manera automática 
        con *Sphinx*,  que representa aproximadamente un 23% del costo total

.. [#]  "Conferencia Python Argentina", sitio web:  http://ar.pycon.org/2010/about/

.. [#]  "II Reunión Interdisciplinaria de Tecnología y Procesos Químicos". Sitio 
        web: http://riteq.efn.uncor.edu

.. [#]  Al término de la presentación de este reporte la agencia organizadora no
        ha expedido sobre la aprobación o no del proyecto. Sitio web: http://adec.org.ar/

.. [#]  El "cloud computing" es un paradigma que permite ofrecer servicios de computación a través de Internet.

.. [#]  "How is the web changing science?". Sitio web:  http://www.scienceonlinelondon.org/        

.. [#]  Ver http://en.wikipedia.org/wiki/Software_as_a_service

.. [JK1999] Kerievsky, Joshua (1999) *Refactoring to Patterns*, Addison-Wesley

