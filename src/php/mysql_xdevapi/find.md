---
title: Collection::find
description: Búsqueda de documento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.find.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/find.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53050
---

Collection::find

Búsqueda de documento

## Descripción

```php
public mysql_xdevapi\Collection::find([string $search_condition]): mysql_xdevapi\CollectionFind
```php

Busca una colección de base de datos para un documento o un conjunto de documentos. Los documentos encontrados se devuelven en forma de un objeto CollectionFind para modificarlos o recuperar resultados adicionales.

## Parámetros

`search_condition`  
Aunque es opcional, normalmente se define una condición para limitar los resultados a un subconjunto de documentos.

Varios elementos pueden construir la condición y la sintaxis soporta la ligadura de argumentos. La expresión utilizada como condición de búsqueda debe ser una expresión SQL válida. Si no se proporciona ninguna condición de búsqueda (campo vacío) entonces se supone find('true').

## Valores devueltos

Un objeto CollectionFind para verificar la operación, o recuperar los documentos encontrados.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::find`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$collection->add('{"name": "Alfred",     "age": 18, "job": "Butler"}')->execute();
$collection->add('{"name": "Bob",        "age": 19, "job": "Swimmer"}')->execute();
$collection->add('{"name": "Fred",       "age": 20, "job": "Construction"}')->execute();
$collection->add('{"name": "Wilma",      "age": 21, "job": "Teacher"}')->execute();
$collection->add('{"name": "Suki",       "age": 22, "job": "Teacher"}')->execute();

$find   = $collection->find('job LIKE :job AND age > :age');
$result = $find
  ->bind(['job' => 'Teacher', 'age' => 20])
  ->sort('age DESC')
  ->limit(2)
  ->execute();

print_r($result->fetchAll());
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [_id] => 00005b6b536100000000000000a8
                [age] => 22
                [job] => Teacher
                [name] => Suki
            )
        [1] => Array
            (
                [_id] => 00005b6b536100000000000000a7
                [age] => 21
                [job] => Teacher
                [name] => Wilma
            )
    )
