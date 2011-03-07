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
equilibrio de fase. La naturaleza interactiva (rotación, superposición de diagramas)
permite complementar y asimilar el conocimiento que es mucho más complejo basandose
en diagramas 2D típicos de la bibliografía. 

Como ya se ha mencionado, un aspecto de especial interés fue la mejora 
en la usabilidad que ha sido estudiado mediante algunas pruebas (por ejemplo, el 
comportamiento de usuarios con conocimiento del dominio del problema que usan 
por primera vez la aplicación, o usuarios que no comprenden el dominio pero logran 
hacer "funcionar" el programa intuitivamente). La conclusión es que la 
interfaz es intuitiva y bien lograda aunque se trate de un aspecto sensible 
a un proceso de mejora continua. 

La calidad de la los gráficos, exportable en múltiples formatos aptos para formatos 
de publicación científica (por ejemplo :abbr:`EPS (Encapsulated PostScript)`, 
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
costo total estimado de **$ 162,167**, devido a un factor de *overhead* (relacionado
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





.. _lineas_abiertas:

Lineas de trabajo abiertas
==========================


.. _experiencia:

Experiencia de trabajo
======================



.. [#]  Sitio web: http://conference.scipy.org

.. [#]  Sitio web: http://fossee.in/

.. [#]  Con cierta perspicacia puede observarse que el autor bautizó el nombre clave del proyecto 
        como ``GPEC 2010`` (tal es el nombre utilizado en *Google Code*) 
        donde se refleja que la expectativa era concluir el trabajo durante 
        dicho año. 

.. [#]  Cocomo es un algoritmo de estimación de costos de software que utiliza una regresión
        de la evolución del proyecto. Ver http://en.wikipedia.org/wiki/COCOMO . 


.. [#]  Una corrección no desestimable a este cálculo es que se calcula el costo de la 
        documentación fuente en *restructuredText* y la generada en HTML de manera automática 
        con *Sphinx*,  que representa aproximadamente un 23% del costo total

