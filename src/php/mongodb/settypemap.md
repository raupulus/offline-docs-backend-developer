---
title: MongoDB\Driver\Cursor::setTypeMap
description: Establece un mapa de tipos para usar en la deserialización BSON
source_url: https://www.php.net/manual/es/mongodb-driver-cursor.settypemap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor/settypemap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49320
---

MongoDB\Driver\Cursor::setTypeMap

Establece un mapa de tipos para usar en la deserialización BSON

## Descripción

```php
final public MongoDB\Driver\Cursor::setTypeMap(array $typemap): void
```php

Establece la [configuración del mapa de tipos](#mongodb.persistence.typemaps) que se usará al deserializar los resultados BSON en valores de PHP.

## Parámetros

`typeMap` (`array`)  
[Configuración del mapa de tipos](#mongodb.persistence.typemaps).

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Al iterar sobre el cursor, también se pueden lanzar las siguientes excepciones debido a una configuración incorrecta del mapa de tipos: Lanza `MongoDB\Driver\Exception\InvalidArgumentException` si una clase en el mapa de tipos no puede ser instanciada o no implementa MongoDB\BSON\Unserializable.

## Ejemplos

Ejemplo de `MongoDB\Driver\Cursor::setTypeMap`

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

$bulk = new MongoDB\Driver\BulkWrite;
$id = $bulk->insert(['x' => 1]);
$manager->executeBulkWrite('db.collection', $bulk);

$query = new MongoDB\Driver\Query(['_id' => $id]);
$cursor = $manager->executeQuery('db.collection', $query);
$cursor->setTypeMap(['root' => 'array']);

foreach ($cursor as $document) {
    var_dump($document);
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["_id"]=>
      object(MongoDB\BSON\ObjectId)#6 (1) {
        ["oid"]=>
        string(24) "56424fb76118fd3267180741"
      }
      ["x"]=>
      int(1)
    }

## Véase también
