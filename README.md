# Falcon 7B aplicado al análisis multitemporal de Lagos de Torca

Este repositorio documenta el uso del modelo de lenguaje Falcon 7B, ejecutado localmente mediante Ollama, como herramienta de apoyo para diseñar y documentar una metodología de análisis multitemporal de cambios de cobertura en Lagos de Torca, Bogotá.

El estudio emplea imágenes Sentinel-2 de 2016 y 2026. El procesamiento geoespacial se realiza en ArcGIS Pro mediante reproyección, recorte, enmascaramiento de nubes y sombras, cálculo de índices espectrales y comparación temporal.

Falcon no procesa directamente las imágenes Sentinel-2. Su función dentro del proyecto consiste en apoyar la explicación de procedimientos, la generación de fórmulas, la documentación metodológica y la elaboración de código.

## Modelo utilizado

- **Modelo:** Falcon 7B
- **Implementación local:** Ollama
- **Etiqueta:** `falcon:7b`
- **Desarrollador original:** Technology Innovation Institute (TII)
- **Tipo de entrada:** texto
- **Tipo de salida:** texto

## Ficha del modelo

La ficha completa se encuentra en:

[Consultar la ficha del modelo](MODEL_CARD.md)

## Aplicación del proyecto

El modelo se utiliza como apoyo para:

- Organizar la metodología multitemporal.
- Explicar las bandas de Sentinel-2.
- Formular los índices NDVI, NDWI, MNDWI, NDBI y BSI.
- Generar instrucciones para ArcGIS Pro.
- Apoyar la elaboración de código en Python y ArcPy.
- Documentar e interpretar los resultados.

## Imágenes del área de estudio

### Composición RGB de 2016

![Composición RGB de Lagos de Torca en 2016](images/rgb_lagos_torca_2016.png)

### Composición RGB de 2026

![Composición RGB de Lagos de Torca en 2026](images/rgb_lagos_torca_2026.png)

## Autor

- **Nombre:** Tatiana Alexandra Otálora Casas
- **Programa:** Ingeniería Catastral y Geodesia
- **Universidad:** Universidad Distrital Francisco José de Caldas
- **Usuario de GitHub:** [tatianaotalora20263](https://github.com/tatianaotalora20263)
- **Fecha:** 14 de octubre de 2026
