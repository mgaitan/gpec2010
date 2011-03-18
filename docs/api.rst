.. _api:

Especificación de la interfaz de comunicación
*********************************************

Esta documentación especifica la interfaz de archivos de entrada y salida
para el conjunto de programas de cálculo que componen *GPEC*. 
Se ha realizado a través de un proceso de *ingeniería inversa*, 
ya que se carecía de documentación fehaciente. 


Tabla de incidencia
====================

 ==========================================  ============  ================
 Entrada                                     Ejecutable    Salida
 ==========================================  ============  ================  
 CONPARIN.DAT                                ModelsParam   CONPAROUT.DAT
 CONPARIN.DAT                                PCSAFT        CONPAROUT.DAT
 GPECIN.DAT                                  GPEC          GPECOUT.DAT
 GPECIN.DAT + GPECOUT.DAT + TFORPXY.dat      PxyGPEC       PXYOUT.DAT
 GPECIN.DAT + GPECOUT.DAT + PFORTXY.dat      TxyGPEC       TXYOUT.DAT
 GPECIN.DAT + GPECOUT.DAT + ZforIsop.dat     IsoplethGPEC  ISOPOUT.DAT
 GPECIN.DAT + FUGIN.DAT                      FUGi          FUGOUT.DAT
 GPECIN.DAT + IsoXTin.DAT                    IsoXT         IsoXTout.DAT
 twophin.DAT2                                PhPxy         PXYOUT.DAT
 twophin.DAT2                                PhTxy         TXYOUT.DAT
 ==========================================  ============  ================

CONPARIN.DAT
------------

Es el archivo de entrada para el cálculo de parámetros específicos para los 
modelos en función de las constantes de cada compuesto, o bien, en sentido contrario, 
ajustar las constantes en función de parámetros del modelo definido por el usuario. 
Esta bidireccionalidad del cálculo se especifica mediante el parametro ``SENTIDO``.

 .. note:: el archivo se encuentra en realidad en `./INOUTS/CONPARIN.DAT`
        

Formato General:


    SENTIDO MODELO
    PARAM1    PARAM2    PARAM3    [PARAM4]   



:SENTIDO:

 ===  =============================================
 ID   Descripción
 ===  =============================================
 0    Calcula parámetros específicos del modelo en 
      función de las constantes del compuesto
 1    Calcula constantes del compuesto en función 
      de los parámetros del modelo
 ===  =============================================

:MODELO: 

 .. _`ID de Modelos`:

 ==  ====================
 ID  Modelo
 ==  ====================
 1   Soave-Redlich-Kwong
 2   Peng-Robinson
 3   RK-PR
 4   PC-SAFT
 6   SPHCT
 -   GC
 ==  ====================


Modo para calcular parámetros del modelo
-----------------------------------------

Este modo se define con ``SENTIDO`` 0. Se definen las variables del compuesto. 

    
  Modelos 1, 2, 3:

    0 MODELO
     TC    PC    OM     VC

  Para los modelos 4 y 6 el formato es el siguiente::

    0  MODELO
     TC    PC    OM


.. attention::
   El ejecutable a invocar para el cálculo en los modelos 4 o 6 es ``PCSAFT``


Detalle:

 ==========  ===================  ======== 
 Parámetro   Descripción          Unidad   
 ==========  ===================  ======== 
 TCeos       Temperatura          K        
 PCeos       Presión              Bar      
 VCeos       Volumen              l/mol    
 OM          Factor acentrico     --
 ==========  ===================  ========


Todos los parámetros son editables en el formulario excepto ``VCeos``. Para 
RK-PR el valor sí es editable y está asociado a un factor denominado  
``Critical Volume Ratio Model/Experimental`` o ``VCrat`` que se fija por omisión a 1.168. 

.. math::

   VCeos = VCmodel*VCrat

Para el modelo ``RK-PR`` se permite editar esta proporción. 
Si el usuario define ``VCeos``, se actualiza el ``VCrat`` y viceversa.


Modo para calcular variables del compuesto
------------------------------------------

