---
title: MongoDB\BSON\Timestamp::__construct
description: Construye una nueva marca de tiempo (Timestamp)
source_url: https://www.php.net/manual/es/mongodb-bson-timestamp.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/timestamp/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48430
---

MongoDB\BSON\Timestamp::\_\_construct

Construye una nueva marca de tiempo (Timestamp)

## Descripción

```php
final public MongoDB\BSON\Timestamp::__construct(int $increment, int $timestamp)
```php

## Parámetros

`increment` (`int`)  
Entero de 32 bits que denota el ordinal de incremento para operaciones dentro de un mismo segundo.

`timestamp` (`int`)  
Entero de 32 bits que denota los segundos transcurridos desde la época Unix.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\BSON\Timestamp::__construct`

```
<?php

$timestamp = new MongoDB\BSON\Timestamp(1234, 5678);

?>

   
```php

El ejemplo anterior mostrará:

    object(MongoDB\BSON\Timestamp)#1 (2) {
      ["increment"]=>
      int(1234)
      ["timestamp"]=>
      int(5678)
    }

## Véase también

Tipos BSON: Marcas de tiempo (Timestamps)
