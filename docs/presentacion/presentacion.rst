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


   - Software GPEC (2005): tésis doctoral del Dr. Cismondi
        

        *Un software para la obtención de curvas
        de **equilibro termodinámico de fase global para sistemas binarios**, 
        que se calculan mediante ecuaciones de estado.*
   

   - Situación: 

        - *Backend* (métodos númericos) (Fortran) 
        - *Frontend* (UI + graficación) (Visual Basic)
        - Comunicación mediante archivos



Motivación
**********

- Software muy utilizado en el ambiente científico-académico

- No se conoce otro software con prestaciones equivalentes

- Gran utilidad en la industria

- Pero... 

    - Interfaz compleja
    - No se basa en bibliotecas
    - Lenguaje obsoleto
    - Sólo funciona en Windows
    - Sólo gráficos 2D. 

Objetivos
*********

   - **Alcance**

        Rediseño e implementación de una nueva aplicación de 
        generación de gráficos para GPEC reutilizando el backend preexistente

   - Se buscó

        - Reimplementar el frontend sin afectar el backend. ("caja negra")
            - Implica respetar la interfaz de comunicación 

        - Equiparar y mejorar las funcionalidades 
        - Multiplataforma
        - Mejorar la usabilidad


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




.. 
    Contexto de trabajo
    ********************

    - Trabajo interdisciplinario 

        .. epigraph::

            La computación no trata sobre las computadoras más de 
            lo que la astronomía trata sobre los telescopios

            -- Edsger Dijkstra

    - Basado en software libre

    - Software Libre

Relevamiento de la versión preexistente
****************************************

.. figure:: ../images/visual_gpec1.png
   :width: 80%
   :align: center 

- Interfaz confusa: Demasiadas opciones simultáneas

- Gráficos: 
    - rutinas adhoc
    - rasterización de pixels. 
    - no se pueden exportar

- Diseño de base de datos (*Ms Jet*) innecesariamente complejo 


Metodología
**************
                            
- Marco conceptual: Agile Manifiesto

     - Individuos e interacciones sobre procesos y herramientas
     - Software funcionando sobre documentación extensiva
     - Colaboración con el comitente sobre negociación contractual
     - Respuesta ante el cambio sobre seguimiento (estricto) de un plan
    
- Desarrollo evolutivo

    .. image:: ../images/desarrollo_evolutivo.png
       :align: center 
       :width: 70% 

Tecnologías empleadas
*********************

- Lenguaje: Python
    

    .. epigraph::
        
        El canónico *"Python es un gran primer lenguaje"* suscitó 
        *"¡Python es un gran último lenguaje!"*

        -- Noah Spurrier

    - Simple, potente y elegante 
    - Multiplataforma
    - Contaba con experiencia 
    
- Graficación: Matplotlib

    - Graficos de alta calidad 2D y 3D
    - Integración con toolkits gráficos
    - Exportación a multiples formatos (mapa de bits y vectoriales)
    - Desarrollo muy activo 

- GUI: WxPython
    
    - Uso nativo de las APIs gráficas en cada entorno
    - *Advanced User Interface*

Arquitectura
**************

- Modelo conceptual

    .. figure:: images/workflow.png
       :width: 70%

Componentes
***********

.. figure:: ../images/arquitectura.png
   :align: center 
   :width: 70%


Patrón de comunicación
**********************

- Publisher/Subscriber

    
    .. image:: ../images/pubsub_concept.png
       :width: 60%
       :align: center 

   - Aplicación modular desacoplada
   - Implementación simple
   - Permite la extensibilidad  
    

API
****

.. figure:: ../images/parser.png
   :width: 30%

   Topología de la información extractada

- Ausencia de documentación 

    - Arduo trabajo ingeniería inversa

- Implementada como una clase independiente 
    
    - Permite reutilizar el backend en otro contexto (¿web?)

- Usa wine sobre plataformas no windows :(

    - Pero es mejorable: compilar nativamente,  f2py, etc. 


Implementacion
**************

- VIDEO


Verificacion
*************

- Pruebas unitarias (test automáticos)

    - Principalmente sobre la API::

    [...]
    test_write_conparin_2 (__main__.TestApiManager) ... ok
    test_write_conparin_3 (__main__.TestApiManager) ... ok
    test_write_gpecin (__main__.TestApiManager) ... ok

    ----------------------------------------------------------------------
    Ran 26 tests in 2.808s

    OK


- Usabilidad
    
    - Pruebas con usuarios
    - Análisis cuantitativo 
    

Implantacion
*************

- En windows

    - py2exe: genera un directorio *stand-alone* 
    - NSIS: genera un instalador

- En linux:

    - setuptools



Conclusiones
************

- Objetivos satisfechos: 
- Gráficos 3D: característica sobresaliente
- Se mejoró de usabilidad

- Impacto: 

    - Se utiliza para práctica en Termodinámica (UNC)
    - Poster en RITEQ
    - Grandes posibilidades comerciales 

Muchas gracias
**************

 
 - A mi familia y a Nati. 
 - a todos los que de una u otra manera me ayudaron a llegar hasta aquí

 Y especialmente 

    - Al pueblo argentino, por la universidad pública que le pertenece. 
    

