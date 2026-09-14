---
title: Imagick::getImageLength
description: Devuelve el tamaño de la imagen en bytes
source_url: https://www.php.net/manual/es/imagick.getimagelength.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagick/getimagelength.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 65c4446ab
order: 33840
---

Imagick::getImageLength

Devuelve el tamaño de la imagen en bytes

## Descripción

```php
public Imagick::getImageLength(): int
```php

Devuelve el tamaño de la imagen en bytes.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un integer.

## Ejemplos

Ejemplo con `Imagick::getImageLength`:

Obtiene el tamaño de la imagen, en bytes

```
<?php
$image = new Imagick('test.jpg');
echo $image->getImageLength() . ' bytes';
?>

    
```php