Cuando ``SENTIDO`` es 1 el formato depende del modelo
    
    
    - 1  _`Soave-Redlich-Kwong`
    
        
        1   1   
        ac    b    m


      Detalle:

      ==========  ===================  ============
      Parámetro   Descripción          Unidad
      ==========  ===================  ============
      ac          --                   bar·m^6·kmol^2
      b           --                   l/mol
      m           --                   --
      ==========  ===================  ============


    - 2  Peng-Robinson
      
      Idem `Soave-Redlich-Kwong`_
    
    - 3  RK-PR
    
      ::

        1   3   
         ac    b    del1    k

      Detalle:

      ==========  ===================  ============
      Parámetro   Descripción          Unidad
      ==========  ===================  ============
      ac          --                   bar·m^6·kmol^2
      b           --                   l/mol
      del1        --                   --
      k           --                   --
      ==========  ===================  ============

    - 4   PC-SAFT

      ::

        1   4   
        eps/k   ro    m

      Detalle:

      ==========  ===================  ============
      Parámetro   Descripción          Unidad
      ==========  ===================  ============
      eps/k       --                   K
      ro          --                   Å
      m           --                   --
      ==========  ===================  ============


    -  5   GC

       .. todo::

            No aplica


    -  6   SPHCT
       ::
        
        1   6   
        T*   V*   c


CONPAROUT.DAT
=============

Es el archivo de salida para el cálculo de parámetros y constantes. 
El formato es el mismo independientemente del sentido de cálculo, teniendo la 
primer línea las variables de estado del compuesto, y en la segunda, los 
parámetros propios del modelo. 


Formato General:

    VAR1  VAR2   VAR3    VAR4
    PARM1 PARAM2 PARAM3  [...]

Detalle:

- Para `Soave-Redlich-Kwong`_ (id 1) y  ``Peng-Robinson`` (id 2)::

   TC    PC    VC    OM
   ac     b     m


- Para  ``RK-PR`` (id 3)::

   TC    PC     VC    OM
   ac     b   del1     k

- Para  ``PC-SAFT`` (id 4)::

   TC    PC     VC    OM
   eps/k   ro    m 

- Para  ``SPHCT`` (id 6):

    TC    PC     VC    OM
    T*   V*   c
  
        


GPECIN.DAT
==========

Se trata del archivo de entrada de parámetros para el cálculo del diagrama global. 

Formato General::

    MODELO
    NCOMB NTDEP
    NOMBRE_COMP1
    CONST1    CONST2    CONST3    [...]
    PARAM1    PARAM2    PARAM3    [...]
    NOMBRE_COMP2
    CONST1    CONST2    CONST3    [...]
    PARAM1    PARAM2    PARAM3    [...]
    K12
    L12
    MAX_P

Ejemplo::

    1
    0 0
    METHANE
    190.56  45.99  0.0115  0.114837
    2.33338  0.029849  0.498078
    ETHANOL
    514  61.37  0.6436  0.232124
    12.722  0.060334  1.420538
    0.1000
    0.0000
    2000

:MODELO: `ID de Modelos`_      
:NCOMB: Regla de combinación

 ==  ====================
 ID  Descripción
 ==  ====================
 0   van Der Waals
 1   Lorentz-Berthelot
 ==  ====================

 No todos los modelos pueden usar cualquier regla de combinación. En particular, 
  ``PC-SAFT`` y ``SPHCT`` exigen que la regla sea ``Lorentz-Berthelot``.

:NTDEP: dependencia con T para los parámetros de interacción, on/off

  ..todo::
    ver qué corno es esto. 


:NOMBRE_COMP: Nombre del compuesto. Se puede ignorar. 

:CONST: Constantes del compuesto. 
        Para los modelos_ 1, 2 y 6 los parámetros son los siguientes::

    
            TC    PC    OM    VC


        Para el modelo 4 se agrega un parámetro más:: 

            TC    PC    OM    VC    VCrat

    
        Detalle:

        ==========  ===================  ============
        Parámetro   Descripción          Unidad
        ==========  ===================  ============
        TC          Temperatura          K
        PC          Presión              Bar
        OM          --                   --
        VC          Volumen              l/mol
        VCrat       Volumen              l/mol 
        ==========  ===================  ============
    
.. _modelos: `ID de Modelos`_

