---
title: RowResult::getColumns
description: Devuelve los metadatos de las columnas
source_url: https://www.php.net/manual/es/mysql-xdevapi-rowresult.getcolumns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/rowresult/getcolumns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 286ab7c12
order: 53830
---

RowResult::getColumns

Devuelve los metadatos de las columnas

## Descripción

```php
public mysql_xdevapi\RowResult::getColumns(): array
```php

Devuelve los metadatos de las columnas presentes en el conjunto de resultados.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array de FieldMetadata que representa las columnas del resultado, o un array vacío si el conjunto de resultados está vacío.

## Ejemplos

Ejemplo de `mysql_xdevapi\RowResult::getColumns`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$session->sql("DROP DATABASE addressbook")->execute();
$session->sql("CREATE DATABASE foo")->execute();
$session->sql("CREATE TABLE foo.test_table(x int)")->execute();
$session->sql("INSERT INTO addressbook.names values ('John', 42), ('Sam', 33)")->execute();

$sql = $session->sql("SELECT * from addressbook.names")->execute();

$cols = $sql->getColumns();

print_r($cols);

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => mysql_xdevapi\FieldMetadata Object
            (
                [type] => 7
                [type_name] => BYTES
                [name] => name
                [original_name] => name
                [table] => names
                [original_table] => names
                [schema] => addressbook
                [catalog] => def
                [collation] => 255
                [fractional_digits] => 0
                [length] => 65535
                [flags] => 0
                [content_type] => 0
            )
        [1] => mysql_xdevapi\FieldMetadata Object
            (
                [type] => 1
                [type_name] => SINT
                [name] => age
                [original_name] => age
                [table] => names
                [original_table] => names
                [schema] => addressbook
                [catalog] => def
                [collation] => 0
                [fractional_digits] => 0
                [length] => 11
                [flags] => 0
                [content_type] => 0
            )
    )
