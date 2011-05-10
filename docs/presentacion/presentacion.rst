********************************************
Global Phase Equilibrium Calculations v.2010
********************************************

.. image::  ../unc3-b.jpg
   :align: right

| Proyecto Integrador de Ingeniería en Computación
| 
| Facultad de Ciencias Exáctas Físicas y Naturales
|
| Martín Gaitán 

Director: 

    Mg. Gustavo Wolfmann

Codirector: 

    Dr. Martín Cismondi Duarte
 

Introducción
************


   - **Objetivo**

        Actualización de un software preexistente: GPEC  (2005)
        
        *Software para la obtención de curvas
        de **equilibro termodinámico de fase global para sistemas binarios**, 
        que se calculan mediante ecuaciones de estado.*

        Arquitectura: *Backend* (cálculo) + *Frontend* (UI + graficación)

   - **Alcance**

        Rediseño e implementación de una nueva aplicación de 
        generación de gráficos para GPEC reutilizando el backend preexistente


Motivación
**********

- Software muy utilizado en el ambiente científico-académico

- No se conoce otro software con prestaciones equivalentes

- Pero... 

    - Interfaz compleja
    - No se basa en bibliotecas
    - Sólo funciona en Windows
    - Sólo gráficos 2D. 


Breve marco Teórico 
********************

- Diagrama de fase

    Gráfico utilizado para mostrar las condiciones en las que
    distintas fases termodinámicas pueden ocurrir en equilibrio.

    .. figure:: ../images/Phase-diag_es.png
       :align: right 
       :width: 50%

       Ejemplo: Diagrama PT para sustancias pura o composición constante (Agua)

- En **Sistemas binarios**  (2 componentes)

    .. figure:: ../images/ejTipo1.png
       :align: right 
       :width: 50%
    
       Diagrama PTx

    - La **composición** (y la **densidad**) se vuelven una variable => espacio 

Breve marco Teórico (cont.)
****************************

- La proyección ortogonal de estas curvas tridimensionales genera gráficos 2D 

    .. figure:: images/ejemploTx.png
       :width: 50%
       :align: right 

       Un diagrama T-x para un sistema binario, mostrando la línea crítica y 
       otras informaciones. 

- Modelo matemático: Ecuaciones de estado que relaciones funciones de estado 

- También se realizan "cortes" fijando una variable (isobaras, isotermas, isopletas)

- Distintos comportamientos segun los compuestos (todos calculables por GPEC


Versión precedente
******************




Análisis de la versión precedente
**************************

Tecnoclogias
**************

Arquitectura
**************

API
****

Implementacion
**************

Verificacion
*************

Implantacion
*************

Conclusiones
*************

