---
title: Gmagick::quantizeimage
description: Analiza los colores dentro de una imagen de referencia
source_url: https://www.php.net/manual/es/gmagick.quantizeimage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/quantizeimage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: 35752f072
order: 27290
---

Gmagick::quantizeimage

Analiza los colores dentro de una imagen de referencia

## Descripción

```php
public Gmagick::quantizeimage(int $numColors, int $colorspace, int $treeDepth, bool $dither, bool $measureError): Gmagick
```php

Analiza los colores dentro de una imagen de referencia y elige un número fijo de colores que representan la imagen. El objetivo del algoritmo es minimizar la diferencia de colores entre la imagen de entrada y de salida mientras minimiza el tiempo de procesamiento.

## Parámetros

`numColors`  
El número de colores.

`colorspace`  
Lleva a cabo una reducción de color en este espacio de color, normalmaente RGBColorspace.

`treeDepth`  
Normalmente, este valor de tipo integer es cero o uno. Un cero o uno indica a Quantize que elija una profundidad de árbol óptima de Log4(número_colores).% Un árbol de esta profundidad generalmente permite la mejor representación de la imagen de referencia con la menor cantidad de memoria y la velocidad de computación más rápida. En algunos casos, como una imagen con dispersión de color baja (un número bajo de colores), se requiere un valor distinto de Log4(número_colores). Para expandir el árbol de colores completamente, use un valor de 8.

`dither`  
Un valor distinto de cero distribuye la diferencia entre una imagen original y el algoritmo de reducción de color correspondiente a los píxeles de la zona inmediata a lo largo de una curva de Hilbert.

`measureError`  
Un valor distinto de cero mide la diferencia entre la imagen original y la cuantificada. Esta diferencia es el error de cuantización total. El error se computa sumando, en todos los píxeles de una imagen, la distancia al cuadrado en el espacio RGB entre cada valor de píxel de referncia y su valor cuantizado.

## Valores devueltos

El objeto Gmagick si se tuvo éxito

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.
