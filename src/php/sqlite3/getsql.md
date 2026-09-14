---
title: SQLite3Stmt::getSQL
description: Recupera el SQL de una declaración
source_url: https://www.php.net/manual/es/sqlite3stmt.getsql.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3stmt/getsql.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: 855bfee2f
order: 86000
---

SQLite3Stmt::getSQL

Recupera el SQL de una declaración

## Descripción

```php
public SQLite3Stmt::getSQL([bool $expand]): string
```php

Recupera el SQL de una declaración preparada. Si `expand` es `false`, se recupera el SQL sin modificar. Si `expand` es `true`, todos los parámetros de la consulta son reemplazados con sus valores vinculados, o con un `NULL` SQL, si no están aún vinculados.

## Parámetros

`expand`  
Si se debe recuperar el código SQL extendido. Pasar `true` solo es soportado a partir de libsqlite 3.14.

## Valores devueltos

Devuelve el SQL de la declaración preparada, o `false` si ocurre un error.

## Errores/Excepciones

Si `expand` es `true`, pero la versión de libsqlite es menor que 3.14, se emite un error de nivel `E_WARNING` o una `Exception`, de acuerdo con SQLite3::enableExceptions.

## Ejemplos

Inspeccionar el SQL extendido

```
<?php
$db = new SQLite3(':memory:');
$stmt = $db->prepare("SELECT :a, ?, :c");
$stmt->bindValue(':a', 'foo');
$answer = 42;
$stmt->bindParam(2, $answer);
var_dump($stmt->getSQL(true));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(24) "SELECT 'foo', '42', NULL"
