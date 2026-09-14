---
title: Imagick::queryFontMetrics
description: Devuelve una matriz que representa las métricas de la fuente
source_url: https://www.php.net/manual/es/imagick.queryfontmetrics.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/queryfontmetrics.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_revision: 0ffb9c9fc
order: 34770
---

Imagick::queryFontMetrics

Devuelve una matriz que representa las métricas de la fuente

## Descripción

```php
public Imagick::queryFontMetrics(ImagickDraw $properties, string $text, [bool $multiline]): array
```php

Devuelve un array multidimensional que representa las métricas de la fuente.

## Parámetros

`properties`  
Objeto ImagickDraw que contiene las propiedades de la fuente

`text`  
El texto

`multiline`  
Parámetro multilínea. Si se deja vacío se autodetecta

## Valores devueltos

Devuelve un array multidimensional que representa las métricas de la fuente.

## Errores/Excepciones

Lanza una ImagickException en caso de error.

## Ejemplos

Usar `Imagick::queryFontMetrics`:

Preguntar por las métricas del texto y verter los resultados en la pantalla.

```
<?php
/* Crear un nuevo objeto Imagick */
$im = new Imagick();

/* Crear un objeto ImagickDraw */
$draw = new ImagickDraw();

/* Establecer la fuente */
$draw->setFont('/path/to/font.ttf');

/* Verter las métricas de la fuente, autodetectado multilínea */
var_dump($im->queryFontMetrics($draw, "¡Hola Mundo!"));
?>

    
```php
