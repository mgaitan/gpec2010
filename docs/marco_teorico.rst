.. _marco:

Marco Teórico
**************

Debido a la naturaleza multidisciplinaria de este trabajo posiblemente sea leído
y evaluado por profesionales o interesados de/en las distintas áreas de incumbecia
(química y computación). 

    .. seealso::

        :ref:`trabajo_interdisciplinario`.

Dado que no necesariamente se tiene un conocimiento
sólido fuera de la especificidad de la profesión, en este capítulo se presentarán 
**conceptos generales de termodinámica y equilibrio de fases** 
(que no pretenden exhaustividad pero sí precisión) . Para definiciónes de términos puntuales, 
consulte el :ref:`glosario <glosario>`.

Como complemento, en :ref:`tecnologias` se verá una introducción a las 
tecnologías, intentando un desarrollo de los conceptos apto para la comprensión 
de todos los lectores.


Diagrama de fases de sistemas binarios
======================================

Un :term:`diagrama de fase` es un tipo de gráfico utilizado para mostrar 
las condiciones en las que distintas fases termodinámicas de un sistema pueden ocurrir en 
equilibrio. Se representa en función de variables que caracterizan el :term:`estado 
intensivo <propiedades intensivas>` del sistema fisicoquímico.  

El estudio introductorio de la :term:`termodinámica` se centra en 
:term:`sustancias puras <sustancia pura>` o mezclas a composición constante. En este caso, el sistema es descripto por dos variables.  Un diagrama de fase típico para estos 
sistemas, es el *Presión vs. temperatura* que muestra la Figura :ref:`ptbasic-num`.

    .. _ptbasic-num:

    .. figure:: images/Phase-diag_es.png
       :width: 80%
       
       La línea verde indica los puntos de congelamiento. La azul los de 
       ebullición. La línea punteada muestra un 
       comportamiento particular del agua. 

Así, para determinada presión y temperatura, la sustancia o mezcla constante 
puede estar en fase líquida, gaseosa o sólida, o bien en un punto crítico.     
Es decir, qué porcentaje o fracción de la mezcla corresponde a cada una de las 
dos sustancias del sistema. La composición habitualmente se mide en fracción molar, 
fracción masa, o concentración molar. 


Para :term:`sistemas binarios <sistema binario>` (una mezcla de dos componentes) 
la *composición*  (o, complementariamente, la *densidad*) se vuelve 
una variable del sistema, cuya representación gráfica son curvas en el 
espacio :math:`R^3` (gráfico tridimensional) como muestra la figura :ref:`tipoI-num`. 
Para un determinado estado *T-P-x* (*x* es composición, en general expresada como fracción molar del compuesto más volátil) el sistema se encuentra en *zonas de equilibrio* vapor/líquido, líquido/líquido, vapor/sólido, líquido/sólido u otros casos particulares. 

   .. _tipoI-num:

   .. figure:: images/ejTipo1.png
      :width: 70%

      Un diagrama P-T-x para un sistema binario de Tipo I. 

La :index:`proyección ortogonal` de estas curvas tridimensionales sobre los planos 
correspondientes genera los gráficos cartesianos bidimensionales PT, Px, Tx 
(y sus análogos para densidad) que son típicos de la bibliografía del tema. Un ejemplo
de proyección *Temperatura vs. Composición* se muestra en la figura :ref:`tx1-num`. 


.. _tx1-num:

.. figure:: images/ejemploTx.png
   :width: 70%

   Un diagrama T-x para un sistema binario, mostrando la línea crítica y 
   otras informaciones. 

El **comportamiento termodinámico de los sistemas binarios** no es uniforme 
cualquiera sean los compuestos de la mezcla. Existen seis **tipos de 
comportamiento**, de los cuales los tipos I, II, III y IV (enumerados en orden 
creciente de complejidad) son los más comunes (todos calculables a través de 
GPEC). Esta complejidad creciente del comportamiento se observa en la aparición 
de equilibrios líquido-líquido, líquido-líquido-vapor, líneas azeotrópicas, etc. 

.. figure:: images/beha_types.png
   :width: 80%

   Representación de diagramas P-T para los primeros 4 tipos de comportamiento


Equilibrio termodinámico
========================

Según [SM-VN-AG2000]_ :

    (...) se reconoce al equilibrio como una condición estática 
    donde, con el tiempo, no ocurre cambio alguno en las propiedades 
    macroscópicas de un sistema, lo cual implica un balance de todos los 
    potenciales que pueden ocasionar un cambio. 