:PARAM: Los parámetros específicos previamente calculados en función del modelo elegido.
        Ver CONPAROUT.DAT

        - Para los modelos 1 o 2 los parámetros tienen el siguiente formato::
        
            ac    b    m
    
          Detalle:

          ==========  ===================  ===============
          Parámetro   Descripción          Unidad
          ==========  ===================  ===============
          ac          --                   bar·m^6·kmol^2
          b           --                   l/mol
          m           --                   --
          ==========  ===================  ===============


        - Para el modelo  3  (RK-PR)::
            
             ac    b    del1    k

          Detalle:

          ==========  ===================  ===============
          Parámetro   Descripción          Unidad
          ==========  ===================  ===============
          ac          --                   bar·m^6·kmol^2
          b           --                   l/mol
          del1        --                   --
          k           --                   --
          ==========  ===================  ===============

        - Para  el modelo 4  (PC-SAFT)::

            eps/k   ro    m

          Detalle:

          ==========  ===================  ============
          Parámetro   Descripción          Unidad
          ==========  ===================  ============
          eps/k       --                   K
          ro          --                   Å
          m           --                   --
          ==========  ===================  ============


        - Para  el modelo 5 (GC):

          .. todo:: aplica ?


        - Para  el modelo 6 (SPHCT) ::

                T*    V*    c    s    q

          Detalle:


          ==========  ===================  ============
          Parámetro   Descripción          Unidad
          ==========  ===================  ============
          T*          Temperatura          K    
          V*          Volumen              .
          ==========  ===================  ============

        .. todo:: 
            falta descripción de parametros ``c``, ``s`` y ``q``


:K12: Parámetro de interacción binario

    .. todo:: 
        ver

:L12: Parámetro de interacción binario

    .. todo:: 
        ver

:MAX_P: Máxima presión para líquidos. Se especifica en ``bar``. 


GPECOUT.DAT
===========

Es el archivo de salida de ``GPEC``. Tiene una cabecera, donde especifica
a fines descriptivos los parámetros que se utilizaron para realizar el cálculo, 
y diversas tablas de valores tabulados, cada una de las cuales representan 
una *curva* en el espacio n-dimensional. Tomando 2 de estas columnas de valores
se obtienen las distintas curvas a graficar. 

Cabecera
--------

Para el analisis sintáctico, se puede ignorar la cabecera del archivo. 
Sin embargo, para los fines descriptivos se incluye un ejemplo::

    METHANE   
    Tc= 190.5600   Pc =  45.9900   Vc =  0.0986   OM = 0.0115
    Zc=   0.2863 Zcrat=   1.1680 Zceos=  0.3344 Vceos= 0.1152
    ac=   2.3270    b =   0.0300  del1=  0.9244    k = 1.5086
    ETHANOL   
    Tc= 514.0000   Pc =  61.3700   Vc =  0.1680   OM = 0.6436
    Zc=   0.2412 Zcrat=   1.1680 Zceos=  0.2817 Vceos= 0.1962
    ac=  14.5350    b =   0.0482  del1=  3.8196    k = 3.1328
     
     Tc, Pc and Vc are given in K, bar and L/mol respectively
     
      K12 =   0.000000000000000E+000
     
       LIJ MATRIX
    METHANE   
    ETHANOL    0.00000
     
      Combining rules:
      0: Classical or van der Waals 

Esta cabecera puede cambiar ligeramente en función del modelo con el que se 
calculó. 

Datos tabulados
---------------

La estructura general de una tabla de datos tabulados tiene la siguiente 
estructura::

   Var1(Un)    Var2(Un)    Var3(Un)    [...]
 TIPO
 dato1.1       dato1.2     dato1.3     [...]    ?   ?   
 dato2.1       dato2.2     dato3.3     [...]    ?   ?   
 ...

 [Comment]


:Var(Un): Describe explicitamente la variable/constante que representa esa columna. 
          Entra paréntesis especifica la unidad de medida. 

:TIPO: 
    
 .. _`Tabla de tipos`:

 =====  ===============================  =======================
 Tipo   Descripción                      Columnas significativas
 =====  ===============================  =======================
 VAP    Vapor                            4                   
 CRI    Curva crítica                    5
 CEP    Critical End Point               6
 LLV    Liquido liquido vapor            10
 =====  ===============================  =======================

 .. todo:: 
    ver descripción. Ver AZE line  ¿Estructura?. 
    



 Las columnas significativas son las que deben *leerse* ya que aportan datos 
 necesarios para la graficación. Las columnas restantes representan detalles 
 del cálculo interno (cantidad de iteraciones, precisión) pero serán ignoradas
 para los fines de graficación. 

 El significado de las las columnas para cada tipo puede verse aqui: 

 =====  ===================================================================================
 Tipo   Columnas
 =====  ===================================================================================
 VAP    ``T(K)    Pv(bar)    rhoL     rhoV``
 CRI    ``T(K)     P(bar)   d(mol/L)   x(1)     1-x(1)``
 CEP    ``T(K)     P(bar)    X(1)     XL1(1)   dc(mol/L)  dL(mol/L)``
 LLV    ``T(K)    P(bar)    XL1    XL2    Y(1)    Y(2)    X2L2    d1(mol/L)    d2(mol/L)    dV(mol/L)``
 =====  ===================================================================================
 
 .. todo:: 
    ver detalle de significación de las columnas. Ver LLV ¿10 col significativas?


