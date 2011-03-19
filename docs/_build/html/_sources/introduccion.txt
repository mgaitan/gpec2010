.. _intro:

*************
Introducción
*************

En sus orígenes y durante muchas décadas, la computación estuvo vinculada
estricta e intrínsecamente al mundo de la ciencia. Este vínculo fue 
retroalimentándose a lo largo de la historia, permitiendo tecnologías que 
abarataron y multiplicaron la potencia de las computadoras y, en el otro sentido, 
ayudando a resolver complejos interrogantes que sin la capacidad computacional los 
científicos no hubieran podido responder. 

Es evidente que en la actualidad las computadoras ya no son exclusividad de 
selectos laboratorios o universidades y su uso generalizado ha modificado 
drásticamente la cultura y la calidad de vida de las personas, teniendo un rol
*sine qua non* en el trabajo, la comunicación, el ocio, etc. 

Esta popularización abrió amplísimos campos de desarrollo de la computación, 
pero, aunque ya no el único, el campo de la :term:`computación científica` sigue 
siendo de gran importancia. 

Diversas áreas de la ciencia y la ingeniería han 
sido revolucionadas por el software para cálculo, visualización 
y simulación disponible. Por nombrar sólo dos ejemplos, 
herramientas como *MATLAB®* o *Mathematica®* 
forman parte del día a día en la labor de ingenieros e investigadores. En "nicho" 
puede hacerse aquí una distinción entre software científico/técnico 
de propósito general como los mencionados (independientemente de que 
tengan mayor aceptación en un campo u otro) de los que son 
de propósito específico y realizan un conjunto de tareas puntuales (software aplicativo).

Este trabajo se incluye en la segunda categoría ya que se trata de una aplicación 
científica multiplataforma, con interfaz gráfica de escritorio, que basada en programas de 
cálculo preexistentes permite realizar *diagramas de equilibro de fase* en 2 y 3 dimensiones 
que son de suma utilidad para la enseñanza, la investigación y la aplicación
industrial.


Descripción
===========

