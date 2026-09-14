---
title: Pdo\Pgsql::copyToArray
description: Copia datos de una tabla a un array PHP
source_url: https://www.php.net/manual/es/pdo-pgsql.copytoarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/copytoarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 858400b07
order: 62510
---

Pdo\Pgsql::copyToArray

Copia datos de una tabla a un array PHP

## Descripción

```php
public Pdo\Pgsql::copyToArray(string $tableName, [string $separator], [string $nullAs], [string $fields]): array
```php

Copia datos de `tableName` a un array utilizando `separator` como delimitador de campos y la lista `fields`.

## Parámetros

`fields`  
La lista de campos a exportar.

## Valores devueltos

Devuelve un array de filas, o `false` si ocurre un error.

## Ejemplos

Ejemplo de Pdo\Pgsql::copyToArray

Cada elemento devuelto es un registro, con los campos unidos por `separator` y un salto de línea final.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');
$db->exec("INSERT INTO fruits VALUES (1, 'apple', 10), (2, 'banana', 20)");

$rows = $db->copyToArray('fruits');
var_export($rows);
?>

   
```php

El ejemplo anterior mostrará:

    array (
      0 => '1   apple   10
    ',
      1 => '2   banana  20
    ',
    )

## Véase también

Pdo\Pgsql::copyFromArray

Pdo\Pgsql::copyFromFile

Pdo\Pgsql::copyToFile
