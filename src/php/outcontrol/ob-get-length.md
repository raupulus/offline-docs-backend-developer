---
title: ob_get_length
description: Devuelve la longitud del contenido del búfer de salida
source_url: https://www.php.net/manual/es/function.ob-get-length.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-get-length.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 6ab6ea465
order: 59810
---

ob_get_length

Devuelve la longitud del contenido del búfer de salida

## Descripción

```php
ob_get_length(): int
```php

Devuelve la longitud del contenido del búfer de salida, en bytes.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la longitud del contenido del búfer de salida, en bytes, si la temporización está activada, y `false` en caso contrario.

## Ejemplos

Ejemplo con `ob_get_length`

```
<?php

ob_start();

echo "Bonjour ";

$len1 = ob_get_length();

echo "le monde";

$len2 = ob_get_length();

ob_end_clean();

echo $len1 . ", " . $len2;
?>

    
```php

El ejemplo anterior mostrará:

    8, 16

## Véase también

`ob_start`, `ob_get_contents`
