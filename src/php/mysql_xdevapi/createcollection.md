---
title: Schema::createCollection
description: Añade una colección al esquema
source_url: https://www.php.net/manual/es/mysql-xdevapi-schema.createcollection.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/schema/createcollection.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53870
---

Schema::createCollection

Añade una colección al esquema

## Descripción

```php
public mysql_xdevapi\Schema::createCollection(string $name, [string $validate]): mysql_xdevapi\Collection
```php

Crea una colección en el esquema.

## Parámetros

`name`  
El nombre de la colección.

`validate`  
La definición de validación, como un objeto JSON.

## Valores devueltos

El objeto Collection.

## Historial de cambios

| Versión | Descripción                              |
|---------|------------------------------------------|
| 8.0.20  | Adición del argumento opcional validate. |

## Ejemplos

Ejemplo de mysql_xdevapi\Schema::createCollection

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS food")->execute();
$session->sql("CREATE DATABASE food")->execute();
$session->sql("CREATE TABLE food.fruit(name text, rating text)")->execute();

$schema = $session->getSchema("food");
$schema->createCollection("trees");

print_r($schema->gettables());
print_r($schema->getcollections());

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [fruit] => mysql_xdevapi\Table Object
            (
                [name] => fruit
            )
    )
    Array
    (
        [trees] => mysql_xdevapi\Collection Object
            (
                [name] => trees
            )
    )

Ejemplo de mysql_xdevapi\Schema::createCollection

```
 
 <?php
 $collection = $schema->createCollection("mycollection", '{
    "validation": {
        "level": "strict",
        "schema": {
            "id": "http://json-schema.org/geo",
            "description": "A geographical coordinate",
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number"
                },
                "longitude": {
                    "type": "number"
                }
            },
            "required": ["latitude", "longitude"]
        }
    }
}');
// Éxito
$collection->add('{"latitude": 10, "longitude": 20}')->execute();

// Fallo, tipos inválidos (no son números)
$collection->add('{"latitude": "lat", "longitude": "long"}')->execute();

    
```php
