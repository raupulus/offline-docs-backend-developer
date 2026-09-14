---
title: MongoDB\Driver\ReadConcern::__construct
description: Crear un nuevo ReadConcern
source_url: https://www.php.net/manual/es/mongodb-driver-readconcern.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/readconcern/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50820
---

MongoDB\Driver\ReadConcern::\_\_construct

Crear un nuevo ReadConcern

## Descripción

```php
final public MongoDB\Driver\ReadConcern::__construct([string $level])
```php

Construye un nuevo `MongoDB\Driver\ReadConcern`, que es un objeto de valor inmutable.

## Parámetros

`level`  
El [nivel del read concern](https://www.mongodb.com/docs/manual/reference/read-concern/#read-concern-levels). Se puede utilizar, pero no se limita a, una de las [constantes de clase](#mongodb-driver-readconcern.constants).

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\ReadConcern::__construct`

```
<?php

/* Nivel de lectura aislado no especificado (utiliza el comportamiento por omisión del servidor) */
$rc = new MongoDB\Driver\ReadConcern();

/* Consulta con un nivel de lectura aislado a partir de un solo nodo del conjunto de réplicas */
$rc = new MongoDB\Driver\ReadConcern(MongoDB\Driver\ReadConcern::LOCAL);

/* Consulta con un nivel de lectura aislado a partir de una mayoría de los nodos del conjunto de réplicas */
$rc = new MongoDB\Driver\ReadConcern(MongoDB\Driver\ReadConcern::MAJORITY);

?>

   
```php

## Véase también

Referencia de Read Concern
