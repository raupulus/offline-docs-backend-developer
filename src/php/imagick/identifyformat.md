---
title: Imagick::identifyFormat
description: Formatea un string con los detalles de la imagen
source_url: https://www.php.net/manual/es/imagick.identifyformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/identifyformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1534707f6
order: 34330
---

Imagick::identifyFormat

Formatea un string con los detalles de la imagen

## Descripción

```php
public Imagick::identifyFormat(string $embedText): string
```php

Reemplaza todos los caracteres de formato integrados por la propiedad de imagen apropiada y devuelve el texto interpretado. Consulte http://www.imagemagick.org/script/escape.php para las secuencias de escape.

## Parámetros

`embedText`  
Un string que contiene secuencias de formato, por ejemplo "Caja de recorte: %@ número de colores únicos: %k".

## Valores devueltos

Devuelve el formato o `false` si ocurre un error.

## Ejemplos

`Imagick::identifyFormat`

```
      
<?php
        $output = "La salida de 'Caja de recorte: %@ número de colores únicos: %k' es: <br/>";
        $imagick = new \Imagick(realpath("./images/artifact/mask.png"));
        $output .= $imagick->identifyFormat("Caja de recorte: %@ número de colores únicos: %k");

?>

      
```php
