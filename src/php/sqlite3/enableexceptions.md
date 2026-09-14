---
title: SQLite3::enableExceptions
description: Activa el lanzamiento de excepciones
source_url: https://www.php.net/manual/es/sqlite3.enableexceptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/enableExceptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: cf116cb47
order: 85700
---

SQLite3::enableExceptions

Activa el lanzamiento de excepciones

## Descripción

```php
public SQLite3::enableExceptions([bool $enable]): bool
```php

Controla si la instancia `SQLite3` lanzará excepciones o advertencias en caso de error.

## Parámetros

`enable`  
Si `true`, la instancia `SQLite3`, y las instancias derivadas de `SQLite3Stmt` y `SQLite3Result`, lanzarán excepciones en caso de errores.

Si `false`, la instancia `SQLite3`, y las instancias derivadas de `SQLite3Stmt` y `SQLite3Result`, lanzarán advertencias en caso de errores.

Para cada uno de los modos, el código y mensaje de error, si los hay, estarán disponibles gracias a SQLite3::lastErrorCode y SQLite3::lastErrorMsg respectivamente.

## Valores devueltos

Devuelve el valor anterior; `true` si las excepciones estaban activadas, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Llamar a SQLite3::enableExceptions con `enable` a `false` desencadenará una advertencia `E_DEPRECATED`. |

## Ejemplos

Ejemplo con SQLite3::enableExceptions

```
<?php
$sqlite = new SQLite3(':memory:');
try {
    $sqlite->exec('create table foo');
    $sqlite->enableExceptions(true);
    $sqlite->exec('create table bar');
} catch (Exception $e) {
    echo 'Caught exception: ' . $e->getMessage();
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

```
Warning: SQLite3::exec(): near "foo": syntax error in example.php on line 4
Caught exception: near "bar": syntax error

   
```php
