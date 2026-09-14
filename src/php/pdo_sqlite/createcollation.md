---
title: Pdo\Sqlite::createCollation
description: Registra una función de usuario de ordenación para su uso en las sentencias
  SQL
source_url: https://www.php.net/manual/es/pdo-sqlite.createcollation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlite/pdo/sqlite/createcollation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlite
translation_status: ready
translation_reviewed: true
translation_revision: 51610360d
order: 62720
---

Pdo\Sqlite::createCollation

Registra una función de usuario de ordenación para su uso en las sentencias SQL

## Descripción

```php
public Pdo\Sqlite::createCollation(string $name, callable $callback): bool
```php

Este método es similar a Pdo\Sqlite::createFunction salvo que registra funciones que se utilizan para ordenar strings.

## Parámetros

`name`  
El nombre de la función de ordenación SQL a crear o redefinir.

`callback`  
La retrollamada que define el comportamiento de una ordenación. Debe aceptar dos `string`s y devolver `-1`, `0`, o `1` si el primer string se ordena antes, es idéntico o después del segundo string respectivamente. Una función interna que se comporta de esta manera es `strcmp`.

Esta función debe ser definida como sigue:

```php
collation(string $string1, string $string2): int
```

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de Pdo\Sqlite::createCollation

```php
<?php
$db = new Pdo\Sqlite('sqlite::memory:');
$db->exec("CREATE TABLE test (col1 string)");
$db->exec("INSERT INTO test VALUES ('a1')");
$db->exec("INSERT INTO test VALUES ('a10')");
$db->exec("INSERT INTO test VALUES ('a2')");

$db->sqliteCreateCollation('NATURAL_CMP', 'strnatcmp');
foreach ($db->query("SELECT col1 FROM test ORDER BY col1") as $row) {
  echo $row['col1'] . "\n";
}
echo "\n";
foreach ($db->query("SELECT col1 FROM test ORDER BY col1 COLLATE NATURAL_CMP") as $row) {
  echo $row['col1'] . "\n";
}
?>

   
```

El ejemplo anterior mostrará:

    a1
    a10
    a2

    a1
    a2
    a10

## Véase también

Pdo\Sqlite::createFunction

Pdo\Sqlite::createAggregate

sqlite_create_function

sqlite_create_aggregate
