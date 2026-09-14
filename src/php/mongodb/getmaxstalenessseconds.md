---
title: MongoDB\Driver\ReadPreference::getMaxStalenessSeconds
description: Devuelve la opción "maxStalenessSeconds" del ReadPreference
source_url: https://www.php.net/manual/es/mongodb-driver-readpreference.getmaxstalenessseconds.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference/getmaxstalenessseconds.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50890
---

MongoDB\Driver\ReadPreference::getMaxStalenessSeconds

Devuelve la opción "maxStalenessSeconds" del ReadPreference

## Descripción

```php
final public MongoDB\Driver\ReadPreference::getMaxStalenessSeconds(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "maxStalenessSeconds" del ReadPreference. Si no se ha especificado ningún tiempo máximo, `MongoDB\Driver\ReadPreference::NO_MAX_STALENESS` será devuelto.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadPreference::getMaxStalenessSeconds`

```
<?php

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY);
var_dump($rp->getMaxStalenessSeconds());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY, null, [
    'maxStalenessSeconds' => MongoDB\Driver\ReadPreference::NO_MAX_STALENESS,
]);
var_dump($rp->getMaxStalenessSeconds());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY, null, [
    'maxStalenessSeconds' => MongoDB\Driver\ReadPreference::SMALLEST_MAX_STALENESS_SECONDS,
]);
var_dump($rp->getMaxStalenessSeconds());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY, null, [
    'maxStalenessSeconds' => 1000,
]);
var_dump($rp->getMaxStalenessSeconds());

?>

   
```php

El ejemplo anterior mostrará:

    int(-1)
    int(-1)
    int(90)
    int(1000)

## Véase también

Referencia de Read Preference
