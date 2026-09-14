---
title: SplFileObject::getMaxLineLen
description: Obtener la longitud máxima de línea
source_url: https://www.php.net/manual/es/splfileobject.getmaxlinelen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/getmaxlinelen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84530
---

SplFileObject::getMaxLineLen

Obtener la longitud máxima de línea

## Descripción

```php
public SplFileObject::getMaxLineLen(): int
```php

Obtiene la longitud máxima de línea establecida por SplFileObject::setMaxLineLen.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la longitud máxima de línea si ha sido establecido con SplFileObject::setMaxLineLen, por omisión es `0`.

## Ejemplos

Ejemplo de SplFileObject::getMaxLineLen

```
<?php
$file = new SplFileObject("fichero.txt");
var_dump($file->getMaxLineLen());

$file->setMaxLineLen(20);
var_dump($file->getMaxLineLen());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(0)
    int(20)

## Véase también

SplFileObject::setMaxLineLen
