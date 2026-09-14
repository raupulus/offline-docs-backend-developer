---
title: MongoDB\BSON\MaxKey::__construct
description: Construye un nuevo MaxKey
source_url: https://www.php.net/manual/es/mongodb-bson-maxkey.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/maxkey/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 47940
---

MongoDB\BSON\MaxKey::\_\_construct

Construye un nuevo MaxKey

## Descripción

```php
final public MongoDB\BSON\MaxKey::__construct()
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo con `MongoDB\BSON\MaxKey::__construct`

```
<?php

var_dump(new MongoDB\BSON\MaxKey());

?>

   
```php

El ejemplo anterior mostrará:

    object(MongoDB\BSON\MaxKey)#1 (0) {
    }

## Véase también

Tipos BSON