Las tablas de datos tabulados pueden tener cualquier extensión y terminan
únicamente por una línea en blanco. 

También pueden existir comentarios luego de la finalización de una tabla tabulada. 
Por ejemplo::
    

     ...
     166.399 0.1241E-007  19.8163 0.8967E-009   1   3
     165.074 0.9122E-008  19.8275 0.6646E-009   1   3
     164.020 0.7117E-008  19.8364 0.5219E-009   1   3
     
      Predicted type of phase behaviour is indicated at the end of this file
     



Pie
---

Al igual que la cabecera, el final del archivo aporta información extra.
Por ejemplo::


  Type of phase behaviour predicted by the model for this system
           3
 
  Total number of Azeotropic End Points found:
           0
 
  Pure Azeotropic End Points found:                    0
 
  Critical Azeotropic End Points found:                0
 
  Heterogeneous Azeotropic End Points found:            0


TFORPXY.dat
===========

``TFORPXY.dat`` es el tercer archivo de entrada que utiliza PxyGPEC para calcular
diagramas Presión-Composición a una temperatura constante dada. 

Este archivo simplemente define el valor de temperatura que el usuario puede ingresar, 
previo al cálculo::

    TEMPERATURA

 :TEMPERATURA: Valor de temperatura en ºK definido por el usuario, dentro del rango 
               de valores aceptados por el sistema. 

               El rango aceptado lo define el máximo y el mínimo de temperatura
               encontrado en los bloques de datos tabulados LLV. 

PXYOUT.DAT
==========

Es el archivo de salida para el diagrama Presión-Composición (diagrama isotermico). 
Tiene una estructura de `datos tabulados`_ como sigue::


 T = TEMPERATURA K
 
    P       X(1)     Y(1)     Y(2)           X(2)    dX(mol/L) dY(mol/L) [...]
 Pxy
 p.1       x1.1      y1.1     y2.1           x2.1    dX.1      dY.1      [...]
 p.2       x1.2      y1.2     y2.2           x2.2    dX.2      dY.2      [...]
 (...)
 p.n       x1.n      y1.n     y2.n           x2.n    dX.n      dY.n      [...]
 

Tiene 7 columnas significativas. 
   

PFORTXY.DAT
===========

Análogo a TFORPXY.dat_ para el diagrama de presión constante, este archivo 
indica el valor de presión definida por el usuario. 

    PRESION

 :PRESION: Valor de presión en Bar definido por el usuario, dentro del rango 
               de valores aceptados por el sistema.

               .. todo:: 
                      cual es el rango ?
                
TXYOUT.DAT
==========

Datos tabulados de salida para diagramas isobáricos. Tiene 
la misma estructura que PXYOUT.DAT_ pero el parámetro constante es la temperatura
y la primer columna de datos tabulados es presión::


 P = PRESION bar
 
    T       X(1)     Y(1)     Y(2)           X(2)    dX(mol/L) dY(mol/L) [...]
 Txy
 t.1       x1.1      y1.1     y2.1           x2.1    dX.1      dY.1      [...]
 t.2       x1.2      y1.2     y2.2           x2.2    dX.2      dY.2      [...]
 (...)
 t.n       x1.n      y1.n     y2.n           x2.n    dX.n      dY.n      [...]


Tiene 7 columnas significativas. 

ZforIsop.dat
============

Es un archivo de entrada para ``IsoplethGPEC`` que realiza los cómputos 
para obtener un set de datos para una proporción del *compuesto 1* constante, 
que define el usuario.  

.. note::

    ``IsoplethGPEC`` requiere, además de este archivo, que ``GPECIN.DAT`` y 
    ``GPECOUT.DAT`` hayan sido generados. 


