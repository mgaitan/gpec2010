Casos de uso
============

.. _`caso de uso 1`:

+---------------+-------------------------------------------+
| **Título:**   | Creación de un sistema binario            | 
+---------------+------------+---------------+--------------+
| **ID:**       |  1         | **Versión:**  | 1            |
+---------------+------------+---------------+--------------+
| **Descripción:**                                          |
|   Un sistema binario es la combinación de dos compuestos  |
|   químicos. Se deben poder seleccionar una combinación    |
|   cualquiera de 2 compuestos un listado o base de datos   |
|   de compuestos   disponibles.                            |
+-----------------------------------------------------------+
| **Actores:**                                              |
|   Usuario                                                 |
|   Motor de Base de datos                                  |
+-----------------------------------------------------------+
| **Precondiciones:**                                       |
|   * Deben existir al menos 2 compuestos en la base.       |
|   * No se puede seleccionar dos veces el mismo compuesto. |
+-----------------------------------------------------------+
| **Flujo normal:**                                         |
|    #. El usuario selecciona un primer compuesto de la     |
|       base (compuesto 1) y lo agrega al sistema.          |  
|    #. El usuario selecciona un segundo compuesto          |
|       (compuesto 2) y lo agrega al sistema.               |  
+-----------------------------------------------------------+
| **Flujo alternativo:**                                    |
|    * El usuario crea un nuevo compuesto y lo agrega a     |
|      la base. Ver `caso de uso 2`_.                       |
|    * El usuario modifica parámetros de un compuesto       |
|      antes de agregarlo al sistema. Ver `caso de uso      |
|      3`_ .                                                |
+-----------------------------------------------------------+
| **Postcondiciones:**                                      |
|   El sistema queda definido por dos compuestos distintos  |
+-----------------------------------------------------------+

.. _`caso de uso 2`:

+---------------+-------------------------------------------+
| **Título:**   | Creación de un nuevo compuesto (Alta)     | 
+---------------+------------+---------------+--------------+
| **ID:**       |  2         | **Versión:**  | 1            |
+---------------+------------+---------------+--------------+
| **Descripción:**                                          |
|   La base de datos de compuestos químicos debe ser        |
|   manipulable. Debe poder agregarse un compuesto a la     |
|   base de datos, presentando un formulario de             |
|   parametrización. Existen parámetros obligatorios y      |
|   otros opcionales.                                       |
|                                                           |
|   Los compuestos creados por el usuario quedan            |
|   debidamente identificados.                              |
+-----------------------------------------------------------+
| **Actores:**                                              |
|   Usuario                                                 |
|   Motor de Base de datos                                  |
+-----------------------------------------------------------+
| **Precondiciones:**                                       |
|   * El nombre asignado al nuevo compuesto no debe existir |
+-----------------------------------------------------------+
| **Flujo normal:**                                         |
|    1. El usuario acciona la creación de un nuevo          |
|       compuesto.                                          |
|    2. Define al menos los campos obligatorios, los        |
|       parámetros críticos  del componente puro:           |
|       temperatura crítica, presión crítica, factor        |
|       acentrico, volumen crítico.                         |
|    3. Se validan los parámetros ingresados. Si son        |
|       válidos, se almacena el nuevo compuesto en la base  |
|    4. El formulario se cierra y se sale.                  |
+-----------------------------------------------------------+
| **Flujo alternativo:**                                    |
|    * El usuario cancela la acción en cualquier momento    |
|    * Si los parámetros ingresados no son válidos, se      |
|      debe informar debidamente al usuario para que los    |
|      corrija.                                             |     
+-----------------------------------------------------------+
| **Postcondiciones:**                                      |
|   Un nuevo compuesto se agregó a la base de datos y puede |
|   utilizarse para la definición de un sistema binario     |
+-----------------------------------------------------------+

.. _`caso de uso 3`:

