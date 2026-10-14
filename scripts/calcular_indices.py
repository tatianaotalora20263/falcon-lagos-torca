"""
Cálculo de índices espectrales Sentinel-2
Proyecto: análisis multitemporal de Lagos de Torca
Años: 2016 y 2026
Sistema de referencia: EPSG:9377
"""

import arcpy
from arcpy.sa import Raster, Con

arcpy.CheckOutExtension("Spatial")

# Parámetros recibidos desde ArcGIS Pro
b2 = Raster(arcpy.GetParameterAsText(0))
b3 = Raster(arcpy.GetParameterAsText(1))
b4 = Raster(arcpy.GetParameterAsText(2))
b8 = Raster(arcpy.GetParameterAsText(3))
b11 = Raster(arcpy.GetParameterAsText(4))
mascara_scl = Raster(arcpy.GetParameterAsText(5))
carpeta_salida = arcpy.GetParameterAsText(6)
anio = arcpy.GetParameterAsText(7)

# Evita división entera
b2 = arcpy.sa.Float(b2)
b3 = arcpy.sa.Float(b3)
b4 = arcpy.sa.Float(b4)
b8 = arcpy.sa.Float(b8)
b11 = arcpy.sa.Float(b11)

# Aplicar máscara: se supone que 1 representa píxel válido
b2_valida = Con(mascara_scl == 1, b2)
b3_valida = Con(mascara_scl == 1, b3)
b4_valida = Con(mascara_scl == 1, b4)
b8_valida = Con(mascara_scl == 1, b8)
b11_valida = Con(mascara_scl == 1, b11)

# Índices espectrales
ndvi = (b8_valida - b4_valida) / (b8_valida + b4_valida)
ndwi = (b3_valida - b8_valida) / (b3_valida + b8_valida)
mndwi = (b3_valida - b11_valida) / (b3_valida + b11_valida)
ndbi = (b11_valida - b8_valida) / (b11_valida + b8_valida)

bsi = (
    ((b11_valida + b4_valida) - (b8_valida + b2_valida))
    /
    ((b11_valida + b4_valida) + (b8_valida + b2_valida))
)

# Guardar resultados
ndvi.save(fr"{carpeta_salida}\NDVI_{anio}.tif")
ndwi.save(fr"{carpeta_salida}\NDWI_{anio}.tif")
mndwi.save(fr"{carpeta_salida}\MNDWI_{anio}.tif")
ndbi.save(fr"{carpeta_salida}\NDBI_{anio}.tif")
bsi.save(fr"{carpeta_salida}\BSI_{anio}.tif")

arcpy.AddMessage(f"Índices espectrales calculados para {anio}.")

arcpy.CheckInExtension("Spatial")