Es similar a `PFORTXY.DAT`_ y `TFORPXY.dat`_ pero define un parámetro ``z``
adimensional que representa la fracción de compuesto:: 

    Z

 :Z: Fracción de compuesto 1 definida por el usuario. 

   .. todo:: 
          cual es el rango ( 0 a 1 ? )

ISOPOUT.DAT
===========

Archivo de salida para isopletas (Presión-Temperatura en composición constante). 
Tiene la siguiente estructura::


 NCRI=           N_L_CRITICAS
 CRI
     T          P(bar)
 tcri1.1        pcri1.1  
 
 (...)
     
   z1 = y1 = Z
 
     T      P(bar)    X(1)     X(2)    dX(mol/L)   dY(mol/L) NITER
 ISO
 t.1       p.1      x1.1      x2.1      dX.1        dY.1      [...]
 t.2       p.2      x1.2      x2.2      dX.1        dY.1      [...]
 (...)
 t.n       p.n      x1.n      x2.n      dX.n        dY.n      [...]
 
     T          P(bar)
 LLV
 t_llv.1     p_llv.1
 t_llv.2     p_llv.2
 (...)
 t_llv.n     p_llv.n

Detalle:

 :N_L_CRITICAS: Indica el número de líneas/puntos críticos, o lo que es lo mismo
                la cantidad de bloque ``CRI`` que se esperan. 

 :Z: es el valor adimensional que indica la proporción del compuesto 1 en el sistema. 

El bloque de datos tabulados ``ISO`` tiene 6 cifras significativas. 


FUGIN.DAT                      
=========

Archivo de entrada para ``FUGi`` que se utiliza para realizar un diagrama
*Fugacidad-Composición* para una temperatura y una presión dadas. 
La estructura del archivo es la siguiente::

    TEMPERATURA PRESION PASO_COMP
    X1_min  X1_max

Detalle: 

 :TEMPERATURA: Temperatura en *K* especificada por el usuario. 
 :PRESION: Presión en *bar* especificada por el usuario. 
 :PASO_COMP: Coeficiente de paso de composición. (determina la resolución)
 :X1_min: Mínimo del dominio (composición del compuesto 1)
 :X1_max: Máximo del dominio (composición del compuesto 1)


FUGOUT.DAT
==========

El archivo de salida de datos para *Fugacidad-Composición* producido por 
``FUGi``. Tiene una estructura similar a GPECOUT.DAT_ y en particular 
una cabecera_ y un bloque de `datos tabulados`_ que tiene la siguiente 
estructura::


   T(K)         P(bar) 
   TEMPERATURA  PRESION
 FUG
   x.min  f1(x.min)    f2(x.min)
   (...)
   x.n    f1(x.n)      f2(x.n)
   (...)
   x.max  f1(x.max)    f2(x.max)
    
    
Detalle:

 :TEMPERATURA: Temperatura en *K* especificada por el usuario. 
 :PRESION: Presión en *bar* especificada por el usuario.
 
  
Las tres columnas de datos son significativas.     
    


IsoXTin.DAT
===========

Archivo de entrada para ``IsoXT`` que se utiliza para realizar un diagrama
*Presión-densidad* para temperatura y composición constante. 
La estructura del archivo es la siguiente::

    TEMPERATURA PROPORCION
    RHO_min RHO_max PASO_DENS
    
Detalle: 

 :TEMPERATURA: Temperatura en *K* especificada por el usuario. 
 :PROPORCION: Proporción (entre 0 y 1, adimensional) del compuesto 1, especificada 
              por el usuario. 
 :Rho_min: Mínimo del dominio (densidad) en *mol/l*
 :Rho_min: Mínimo del dominio (densidad) en *mol/l*
 :PASO_DENS: Coeficiente de paso de densidad. (determina la resolución)


IsoXTout.DAT
============

Archivo de salida similar a FUGOUT.DAT_ con una cabecera_ con la siguiente
estructura::


    T (K)       x1          x2 
    TEMPERATURA PROPORCION  1-PROPORCION
 
    rho(mol/L)   P(bar) 
    rho.min     p(rho_min)
    (...)
    rho.n       p(rho_n)
    (...)
    rho.max     rho.max

Detalle:

 :TEMPERATURA: Temperatura en *K* especificada por el usuario. 
 :PROPORCION: Proporción (entre 0 y 1, adimensional) del compuesto 1
 
Notar que el bloque de datos no tiene un identificador de tres letras
previo a las columnas de datos. 



