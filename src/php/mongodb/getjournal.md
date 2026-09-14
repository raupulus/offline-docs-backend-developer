---
title: MongoDB\Driver\WriteConcern::getJournal
description: Devuelve la opción "journal" del WriteConcern
source_url: https://www.php.net/manual/es/mongodb-driver-writeconcern.getjournal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeconcern/getjournal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51480
---

MongoDB\Driver\WriteConcern::getJournal

Devuelve la opción "journal" del WriteConcern

## Descripción

```php
final public MongoDB\Driver\WriteConcern::getJournal(): bool
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "journal" del WriteConcern.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\WriteConcern::getJournal`

```
<?php

$wc = new MongoDB\Driver\WriteConcern(1);
var_dump($wc->getJournal());

$wc = new MongoDB\Driver\WriteConcern(1, 0, true);
var_dump($wc->getJournal());

$wc = new MongoDB\Driver\WriteConcern(1, 0, false);
var_dump($wc->getJournal());

?>

   
```php

El ejemplo anterior mostrará:

    NULL
    bool(true)
    bool(false)

## Véase también

Referencia de Write Concern
