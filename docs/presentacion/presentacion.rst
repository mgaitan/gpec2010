************************************************************
Proyecto Integrador de Ingeniería en Computación
************************************************************

.. image::  img/unc3-b.jpg
   :align: right
   :width: 40 % 

| *GPEC 2010*
|
| Martín Gaitán 
| 
| FCEFyN - UNC
| 12 de mayo de 2011
|
|


- Director: 

   * Mg. Gustavo Wolfmann

- Codirector: 

   * Dr. Martín Cismondi Duarte
 

Introducción
************

.. class:: incremental

   - Software GPEC (2005): tésis doctoral del Dr. Cismondi
        

        Un software para la obtención de curvas
        de equilibro termodinámico de fase global para sistemas binarios, 
        que se calculan mediante ecuaciones de estado.
   

   - Situación: 

        - *Backend* (métodos númericos) (Fortran) 
        - *Frontend* (UI + graficación) (Visual Basic)
        - Comunicación mediante archivos



Motivación
**********

.. class:: incremental

    - Actualmente

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


.. image:: ../images/Phase-diag_es.png
   :align: right 
   :width: 50%

- Diagrama de fase

    Gráfico utilizado para mostrar las condiciones en las que
    distintas fases termodinámicas pueden ocurrir en equilibrio.

   
.. image:: ../images/ejTipo1.png
      :align: right 
      :width: 50%
    
    
- En **Sistemas binarios**  (2 componentes)
   
    - La **composición** (y la **densidad**) se vuelven una variable => espacio 

Breve marco Teórico (cont.)
****************************

- La proyección ortogonal de estas curvas tridimensionales genera gráficos 2D 

    .. image:: ../images/ejemploTx.png
       :width: 50%
       :align: right 

- Modelo matemático: Ecuaciones de estado que relaciones funciones de estado 

    - Todo parte de las famosa *Ecuacíón de Van der Wals*

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
   :width: 60%
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
.. class:: incremental 

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

.. image:: ../images/workflow.png
   :width: 70%
   :align: center 

Componentes
***********

.. figure:: ../images/arquitectura.png
   :align: center 
   :width: 60%


Patrón de comunicación
**********************
   
.. figure:: ../images/pubsub_concept.png
   :width: 60%
   :align: center 

   Patrón Publisher/Subscriber

- Aplicación modular desacoplada
- Permite la extensibilidad  
- Implementación simple

.. code-block:: python 

    #suscribe
    pub.subscribe(self.OnAppendLog, 'log')  
    #envia
    pub.sendMessage('log', mensaje)


API
****

.. image:: ../images/parser.png
   :width: 50%
   :align: right 

.. class:: incremental

    - Escasa documentación del formato de los archivos

      - Arduo trabajo ingeniería inversa

    - Implementada como una clase independiente 
        
      - Permite reutilizar el backend en otro contexto (¿web?)

    - Usa wine sobre plataformas no Windows :(

      - Pero es mejorable: compilar nativamente,  *f2py*, etc. 


Implementacion
**************

- VIDEO


Verificacion
*************

- Pruebas unitarias (test automáticos)

    - Principalmente sobre la API

    .. code-block:: python

        [...]
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
    

