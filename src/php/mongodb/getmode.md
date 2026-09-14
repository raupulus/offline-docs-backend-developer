---
title: MongoDB\Driver\ReadPreference::getMode
description: Devuelve la opción "mode" del ReadPreference
source_url: https://www.php.net/manual/es/mongodb-driver-readpreference.getmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference/getmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50900
---

MongoDB\Driver\ReadPreference::getMode

Devuelve la opción "mode" del ReadPreference

> [!WARNING]
> Esta función ha sido *DEPRECADA* desde la versión 1.20.0 de la extensión y ha sido eliminada en la versión 2.0. Las aplicaciones deberían utilizar MongoDB\Driver\ReadPreference::getModeString en su lugar.

## Descripción

```php
final public MongoDB\Driver\ReadPreference::getMode(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "mode" del ReadPreference.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión            | Descripción                    |
|--------------------|--------------------------------|
| PECL mongodb 2.0.0 | Este método ha sido eliminado. |

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadPreference::getMode`

```
<?php

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::PRIMARY);
var_dump($rp->getMode());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::PRIMARY_PREFERRED);
var_dump($rp->getMode());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY);
var_dump($rp->getMode());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED);
var_dump($rp->getMode());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::NEAREST);
var_dump($rp->getMode());

?>

   
```php

El ejemplo anterior mostrará:

    int(1)
    int(5)
    int(2)
    int(6)
    int(10)

## Véase también

MongoDB\Driver\ReadPreference::getModeString

Referencia de Read Preference
