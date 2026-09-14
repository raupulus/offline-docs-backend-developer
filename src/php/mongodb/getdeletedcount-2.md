---
title: MongoDB\Driver\WriteResult::getDeletedCount
description: Devuelve el número de documentos eliminados
source_url: https://www.php.net/manual/es/mongodb-driver-writeresult.getdeletedcount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/writeresult/getdeletedcount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51620
---

MongoDB\Driver\WriteResult::getDeletedCount

Devuelve el número de documentos eliminados

## Descripción

```php
final public MongoDB\Driver\WriteResult::getDeletedCount(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de documentos eliminados.

## Errores/Excepciones

Levanta una excepción

MongoDB\Driver\Exception\LogicException

si la escritura no ha sido reconocida.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | Este método ahora lanza una excepción cuando es llamado para una escritura no reconocida, en lugar de retornar `null`. |

## Ejemplos

Ejemplo con `MongoDB\Driver\WriteResult::getDeletedCount`

```
<?php

$manager = new MongoDB\Driver\Manager;

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->update(['x' => 1], ['$set' => ['y' => 3]]);
$bulk->update(['x' => 2], ['$set' => ['y' => 1]], ['upsert' => true]);
$bulk->update(['x' => 3], ['$set' => ['y' => 2]], ['upsert' => true]);
$bulk->delete(['x' => 1]);

$result = $manager->executeBulkWrite('db.collection', $bulk);

var_dump($result->getDeletedCount());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(1)

## Véase también

MongoDB\Driver\WriteResult::isAcknowledged
