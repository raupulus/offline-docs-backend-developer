---
title: SQLite3::createFunction
description: Registra una función PHP para su uso como función escalar SQL
source_url: https://www.php.net/manual/es/sqlite3.createfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/createfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: f27cfeeef
order: 85690
---

SQLite3::createFunction

Registra una función PHP para su uso como función escalar SQL

## Descripción

```php
public SQLite3::createFunction(string $name, callable $callback, [int $argCount], [int $flags]): bool
```php

Registra una función PHP o una función de usuario para su uso como función escalar SQL, para su utilización en las consultas SQL.

## Parámetros

`name`  
Nombre de la función SQL a crear o redefinir.

`callback`  
El nombre de la función PHP o la función de usuario a aplicar como callback, definiendo el comportamiento de la función SQL.

Esta función debe ser definida como:

```php
callback(mixed $value, mixed ...$values): mixed
```

`value`  
El primer argumento a pasar a la función SQL.

`values`  
Argumentos adicionales a pasar a la función SQL.

`argCount`  
Número de argumentos que la función SQL acepta. Si este parámetro es `-1`, la función SQL puede aceptar cualquier número de argumentos.

`flags`  
Una conjunción de operaciones a nivel de bits de indicadores. Actualmente, solo `SQLITE3_DETERMINISTIC` es soportado, lo cual especifica que la función devuelve siempre el mismo resultado dado los mismos argumentos en una sola instrucción SQL.

## Valores devueltos

Devuelve `true` si la función fue creada con éxito, `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                       |
|---------|-----------------------------------|
| 7.1.4   | El parámetro `flags` fue añadido. |

## Ejemplos

Ejemplo con `SQLite3::createFunction`

```php
<?php
function my_udf_md5($string) {
    return hash('md5', $string);
}

$db = new SQLite3('mysqlitedb.db');
$db->createFunction('my_udf_md5', 'my_udf_md5');

var_dump($db->querySingle('SELECT my_udf_md5("test")'));
?>

    
```

Resultado del ejemplo anterior es similar a:

    string(32) "098f6bcd4621d373cade4e832627b4f6"