:abbr:`GPEC (Global Phase Equilibrium Calculations)` [#]_, es un software para la  
obtención de curvas de equilibro termodinámico de fase global  
para :term:`sistemas binarios <sistema binario>`, que se calculan mediante 
:term:`ecuaciones de estado <ecuación de estado>`. 
Es útil para fines académicos, científicos y de desarrollo industrial. 

*GPEC* fue desarrollado originalmente por el Dr. Martín Cismondi Duarte, codirector de este trabajo, 
en el marco de su tesis doctoral [#]_ en Ingeniería Química por la Universidad Técnica de Dinamarca [#]_, en 2005 y luego ampliado junto a Diego Nuñez.

Está basado en métodos numéricos y algoritmos desarrollados principalmente por Cismondi 
en colaboración con el Prof. Michael Michelsen, del Department of Chemical Engineering, 
DTU (Dinamarca), y el Prof. Marcelo Zabaloy de la Universidad Nacional del Sur, 
(Argentina). 

Actualmente es un proyecto dirigido por el Prof. Esteban Brignole de 
:abbr:`PLAPIQUI (Planta Piloto de Ingeniería Química)` [#]_
en colaboración con el :abbr:`IDTQ (Investigación y Desarrollo en Tecnologías Químicas)` [#]_ 

El software tiene una arquitectura de capas con un mecanismo de comunicación. 
El :term:`Back end` corresponde al conjunto de programas (codificados en lenguaje Fortran) que implementa los algoritmos
de cálculo . El :term:`Front end`, denominado *Visual Gpec* es la interfaz 
de usuario que genera datos de entrada con formato comprensible por los algoritmos
y procesa las salidas generando distintos gráficos. Para detalle sobre esta arquitectura
puede ver :ref:`modelo`. Para mayores detalle sobre la versión preexistente de GPEC vea :ref:`relevamiento`.


     .. important::
    
        Estrictamente, *GPEC* es el conjunto de aplicaciones de cálculo 
        desarrolladas por Cismondi
        Con el advenimiento de la primera interfaz gráfica *Visual Gpec*, se comenzó a 
        llamar *GPEC* al conjunto de software, y es, salvo
        aclaración explícita, la asepción que tiene en este libro. 





Motivación
==========

GPEC es un software que goza de cierta popularidad en el ambiente científico- 
académico. Se utiliza, por ejemplo, en el curso intesivo de postgrado *High Pressure Technology in 
Process and Chemical Industry* en el marco del programa Socrates Erasmus de la Unión Europea [#]_. 
Dicho curso se dicta iterativamente en distintas universidades europeas de Alemania, 
Italia, España, Holanda, etc. 

Hasta el momento no se conoce ningún otro software con capacidades equivalentes, 
lo que implica una creciente comunidad de usuarios, pertenecientes no sólo a instituciones académicas y de investigación, si no también a industrias.

Sin embargo, algunos factores han sido determinantes para el virtual congelamiento de su desarrollo
desde el año 2008. En particular:

* La falta de recursos técnicos especializados en el desarrollo de software
  vinculados a los grupos que impulsan GPEC

* La ausencia de documentación 

* La complejidad que ha alcanzado el proyecto 

* El diseño :term:`cerrado <software cerrado>`, no reutilizable y 
  poco extensible adoptado

    .. seealso:: :ref:`problemas`
        

Importancia 
===========

Las potencialidades técnicas, científicas e incluso comerciales de este software
son amplias, ya que su *nicho* tiene aplicación en la industria alimenticia, 
petroquímica, etc. 

También es útil como herramienta educativa, donde los estudiantes consolidan
conceptos teóricos y manipulan parámetros obteniendo una visualización interactiva
de los resultados.

    .. seealso::  Para un detalle sobre este aspecto vea :ref:`aplicacion`


Alcance
=======

El alcance de este trabajo es el rediseño y la implementación de una nueva aplicación
de generación de gráficos para *GPEC*, cubriendo y superando las prestaciones ofrecidas 
hasta el momento, contemplando los mecanismos de comunicación con el software de cálculo
subyacente sin alterarlo de manera alguna.


Objetivos
=========

Objetivo general
----------------

El objetivo principal que persigue este trabajo es:

* Desarrollar un software *front end* totalmente compatible con el *back end*
  existente que reemplace al actual (*Visual Gpec*), orientado a un desarrollo
  prolongado y extensible, basado en un lenguaje de programación moderno y bibliotecas
  en desarrollo activo. 
  Debe satisfacer las funcionalidades con las que 
  la versión actual cuenta, ampliándolas y mejorándolas en algunos aspectos como 
  la ergonomía, la calidad de los diagramas producidos, 
  la :term:`usabilidad` general, y aspecto visual del programa.

Objetivos específicos
----------------------

Los objetivos específicos del proyecto son:

* Estudiar y documentar la versión preexistente del software. Vea :ref:`relevamiento`.

* Estudiar y documentar el mecanismo de comunicación entre el *front end* y el 
  *back end* . Vea :ref:`api`. 

* Dilucidar fallas de diseño desde el punto de vista del usuario
  e idear sus soluciones para incluirlas como nuevos requerimientos.

* Relevar nuevos requerimientos.

* Investigar metodologías, procedimientos y paradigmas del desarrollo de software
  y justificar las adoptadas para este proyecto

* Investigar tecnologías (lenguajes de programación, bibliotecas de funciones, 
  etc) y justificar las adoptadas. 

* Codificar y documentar el proyecto de manera que satisfaga el conjunto
  de requerimientos planteados.

* Verificar y validar la implementación. 


    .. seealso::
            
        :ref:`requerimientos`




.. [#] Web: http://gpec.efn.uncor.edu

.. [#] *Global phase equilibrium calculations: Critical lines, critical end points 
       and liquid-liquid-vapour equilibrium in binary mixtures*, M Cismondi, ML Michelsen 
       - The Journal of Supercritical Fluids, 2007 - Elsevier

.. [#] DTU - Danmarks Tekniske Universitet. Web http://www.dtu.dk/

.. [#] Es un instituto de investigación, educación y desarrollo de tecnología 
       con sede en la ciudad de Bahía Blanca, dependiente de la Universidad 
       Nacional del Sur (UNS) y del Consejo Nacional de Investigaciones Científicas 
       y Técnicas (CONICET). Web: http://www.plapiqui.edu.ar

.. [#] Grupo de investigación de la Facultad de Ciencias Exáctas Físicas
       y Naturales. Web: http://www.idtq.efn.uncor.edu

.. [#] http://atom.uni-mb.si/Labs/lab_sep/socrates.htm


