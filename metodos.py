import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class metodos:
    

    def prepararDatos():     
        data = pd.read_csv("datos.csv")
        data.dropna(axis = 0, how = "all", inplace = True) 
        data = data.astype(str)
        return data.to_dict(orient="records")

    def departamentos():
        data = pd.read_csv("datos.csv")
        data.dropna(axis = 0, how = "all", inplace = True) 
        datos_agrupados_departamento = data.groupby(["DEPARTAMENTO"]).mean().reset_index().copy()
        lista_departamentos = list(datos_agrupados_departamento["DEPARTAMENTO"].unique())
        return lista_departamentos


    def desercion_transicion():
        data = pd.read_csv("datos.csv")
        data.dropna(axis = 0, how = "all", inplace = True) 
        datos_agrupados_departamento_dt = data.groupby(["AÑO","DEPARTAMENTO"])['DESERCIÓN_TRANSICIÓN'].mean().reset_index().copy()
        datos_agrupados_departamento_dt = datos_agrupados_departamento_dt.astype(str)
        return datos_agrupados_departamento_dt.to_dict(orient="records")

    def desercion_primaria():
        data = pd.read_csv("datos.csv")
        data.dropna(axis = 0, how = "all", inplace = True) 
        datos_agrupados_departamento_dp = data.groupby(["AÑO","DEPARTAMENTO"])['DESERCIÓN_PRIMARIA'].mean().reset_index().copy()
        datos_agrupados_departamento_dp = datos_agrupados_departamento_dp.astype(str)        
        return datos_agrupados_departamento_dp.to_dict(orient="records")

    def desercion_secundaria():
        data = pd.read_csv("datos.csv")
        data.dropna(axis = 0, how = "all", inplace = True) 
        datos_agrupados_departamento_ds = data.groupby(["AÑO","DEPARTAMENTO"])['DESERCIÓN_SECUNDARIA'].mean().reset_index().copy()
        datos_agrupados_departamento_ds = datos_agrupados_departamento_ds.astype(str)       
        return datos_agrupados_departamento_ds.to_dict(orient="records")

    def desercion_media():
        data = pd.read_csv("datos.csv")
        # data.dropna(axis = 0, how = "all", inplace = True) 
        datos_agrupados_departamento_dm = data.groupby(["AÑO","DEPARTAMENTO"])['DESERCIÓN_MEDIA'].mean().reset_index().copy()
        datos_agrupados_departamento_dm = datos_agrupados_departamento_dm.astype(str)       
        return datos_agrupados_departamento_dm.to_dict(orient="records")

    
    