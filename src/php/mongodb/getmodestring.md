---
title: MongoDB\Driver\ReadPreference::getModeString
description: Devuelve la opción "mode" del ReadPreference
source_url: https://www.php.net/manual/es/mongodb-driver-readpreference.getmodestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readpreference/getmodestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50910
---

MongoDB\Driver\ReadPreference::getModeString

Devuelve la opción "mode" del ReadPreference

## Descripción

```php
final public MongoDB\Driver\ReadPreference::getModeString(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la opción "mode" del ReadPreference como string.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadPreference::getModeString`

```
<?php

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::PRIMARY);
var_dump($rp->getModeString());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::PRIMARY_PREFERRED);
var_dump($rp->getModeString());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY);
var_dump($rp->getModeString());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::SECONDARY_PREFERRED);
var_dump($rp->getModeString());

$rp = new MongoDB\Driver\ReadPreference(MongoDB\Driver\ReadPreference::NEAREST);
var_dump($rp->getModeString());

?>

   
```php

El ejemplo anterior mostrará:

    string(7) "primary"
    string(16) "primaryPreferred"
    string(9) "secondary"
    string(18) "secondaryPreferred"
    string(7) "nearest"

## Véase también

MongoDB\Driver\ReadPreference::getMode

Referencia de Read Preference
