.. header::
   Propuesta de Proyecto Integrador - Martín Gaitán

.. footer::
    ###Page###



================================
Propuesta de Proyecto Integrador
================================

    
    :Estudiante: Martín Emilio Gaitán   <gaitan@gmail.com>
    :Carrera: Ingeniería en Computación (Plan 285/2005)
    :Director de PI: Prof. Gustavo Wolfmann
    :Codirector de PI: Dr. Martín Cismondi
    
    :Palabras clave: software, graficación, termodinámica, diagramas de fases, 
                     ecuaciones de estado, sistemas binarios.

    :Fecha: 30 de julio de 2010
    :revisión: 12


.. raw:: pdf

   PageBreak oneColumn



Introducción 
============


GPEC, *Global Phase Equilibrium Calculations*, es un software  que 
permite la obtención de curvas de equilibro global entre fases fluidas y otros diagramas 
termodinámicos para sistemas binarios, que se calculan mediante ecuaciones 
de estado. Es útil para fines educativos, académicos, científicos 
e industriales. 

GPEC fue desarrollado originalmente por el Dr. Martín Cismondi Duarte en el marco
de su tesis doctoral en Ingeniería Química por la Universidad Técnica de Dinamarca, 
en 2005.

Está basado en métodos numéricos y algoritmos desarrollados e implementados 
en lenguaje Fortran por el Dr.Cismondi en colaboración con el Prof. Michael Michelsen, 
del Department of Chemical Engineering, 
DTU (Dinamarca),  y el Prof. Marcelo Zabaloy de la Universidad Nacional del Sur, 
(Argentina). 

La falta de mantenimiento, el lenguaje de desarrollo 
adoptado y la incapacidad de expandir las funcionalidades, entre otros, 
determinan la necesidad de rediseñar este software desarrollándolo bajo 
una nueva arquitectura, labor que se propone como  Proyecto Integrador (PI) para 
final de carrera de grado en Ingeniería en Computación. 


Dirección y seguimiento del Proyecto Integrador
===============================================

Este PI estará dirigido por el **Prof. Gustavo Wolfmann**, titular de la 
cátedra *Algoritmos y Estructuras de datos*  y *Paradigmas de Programación*, 
de Ingeniería en Computación, en el rol de **Director del Proyecto**, con el  
el Dr. `Martín Cismondi <http://idtq.efn.uncor.edu/Martin-Cismondi-Duarte>`_ , 
profesor de la cátedra *Termodinámica Química* de la carrera Ingeniería Química 
e investigador de Conicet, como **Co-director de proyecto** y mentor del 
proyecto. 


Requerimientos
==============

El plan de desarrollo y la ingeniería de requerimientos completa se realizará
como parte del proyecto, pero haciendo un somero listado, el proyecto 
debe satisfacer *de mínima*, las funcionalidades provistas por la versión
a reemplazar. 

Esto implica dar soporte a distintos diagramas en 2D:

 * Diagrama de equilibrio de fase global en diferentes proyecciones
 * Diagramas Pxy para temperatura constante 
 * Txy para presión constante
 * Diagramas isopléticos

Además, de la utilización de al menos 5 modelos termodinámicos:

 * Soave-Redlich-Kwong EOS (Soave, 1972)
 * Peng-Robinson EOS (Peng and Robinson, 1976)
 * RK-PR EOS (Cismondi and Mollerup, 2005)
 * Simplified Perturbed Hard Chain Theory EOS (Kim et al., 1986)
 * Perturbed Chain Statistical Associating Fluid Theory (Gross
   and Sadowski, 2001)

Si bien las proyecciones y funcionalidades incorporables a GPEC son vastas,
y darán lugar a un plan de trabajo a largo plazo que exceden las alcanzables por 
este proyecto integrador, los requerimientos enmarcados dentro del mismo serán acotados a un 
*rediseño integral de la arquitectura*, manteniendo compatibilidad y separación funcional 
con los algoritmos de cálculo numérico implementados en Fortran.  

Este implica que la aplicación mantendrá su concepción de *Front-end*, 
que permite al usuario la gestión intuitiva del software subyacente y una 
potente visualización de los cálculos obtenidos. 


Plan de trabajo
===============

Cronograma tentativo
--------------------

Semana 1 a 4 
^^^^^^^^^^^^
- Relevamiento del estado actual
- Estudio de factibilidad 
- Rediseño arquitectónico 
- Informe de proyecto 
- Lectura de bibliografía

Semana 5 - 7
^^^^^^^^^^^^

- Estudio de la API de comunicación (archivos de entrada y salida con el software
  de cálculo subyacente)
- Analizador sintáctico (parser) de datos de salida y rutinas de conversión a arrays numéricos
- Prototipo de graficación (sin GUI) de archivos de salida para algunos digramas 
  de fase
- Prototipo de interfaz GUI
- Testing estático


Semana 8 - 10
^^^^^^^^^^^^^
- Prototipo de interfaz de usurio. 
- Gestión de proyectos.
- Implementación de diagramas 2D (fase global)
- Modelo de gestión de base de datos (Alta, Baja, Modificación)
- Testing: pruebas unitarias automatizadas

Semana 11 - 13
^^^^^^^^^^^^^^
- Configuración y manipulación de gráficos
- Exportación de datos
- Implementación de otras ecuaciones de estado
- Revisión y refactorización
- Testing

Semana 14 - 15
^^^^^^^^^^^^^^
- Testing y debugging
- Release


Bibliografía
============

Ingeniería en Software
----------------------
- *Refactoring to Pattern*. Joshua Kerievsky, Addison Wesley, 2004
- *Engineering the User Interface From Research to Practice*, Miguel Redondo, Crescencio Bravo 
  y Manuel Ortega, Springer Science, 
- *El testing como parte del proceso de calidad del software*, Departamento de 
  Testing del Instituto Nacional de Tecnología Industrial - Sede Córdoba, INTI, 2010

Diseño de GUI
-------------
- *GUI Bloopers 2.0 Common User Interface Design Don'ts and Dos*,  Jeff Johnson, Morgan Kaufmann Publishers, 2008
- *User Interface Design for Programmers*, Joel Spolsky, Apress, 2008


