---
title: exif_tagname
description: Obtener el nombre de la cabecera de un índice
source_url: https://www.php.net/manual/es/function.exif-tagname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exif/functions/exif-tagname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exif
translation_status: ready
translation_revision: 6a08181be
order: 20690
---

exif_tagname

Obtener el nombre de la cabecera de un índice

## Descripción

```php
exif_tagname(int $index): string
```php

## Parámetros

`index`  
La etiqueta ID correspondiente a la etiqueta Name que examinará.

## Valores devueltos

Devuelve el nombre de la cabecera, o `false` si `index` no está definido con un identificador de etiqueta EXIF.

## Ejemplos

Ejemplo `exif_tagname`

```
<?php
echo "256: ".exif_tagname(256).PHP_EOL;
echo "257: ".exif_tagname(257).PHP_EOL;
?>

   
```php

El ejemplo anterior mostrará:

    256: ImageWidth
    257: ImageLength

## Véase también

exif_imagetype

Especificación EXIF

Etiquetas EXIF
