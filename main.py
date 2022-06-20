"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 2.                                                                                     -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author:                                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository:                                                                                         -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import functions
import visualizations

def data(crypto : "Nombre de la criptodivisa", n : "Número de datos a leer"):
    """
    data se encarga de la carga de datos.
    
    """
    
    return functions.downloadData(crypto, n)

def dataVisual(data):
    """
    dataVisual retorna un gráfico interactivo.
    
    """
    
    return visualizations.dataVisualization(data)

def RollModel(data : "Información de la criptodivisa"):
    """
    RollModel obtiene un spread teórico con el modelo teórico de Roll.
    
    """
    
    return functions.RollSpread(data)

def RollVisual(data):
    """
    RollVisual retorna un gráfico interactivo.
    
    """
    
    return visualizations.RollVisualization(data)

