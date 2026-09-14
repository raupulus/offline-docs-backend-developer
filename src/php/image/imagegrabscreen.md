---
title: imagegrabscreen
description: Captura la pantalla completa
source_url: https://www.php.net/manual/es/function.imagegrabscreen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/imagegrabscreen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 9960a09a5
order: 32140
---

imagegrabscreen

Captura la pantalla completa

## Descripción

```php
imagegrabscreen(): GdImage
```php

`imagegrabscreen` realiza una captura de toda la pantalla.

> [!NOTE]
> Esta función solo está disponible en Windows.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto imagen en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `GDImage` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `imagegrabscreen`

Este ejemplo muestra cómo realizar una captura de pantalla y guardarla en una imagen png.

```
<?php
$im = imagegrabscreen();
imagepng($im, "myscreenshot.png");
?>

    
```php

## Véase también

imagegrabwindow