Por ejemplo, un sistema aislado que consta de las fases en contacto estrecho 
líquido y vapor, con el tiempo alcanza un estado final donde no existe 
tendencia a que suceda un cambio en sí mismo. La temperatura, la presión y 
las composiciones de fase logran los valores finales que en adelante 
permanecen fijos, por lo que el sistema logra el equilibrio [#]_ . 

Ecuaciones de Estado 
====================
El modelado cuantitativo de los equilibrios de fases se realiza principalmente 
utilizando **ecuaciones de estado** (:abbr:`EoS (Equation of State)`). Estas son relaciones 
matemáticas (modelos matemáticos) entre dos o más funciones de 
estado asociadas a la materia como la temperatura, la presión, el volumen o 
la energía interna. 

Como ejemplo conocido en cualquier curso introductorio de química, 
la Ley del gas ideal :eq:`gasideal` es una ecuación de estado, que al  
considerar el volumen molecular nulo y a las fuerzas de atracción-repulsión 
despreciables, limita su utilidad para modelar gases reales. 

 .. math:: pV=nRT
    :label: gasideal

:math:`p` es la presión absoluta, :math:`V` el volumen, :math:`T` la temperatura, 
:math:`n` la cantidad de materia y :math:`R` la constante del gas ideal.

La  Ecuación de Van der Waals :eq:`vdw` (1873) [#]_ generaliza la ecuación :eq:`gasideal`, teniendo en consideración tanto el volumen finito de las moléculas de gas como la atracción intermolecular que afectan al término de presiones

.. math:: 
   :label: vdw

    \left(P + \frac{a}{\upsilon^2}\right)\left(\upsilon-b\right) = RT


:math:`a` y :math:`b` son constantes físicas de la sustancia en cuestión. 

Muchas de las **ecuaciones de estado modernas** son mejoras y correcciones 
a la ecuación original de Van der Waals (denominadas ecuaciones de estado 
cúbicas). Por ejemplo la ecuación de Soave-Redlich-Kwong (1972), Peng-Robinson (1976), 
Elliott-Suresh-Donohue (1990), etc. 

GPEC es capaz de realizar los cálculos usando cinco diferentes ecuaciones de 
estado (ver :ref:'Requerimientos funcionales').

.. _aplicacion:

Aplicación y utilidad
======================

Los equilibrios entre fases tienen un rol muy importante en la tecnología química, 
alcanzando una gran diversidad de aplicaciones, principalmente en procesos de
separación de la industria química, petroquímica y el sector
de hidrocarburos, pero también en novedosos procesos basados en fluídos 
supercríticos, de gran desarrollo y creciente interés en las últimas 
décadas, como la generación de co-cristales, la producción de biodiesel, 
secado supercrítico, cromatografía supercrítica, etc. [#]_. Especialmente a altas presiones
estos equilibrios ser complejos de calcular e interpretar, por lo que la representación
a traves de diagramas de fases es esencial.

Como ejemplificación del interés de la industria y la academia sobre esta 
área de investigación, vale mencionar la experiencia del curso *Advanced 
Course on Thermodynamic Models*  , dictada por los profesores Michael Michelsen 
y Jørgen Mollerup de la Universidad Técnica de Dinamarca, que 
ha convocado a centenares de profesionales de diversas firmas como British 
Petroleum, Chevron, Phillips, Shell y muchas otras de renombre mundial. 

Este curso se realizó durante 2009 por primera vez en Latinoamérica, teniendo 
sede en la Universidad Nacional de Córdoba, organizado desde IDTQ, 
con participantes de Brasil, Canadá, Chile, Alemania y varias otras procedencias [#]_. 

.. [#]  A pesar de eso, en el nivel microscópico las condiciones no son estáticas. 
        Las moléculas contenidas en una fase en un determinado instante son 
        diferentes a las que después ocuparan la misma fase, es decir, existe 
        intercambio de de moléculas en la zona interfacial, aunque al ser de 
        igual rapidez promedio en ambas direcciones no ocurre transferencia 
        neta de material. 

.. [#]  Por este descubrimiento, Van der Waals recibió el Premio Nobel de Química 
        en 1910.

.. [#]  Para un listado más abarcativo, ver `Supercritical fluid: 
        Applications <http://en.wikipedia.org/wiki/Supercritical_fluid#Applications>`_
        
.. [#]  Ver http://www.course.efn.uncor.edu/

