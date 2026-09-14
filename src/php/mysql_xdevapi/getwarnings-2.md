---
title: DocResult::getWarnings
description: Devuelve los avisos de la última operación
source_url: https://www.php.net/manual/es/mysql-xdevapi-docresult.getwarnings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/docresult/getwarnings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 286ab7c12
order: 53670
---

DocResult::getWarnings

Devuelve los avisos de la última operación

## Descripción

```php
public mysql_xdevapi\DocResult::getWarnings(): Array
```php

Recupera los avisos generados por la última operación del servidor MySQL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de objetos Warning de la última operación. Cada objeto define un 'message' de error, un 'nivel' de error y un 'code' de error. Un array vacío es devuelto si no hay errores presentes.

## Ejemplos

Ejemplo de `mysql_xdevapi\DocResult::getWarnings`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$create->add('{"name": "Alfred", "age": 18, "job": "Butler"}')->execute();
$create->add('{"name": "Reginald", "age": 42, "job": "Butler"}')->execute();

// ...

$collection = $schema->getCollection("people");

// Devuelve un objeto DocResult
$result = $collection
  ->find('job like :job and age > :age')
  ->bind(['job' => 'Butler', 'age' => 16])
  ->sort('age desc')
  ->execute();

if (!$result->getWarningsCount()) {
    echo "Hubo un error:\n";
    print_r($result->getWarnings());
    exit;
}

var_dump($result->fetchOne());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Hubo un error:

    Array
    (
        [0] => mysql_xdevapi\Warning Object
            (
                [message] => Algo malo y así sucesivamente
                [level] => 2
                [code] => 1365
            )
        [1] => mysql_xdevapi\Warning Object
            (
                [message] => Algo malo y así sucesivamente
                [level] => 2
                [code] => 1365
            )
    )
