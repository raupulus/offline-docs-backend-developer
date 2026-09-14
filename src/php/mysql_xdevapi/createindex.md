---
title: Collection::createIndex
description: Crear un índice de colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.createindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/createindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 5a20fd035
order: 53020
---

Collection::createIndex

Crear un índice de colección

## Descripción

```php
public mysql_xdevapi\Collection::createIndex(string $index_name, string $index_desc_json): void
```php

Crear un índice en la colección.

Se lanza una excepción si ya existe un índice con el mismo nombre, o si la definición del índice no está correctamente formada.

## Parámetros

`index_name`  
El nombre del índice a crear. Este nombre debe ser un nombre de índice válido tal como aceptado por la consulta SQL `CREATE INDEX`.

`index_desc_json`  
La definición del índice a crear. Contiene un array de objetos IndexField, y cada objeto describe un solo miembro de documento a incluir en el índice, y una cadena opcional para el tipo de índice que podría ser INDEX (por omisión) o SPATIAL.

Una descripción única de IndexField se compone de los siguientes campos:

- `field`: string, la ruta completa del documento hacia el miembro del documento o el campo a indexar.

- `type`: string, uno de los tipos de columnas SQL admitidos para mapear el campo. Para los tipos numéricos, la palabra clave opcional UNSIGNED puede seguir. Para el tipo TEXT, la longitud a considerar para la indexación puede ser añadida.

- `unique`: bool, (opcional) true si el campo debe ser existente en el documento. Por omisión es `false`, excepto para `GEOJSON` donde por omisión es `true`.

- `options`: integer, (opcional) flags de opciones especiales a utilizar al decodificar datos `GEOJSON`.

- `srid`: integer, (opcional) valor srid a utilizar al decodificar datos `GEOJSON`.

Es un error incluir otros campos no descritos anteriormente en los documentos IndexDefinition o IndexField.

## Valores devueltos

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::createIndex`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

// Crear un índice de texto
$collection->createIndex(
  'myindex1',
  '{"fields": [{
    "field": "$.name",
    "type": "TEXT(25)",
    "required": true}],
    "unique": false}'
);

// Un índice espacial
$collection->createIndex(
  'myindex2',
  '{"fields": [{
    "field": "$.home",
    "type": "GEOJSON",
    "required": true}],
    "type": "SPATIAL"}'
);

// Índice con múltiples campos
$collection->createIndex(
  'myindex3',
  '{"fields": [
    {
      "field": "$.name",
      "type": "TEXT(20)",
      "required": true
    },
    {
      "field": "$.age",
      "type": "INTEGER"
    },
    {
      "field": "$.job",
      "type": "TEXT(30)",
      "required": false
    }
  ],
  "unique": true
  }'
);

   
```php
