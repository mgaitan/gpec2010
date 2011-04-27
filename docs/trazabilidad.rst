*****************************
Documentación de trazabilidad
*****************************

Este apéndice es la referencia de implementación de los requerimientos y 
las definiciones formales.


Implementación de los requerimientos
====================================

 +---------------+------------------------------------------------------------+
 | Requerimiento | Entidad de implementación (módulo / clase / método)        |
 +===============+============================================================+
 |    1          | :class:`apimanager.ApiManager`. Ver :ref:`api`             |
 +---------------+------------------------------------------------------------+
 |    2          | :class:`crud.DefineSystemDialog` y                         |     
 |               | :class:`crud.SystemValidator`                              |
 +---------------+------------------------------------------------------------+
 |    3          | :class:`crud.DefineSystemDialog`                           |               
 +---------------+------------------------------------------------------------+
 |    4          | :class:`panels.VarsAndParamPanel` y                        |  
 |               | :class:`panels.CasePanel`                                  |
 +---------------+------------------------------------------------------------+
 |    5          | :class:`plots.BasePlot`, :class:`plots.Plot2D`             |  
 +---------------+------------------------------------------------------------+
 |    5.1        | :class:`plots.PT`, :class:`plots.Tx`,                      |
 |               | :class:`plots.Trho`, :class:`plots.Px`,                    |
 |               | :class:`plots.Prho`                                        |
 +---------------+------------------------------------------------------------+
 |    5.2        | :class:`plots.IsoPT`, :class:`plots.IsoTx`,                |
 |               | :class:`plots.IsoTrho`, :class:`plots.IsoPx`,              |
 |               | :class:`plots.IsoPrho`                                     |
 +---------------+------------------------------------------------------------+
 |    5.3        | :class:`plots.Pxy`, :class:`plots.PxyPrho`                 |
 +---------------+------------------------------------------------------------+  
 |    5.4        | :class:`plots.Txy`, :class:`plots.TxyTrho`                 |
 +---------------+------------------------------------------------------------+
 |    6          | :class:`plots.BasePlot`, :class:`plots.Plot3D`             |  
 +---------------+------------------------------------------------------------+
 |    6.1        | :class:`plots.PTx`                                         |
 +---------------+------------------------------------------------------------+  
 |    6.2        | :class:`plots.PTrho`                                       |
 +---------------+------------------------------------------------------------+
 |    7          | :class:`plots.CustomPlot`, :class:`plots.PlotsTreePanel`,  |
 |               | :meth:`planels.SuitePlotPanel.MakeCustomPlot`              |
 +---------------+------------------------------------------------------------+
 |    8          | :class:`plots.SuitePlotsPanel`                             |  
 +---------------+------------------------------------------------------------+
 |    9          | :meth:`aui.MainFrame.FileSaveAs`,                          |
 |               | :meth:`aui.MainFrame.FileSave`,                            |  
 |               | :meth:`aui.MainFrame.Open`                                 |  
 +---------------+------------------------------------------------------------+
 |  10           | Ver :ref:`implantacion`                                    |
 +---------------+------------------------------------------------------------+
 |  11           | Función implementada en Matplolib, accesible mediante      |  
 |               |  `NavigationToolbar2Wx` mediante :class:`panels.PlotPanel` |
 +---------------+------------------------------------------------------------+

Definiciones 
============


.. automodule::  crud
   :members: DefineSystemDialog, SystemValidator

.. autoclass:: plots.BasePlot
   :members:
   :inherited-members:
   :undoc-members: 

.. automodule:: panels
   :members:  VarsAndParamPanel, CasePanel, PlotPanel, PlotsTreePane

.. autoclass:: aui.MainFrame
   :members:
   :undoc-members: 
    
