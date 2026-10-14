# Model Card: Falcon 7B para análisis multitemporal de Lagos de Torca

## 1. Descripción del modelo

Falcon 7B es un modelo grande de lenguaje desarrollado originalmente por el Technology Innovation Institute (TII). En este proyecto se ejecuta localmente mediante Ollama con la etiqueta `falcon:7b`.

El modelo se emplea como asistente para diseñar, explicar y documentar una metodología de análisis multitemporal de cambios de cobertura en Lagos de Torca, Bogotá, usando imágenes Sentinel-2 de 2016 y 2026.

Falcon 7B no procesa directamente los archivos ráster ni sustituye las operaciones realizadas en ArcGIS Pro. Su función es generar orientaciones textuales, fórmulas, explicaciones metodológicas y propuestas de código.

## 2. Información técnica

| Parámetro | Valor |
|---|---|
| Nombre | Falcon 7B |
| Desarrollador original | Technology Innovation Institute (TII) |
| Arquitectura | Falcon |
| Número de parámetros | 7 mil millones |
| Plataforma de ejecución | Ollama |
| Etiqueta local | `falcon:7b` |
| Cuantización | Q4_0 |
| Tamaño aproximado | 4,2 GB |
| Longitud de contexto | 2048 tokens |
| Tipo de entrada | Texto |
| Tipo de salida | Texto |
| Capacidad reportada | Generación o completado de texto |
| Idioma principal del proyecto | Español |

## 3. Uso previsto

El modelo se utiliza para apoyar las siguientes actividades:

- Diseñar la metodología del análisis multitemporal.
- Explicar las características de las bandas Sentinel-2.
- Formular índices espectrales.
- Proponer procedimientos para ArcGIS Pro.
- Generar ejemplos de código en Python y ArcPy.
- Documentar el flujo de procesamiento.
- Ayudar a interpretar los resultados obtenidos.

## 4. Datos del proyecto

El estudio utiliza imágenes Sentinel-2 correspondientes a 2016 y 2026, seleccionadas considerando la menor presencia posible de nubes sobre el área de estudio.

Las bandas empleadas incluyen:

| Banda | Resolución original | Aplicación |
|---|---:|---|
| B2 – Azul | 10 m | Composición RGB y apoyo a la identificación visual |
| B3 – Verde | 10 m | RGB y análisis de agua |
| B4 – Rojo | 10 m | RGB, vegetación y suelo |
| B8 – Infrarrojo cercano | 10 m | Vegetación y agua |
| B11 – SWIR 1 | 20 m | Humedad, áreas construidas y suelo |
| B12 – SWIR 2 | 20 m | Suelo, humedad y superficies construidas |
| SCL | 20 m | Máscara de nubes, sombras y píxeles no válidos |

Las bandas B11, B12 y SCL se remuestrean a 10 metros para hacerlas compatibles con las bandas B2, B3, B4 y B8.

## 5. Preprocesamiento geoespacial

El procesamiento se realiza en ArcGIS Pro mediante:

1. Reproyección al sistema de referencia MAGNA-SIRGAS / Origen-Nacional, EPSG:9377.
2. Remuestreo de las bandas de 20 m a 10 m.
3. Alineación mediante un ráster de ajuste o `Snap Raster`.
4. Recorte con el polígono de Lagos de Torca.
5. Creación de máscaras mediante la capa SCL.
6. Exclusión de nubes, sombras y píxeles no válidos.
7. Cálculo de índices espectrales.
8. Comparación de resultados entre 2016 y 2026.

## 6. Índices espectrales

### NDVI — vegetación

```text
NDVI = (B8 - B4) / (B8 + B4)
```

### NDWI — agua superficial

```text
NDWI = (B3 - B8) / (B3 + B8)
```

### MNDWI — agua con reducción del efecto urbano

```text
MNDWI = (B3 - B11) / (B3 + B11)
```

### NDBI — superficies construidas

```text
NDBI = (B11 - B8) / (B11 + B8)
```

### BSI — suelo desnudo

```text
BSI = ((B11 + B4) - (B8 + B2)) / ((B11 + B4) + (B8 + B2))
```

## 7. Resultados esperados

El procedimiento permitirá:

- Comparar la cobertura de 2016 y 2026.
- Identificar pérdida o recuperación de vegetación.
- Detectar modificaciones en cuerpos de agua o zonas húmedas.
- Reconocer la expansión de superficies construidas.
- Identificar cambios hacia suelo desnudo.
- Elaborar mapas temáticos y estadísticas por año.
- Construir una matriz de transición de coberturas.

## 8. Limitaciones

- Falcon 7B puede generar información incorrecta o incompleta.
- Sus respuestas deben ser verificadas por una persona con conocimientos en teledetección y SIG.
- El modelo no interpreta directamente archivos Sentinel-2, rásteres o geodatabases.
- La cuantización puede reducir la precisión de algunas respuestas.
- Su contexto de 2048 tokens limita la información procesada en una sola consulta.
- Los resultados espaciales dependen de la calidad y alineación de las imágenes.
- Las diferencias estacionales, atmosféricas y de iluminación pueden confundirse con cambios reales.
- Dos fechas permiten detectar diferencias, pero no demuestran por sí solas que los cambios fueron causados por el Plan Zonal del Norte.
- El uso del modelo no sustituye la validación de campo ni la revisión de fuentes oficiales.

## 9. Consideraciones éticas

Los resultados deben comunicarse con precaución. No se deben presentar como una demostración automática de causalidad entre el Plan Zonal del Norte y los cambios observados.

La interpretación debe complementarse con instrumentos de planificación, cartografía oficial, cronologías de obras, licencias urbanísticas y otras fuentes verificables.

## 10. Recomendaciones de uso

- Utilizar instrucciones claras y proporcionar contexto técnico.
- Dividir las consultas complejas en tareas pequeñas.
- Verificar fórmulas, rutas, nombres de bandas y código.
- No introducir información personal o confidencial.
- Comparar las respuestas del modelo con documentación técnica oficial.
- Registrar los parámetros empleados para garantizar la reproducibilidad.

## 11. Ejemplo de instrucción

```text
Actúa como especialista en teledetección y análisis multitemporal.
Diseña un procedimiento en ArcGIS Pro para comparar cambios de vegetación,
agua, suelo desnudo y superficies construidas en Lagos de Torca mediante
imágenes Sentinel-2 de 2016 y 2026. Considera las bandas B2, B3, B4, B8,
B11 y B12, una máscara SCL, resolución de 10 metros y sistema EPSG:9377.
Aclara las limitaciones y no atribuyas causalidad sin evidencia adicional.

```

## 12. Autoría del proyecto

- **Autora:** Tatiana Alexandra Otálora Casas
- **Programa:** Ingeniería Catastral y Geodesia
- **Universidad:** Universidad Distrital Francisco José de Caldas
- **Usuario de GitHub:** [tatianaotalora20263](https://github.com/tatianaotalora20263)
- **Fecha:** 14 de octubre de 2026
