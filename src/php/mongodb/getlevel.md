---
title: MongoDB\Driver\ReadConcern::getLevel
description: Devuelve la opción "level" del ReadConcern
source_url: https://www.php.net/manual/es/mongodb-driver-readconcern.getlevel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readconcern/getlevel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50830
---

MongoDB\Driver\ReadConcern::getLevel

Devuelve la opción "level" del ReadConcern

## Descripción

```php
final public MongoDB\Driver\ReadConcern::getLevel(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "level" del ReadConcern.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadConcern::getLevel`

```
<?php

$rc = new MongoDB\Driver\ReadConcern();
var_dump($rc->getLevel());

$rc = new MongoDB\Driver\ReadConcern(MongoDB\Driver\ReadConcern::LOCAL);
var_dump($rc->getLevel());

$rc = new MongoDB\Driver\ReadConcern(MongoDB\Driver\ReadConcern::MAJORITY);
var_dump($rc->getLevel());

?>

   
```php

El ejemplo anterior mostrará:

    NULL
    string(5) "local"
    string(8) "majority"

## Véase también

Referencia de Read Concern
