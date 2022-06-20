"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab 2.                                                                                     -- #
# -- script: visualizations.py : python script with the data visualization functions                     -- #
# -- author:                                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository:                                                                                         -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def dataVisualization(data : "Información de la criptodivisa"):
    """
    dataVisualization retorna un gráfico interactivo para el Bid-Ask & Close de la criptodivisa en cuestión.
    
    """
    
    plot = make_subplots(specs = [[{"secondary_y" : False}]])
    plot.add_trace(go.Scatter(x = data.index, y = data["Bid"], name = "Bid"), secondary_y = False,)
    plot.add_trace(go.Scatter(x = data.index, y = data["Ask"], name = "Ask"), secondary_y = False,)
    plot.add_trace(go.Scatter(x = data.index, y = data["Close"], name = "Close"), secondary_y = False,)
    
    plot.update_layout(title = "Bid-Ask & Close",  xaxis_title = "Date")
    
    return plot

def RollVisualization(data : "Modelo de Roll"):
    """
    RollVisualization retorna un gráfico interactivo para el Spread y el Effective Spread calculado con el modelo de Roll.
    
    """
    
    plot = make_subplots(specs = [[{"secondary_y" : False}]])
    plot.add_trace(go.Scatter(x = data.index, y = data["Spread"], name = "Spread"), secondary_y = False,)
    plot.add_trace(go.Scatter(x = data.index, y = data["Roll Spread"], name = "Roll Spread"), secondary_y = False,)
    
    plot.update_layout(title = "Spread & Roll Spread",  xaxis_title = "Date")
    
    return plot
