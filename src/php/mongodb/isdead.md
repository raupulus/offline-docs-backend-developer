---
title: MongoDB\Driver\Cursor::isDead
description: Comprueba si el cursor está agotado o puede tener resultados adicionales
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.isdead.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/isdead.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49280
---

MongoDB\Driver\Cursor::isDead

Comprueba si el cursor está agotado o puede tener resultados adicionales

## Descripción

```php
final public MongoDB\Driver\Cursor::isDead(): bool
```php

Comprueba si no hay definitivamente más resultados disponibles en el cursor. Este método es similar al método [cursor.isExhausted()](https://www.mongodb.com/docs/manual/reference/method/cursor.isExhausted/) en el MongoDB shell y es principalmente útil al iterar [cursores persistentes](https://www.mongodb.com/docs/manual/core/tailable-cursors/).

Un cursor no tiene más resultados y se considera "agotado" cuando se cumple una de las siguientes condiciones: La actual serie de resultados se ha iterado completamente *y* el identificador del cursor es cero (es decir, no se puede emitir un [getMore](https://www.mongodb.com/docs/manual/reference/command/getMore/))., Se encontró un error al iterar el cursor., El cursor alcanzó su límite configurado.

Por diseño, no siempre es posible determinar si un cursor tiene resultados adicionales. Los casos en los que un cursor *puede* tener más datos disponibles son los siguientes: Hay documentos adicionales en la actual serie de resultados, que están almacenados en el lado-cliente. Iterar obtendrá un documento del búfer local., No hay documentos adicionales en la actual serie de resultados (es decir, búfer local), pero el identificador del cursor no es cero. Iterar solicitará más documentos al servidor mediante una operación [getMore](https://www.mongodb.com/docs/manual/reference/command/getMore/), que puede o no devolver más resultados y/o indicar que el cursor ha sido cerrado en el servidor al devolver cero para su identificador.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si no hay definitivamente más resultados disponibles en el cursor, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Ejemplos

Ejemplo de `MongoDB\Driver\Cursor::isDead`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$query = new MongoDB\Driver\Query([]);

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1]);
$bulk->insert(['x' => 2]);
$bulk->insert(['x' => 3]);
$manager->executeBulkWrite('db.collection', $bulk);

$cursor = $manager->executeQuery('db.collection', $query);

$iterator = new IteratorIterator($cursor);

$iterator->rewind();
var_dump($cursor->isDead());

$iterator->next();
var_dump($cursor->isDead());

$iterator->next();
var_dump($cursor->isDead());

$iterator->next();
var_dump($cursor->isDead());

?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    bool(false)
    bool(true)

## Véase también

Cursores persistentes

en el manual de MongoDB

cursor.isExhausted()

en el manual de MongoDB
