Diseño
****** 




Flujo de trabajo general
========================

Diagrama de actividades
-----------------------




Base de datos
=============

El almacenamiento y gestión de la información necesaria como entrada para GPEC se realiza
a través de un sistema de gestión de base de datos relacional. Se 
utilizó el software `Sqlite <http://sqlite.org>`_  (versión 3) que respeta casi íntegramente 
el estándar :abbr:`SQL (Structured Query Language)`  mediante una librería 
monolítica, portable, eficiente y compacta que es fácilmente interfaceable con Python [#]_. 

Una base de datos de *Sqlite* está autocontenida en un 
archivo binario que puede ser distribuído en conjunto con el software, sin 
requerir inicialización o un *servidor* de base de datos local o remoto. 

En particular, los datos almacenados son las constantes de compuestos 
químicos. Se incluye una vasta base de compuestos denominada :abbr:`DIPPR` cuya 
modificación está vedada a través de la interfaz de usuario (modo *sólo lectura* [#]_), 
así como *compuestos definidos por el usuario* que pueden ser agregados como 
una copia de un compuesto :abbr:`DIPPR` (que acepta, entonces, la modificación 
o ajuste de sus valores) o bien como un nuevo compuesto definido desde datos 
experimentales. 

.. todo:: 
        Siglas de dippr ? 


Modelo Entidad-Relación
-----------------------

.. todo:: 

    entidad-relacion

Definición de las tablas
-------------------------


.. code-block:: sql

    CREATE TABLE "compounds" ("id" INTEGER,"id_category" INTERGER PRIMARY KEY 
                                                      AUTOINCREMENT NOT NULL ,
                              "name" VARCHAR,
                              "formula" VARCHAR,
                              "formula_extended" VARCHAR,
                              "tc" FLOAT,
                              "pc" FLOAT,
                              "vc" FLOAT,
                              "acentric_factor" FLOAT,
                              "vc_rat" FLOAT DEFAULT (1.168) 
                             );

    CREATE TABLE "categories" ("id_category" INTEGER PRIMARY KEY  
                                             AUTOINCREMENT  NOT NULL, 
                               "name" VARCHAR, 
                               "editable" BOOL NOT NULL DEFAULT True
                              );
    INSERT INTO "categories" VALUES(1,'DIPPR','False');
    INSERT INTO "categories" VALUES(2,'User defined','True');


    


.. _frontend_backend:
    
Interacción Frontend / Backend
==============================
        

Metodología de relevamiento
----------------------------






.. _justificacion_diseno:

Justificación de diseño
------------------------



.. [#] De hecho, a partir de la versión 2.6 de Python, el modulo ``sqlite3`` forma 
       parte de la biblioteca estándar de Python. 

.. [#] Sqlite no permite definir tablas o registros de datos como *sólo lectura*. 
       Queda en potestad del desarrollador vedar la posilidad de modificación como parte    
       del proceso de validación. Sin embargo, siempre es posible para un usuario abrir
       y modificar la información "manualmente" a través de un gestor que interprete 
       el formato *sqlite*. 
        
        
