---
title: Imagick::clone
description: Realiza una copia exacta de un objeto Imagick
source_url: https://www.php.net/manual/es/imagick.clone.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/clone.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: false
translation_revision: 65c4446ab
order: 32840
---

Imagick::clone

Realiza una copia exacta de un objeto Imagick

## Descripción

```php
public Imagick::clone(): Imagick
```php

Realiza una copia exacta de un objeto Imagick.

> [!WARNING]
> Esta función se ha vuelto *OBSOLETA* a partir de imagick 3.1.0. Ahora debe utilizarse la palabra clave [clone](#language.oop5.cloning).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia del objeto Imagick.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL imagick 3.1.0 | Este método se ha vuelto obsoleto en favor de la palabra clave [clone](#language.oop5.cloning). |

## Ejemplos

Clonación de objeto Imagick con diferentes versiones de Imagick

```
     
<?php
// Clonación de un objeto Imagick utilizando la versión 2.x y 3.0:
$newImage = $image->clone();

// Clonación de un objeto Imagick a partir de la versión 3.1.0:
$newImage = clone $image;
?>

    
```php
