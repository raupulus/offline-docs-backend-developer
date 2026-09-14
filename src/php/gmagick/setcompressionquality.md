---
title: Gmagick::setCompressionQuality
description: Define la calidad de compresión por defecto del objeto
source_url: https://www.php.net/manual/es/gmagick.setcompressionquality.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/gmagick/setcompressionquality.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: true
translation_revision: 35752f072
order: 27490
---

Gmagick::setCompressionQuality

Define la calidad de compresión por defecto del objeto

## Descripción

```php
Gmagick::setCompressionQuality(int $quality): Gmagick
```php

Define la calidad de compresión por defecto del objeto.

## Parámetros

`quality`  
El valor por defecto de GraphicsMagick es 75.

## Valores devueltos

El objeto `Gmagick`.

## Errores/Excepciones

Emite una excepción `GmagickException` en caso de error.

## Ejemplos

Ejemplo con `Gmagick::setCompressionQuality`

```
     
<?php
$gm = new Gmagick();
$gm->read("magick:rose");
$gm->setCompressionQuality(2);
?>

     
```php
