---
title: Pdo\Pgsql::escapeIdentifier
description: Escapa una string para su uso como identificador SQL
source_url: https://www.php.net/manual/es/pdo-pgsql.escapeidentifier.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_pgsql/pdo/pgsql/escapeidentifier.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 02b075821
order: 62530
---

Pdo\Pgsql::escapeIdentifier

Escapa una string para su uso como identificador SQL

## Descripción

```php
public Pdo\Pgsql::escapeIdentifier(string $input): string
```php

Escapa una string para su uso como identificador SQL, como una tabla, una columna o un nombre de función. Esto es útil cuando el identificador proporcionado por el usuario podría contener caracteres especiales que no serían interpretados como parte del identificador por el analizador SQL, o cuando el identificador podría contener caracteres en mayúsculas cuya capitalización debería preservarse.

## Parámetros

`input`  
Una `string` que contiene el texto a escapar.

## Valores devueltos

Una `string` que contiene los datos escapados.

## Ejemplos

Ejemplo de Pdo\Pgsql::escapeIdentifier

```
<?php
$pdo = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);

$unescapedTableName = 'UnescapedTableName';
$pdo->exec("CREATE TABLE $unescapedTableName ()");

$escapedTableName = $pdo->escapeIdentifier('EscapedTableName');
$pdo->exec("CREATE TABLE $escapedTableName ()");

$statement = $pdo->query(
  "SELECT relname FROM pg_stat_user_tables WHERE relname ilike '%tablename'"
);

var_export($statement->fetchAll(PDO::FETCH_COLUMN, 0));

$tableNameWithSymbols = 'Table-Name-With-Symbols';
$pdo->exec("CREATE TABLE $tableNameWithSymbols ()");
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array (
      0 => 'unescapedtablename',
      1 => 'EscapedTableName',
    )
    Fatal error: Uncaught PDOException: SQLSTATE[42601]: Syntax error: 7 ERROR:  syntax error at or near "Table"
    LINE 1: CREATE TABLE Table-Name-With-Symbols ()

## Véase también

PDO::quote
