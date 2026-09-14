---
title: ArrayObject::getFlags
description: Obtiene las opciones de comportamiento
source_url: https://www.php.net/manual/es/arrayobject.getflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/getflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81410
---

ArrayObject::getFlags

Obtiene las opciones de comportamiento

## Descripción

```php
public ArrayObject::getFlags(): int
```php

Obtiene las opciones de comportamiento del objeto `ArrayObject`. Consúltese el método [ArrayObject::setFlags](#arrayobject.setflags) para obtener una lista de opciones disponibles.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve las opciones de comportamiento del objeto `ArrayObject`.

## Ejemplos

Ejemplo con `ArrayObject::getFlags`

```
<?php
// Lista de frutas
$fruits = array("limones" => 1, "naranjas" => 4, "plátanos" => 5, "manzanas" => 10);

$fruitsArrayObject = new ArrayObject($fruits);

// Lista las opciones actuales
$flags = $fruitsArrayObject->getFlags();
var_dump($flags);

// Configura nuevas opciones
$fruitsArrayObject->setFlags(ArrayObject::ARRAY_AS_PROPS);

// Obtiene las nuevas opciones
$flags = $fruitsArrayObject->getFlags();
var_dump($flags);
?>

    
```php

El ejemplo anterior mostrará:

    int(0)
    int(2)

## Véase también

ArrayObject::setFlags
