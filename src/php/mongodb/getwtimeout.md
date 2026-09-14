---
title: MongoDB\Driver\WriteConcern::getWtimeout
description: Devuelve la opción "wtimeout" del WriteConcern
source_url: https://www.php.net/manual/es/mongodb-driver-writeconcern.getwtimeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcern/getwtimeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51500
---

MongoDB\Driver\WriteConcern::getWtimeout

Devuelve la opción "wtimeout" del WriteConcern

## Descripción

```php
final public MongoDB\Driver\WriteConcern::getWtimeout(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "wtimeout" del WriteConcern.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.7.0 | En sistemas de 32 bits, este método siempre truncará el valor `wTimeout` si excede el rango de 32 bits. En tal caso, se emitirá una advertencia. |

## Ejemplos

Ejemplo de `MongoDB\Driver\WriteConcern::getWtimeout`

```
<?php

$wc = new MongoDB\Driver\WriteConcern(1);
var_dump($wc->getWtimeout());

$wc = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 3000);
var_dump($wc->getWtimeout());

?>

   
```php

El ejemplo anterior mostrará:

    int(0)
    int(3000)

## Véase también

Referencia de Write Concern