+---------------+-------------------------------------------+
| **Título:**   | Modificación de un compuesto              | 
+---------------+------------+---------------+--------------+
| **ID:**       |  3         | **Versión:**  | 1            |
+---------------+------------+---------------+--------------+
| **Descripción:**                                          |
|   Un compuesto definido en la base puede modificarse      |
|   reemplazando sus parámetros.                            |
|   Los cambios pueden salvarse sobre el mismo registro     |
|   o bien guardarlo como un nuevo registro de usuario      |
+-----------------------------------------------------------+
| **Actores:**                                              |
|   Usuario                                                 |
|   Base de datos                                           |
+-----------------------------------------------------------+
| **Precondiciones:**                                       |
|   Debe existir al menos un compuesto en la base de datos  |
+-----------------------------------------------------------+
| **Flujo normal:**                                         |
|    1. El usuario selecciona un compuesto a modificar      |
|    2. Modifica los parámetros.                            |
|    3. Si los nuevos parámetros son válidos se guarda el   |
|       el compuesto                                        |
+-----------------------------------------------------------+
| **Flujo alternativo:**                                    |
|   * El usuario puede cancelar la acción en cualquier      |
|     momento.                                              |
|   * Se puede guardar el compuesto modificado como un      |
|     nuevo registro sin afectar el registro original.      |
|     Ver `caso de uso 1`_.                                 |
+-----------------------------------------------------------+
| **Postcondiciones:**                                      |
|   Un compuesto previamente existente se ha modificado     |
|   o guardado como un nuevo compuestos                     |
+-----------------------------------------------------------+

.. _`caso de uso 4`:

+---------------+-------------------------------------------+
| **Título:**   | Eliminación de un compuesto de usuario    | 
+---------------+------------+---------------+--------------+
| **ID:**       |  4         | **Versión:**  | 1            |
+---------------+------------+---------------+--------------+
| **Descripción:**                                          |
|   Un compuesto previamente generado por el usuario        |
|   puede ser eliminado de la base de datos                 |
+-----------------------------------------------------------+
| **Actores:**                                              |
|   Usuario                                                 |
|   Base de datos                                           |
+-----------------------------------------------------------+
| **Precondiciones:**                                       |
|   Debe existir al menos un compuesto en la base           |
+-----------------------------------------------------------+
| **Flujo normal:**                                         |
|    1. El usuario selecciona un compuesto de la base       |
|    2. Ejecuta la acción Eliminar                          |
|    3. Se solicita confirmación al usuario y si acepta     |
|       se elimina el regitro de la base
+-----------------------------------------------------------+
| **Flujo alternativo:**                                    |
|   * El usuario puede cancelar la acción en cualquier      |
|     momento.                                              |
+-----------------------------------------------------------+
| **Postcondiciones:**                                      |
|   El componente se ha eliminado de la base de datos       |
+-----------------------------------------------------------+

.. _`caso de uso 5`:

+---------------+-------------------------------------------+
| **Título:**   | Cálculo de parámetros específicos del     | 
|               | modelo                                    |
+---------------+------------+---------------+--------------+
| **ID:**       |  5         | **Versión:**  | 1            |
+---------------+------------+---------------+--------------+
| **Descripción:**                                          |
|   Luego de seleccionar compuestos,                                                  |
+-----------------------------------------------------------+
| **Actores:**                                              |
|   Actor 1                                                 |
|   Actor 2                                                 |
+-----------------------------------------------------------+
| **Precondiciones:**                                       |
|   El usuario debe haberse logeado en el sistema.          |
+-----------------------------------------------------------+
| **Flujo normal:**                                         |
|    #. paso 1                                              |
|    #. paso 2                                              |
+-----------------------------------------------------------+
| **Flujo alternativo:**                                    |
|    #. paso 1                                              |
|    #. paso 2                                              |
+-----------------------------------------------------------+
| **Postcondiciones:**                                      |
|   El usuario debe haberse logeado en el sistema.          |
+-----------------------------------------------------------+






.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }


.. image:: http://yuml.me/diagram/scruffy/usecase/[Customer]-(Login), [Customer]-(note: Cust can be registered or not{bg:beige}).png
       

Template
++++++++

.. _`caso de uso `:

+---------------+-------------------------------------------+
| **Título:**   | Creación de un sistema binario            | 
+---------------+------------+---------------+--------------+
| **ID:**       |  1         | **Versión:**  | 1            |
+---------------+------------+---------------+--------------+
| **Descripción:**                                          |
|   text                                                    |
+-----------------------------------------------------------+
| **Actores:**                                              |
|   Actor 1                                                 |
|   Actor 2                                                 |
+-----------------------------------------------------------+
| **Precondiciones:**                                       |
|   El usuario debe haberse logeado en el sistema.          |
+-----------------------------------------------------------+
| **Flujo normal:**                                         |
|    #. paso 1                                              |
|    #. paso 2                                              |
+-----------------------------------------------------------+
| **Flujo alternativo:**                                    |
|    #. paso 1                                              |
|    #. paso 2                                              |
+-----------------------------------------------------------+
| **Postcondiciones:**                                      |
|   El usuario debe haberse logeado en el sistema.          |
+-----------------------------------------------------------+


