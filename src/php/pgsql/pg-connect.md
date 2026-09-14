---
title: pg_connect
description: Establece una conexión PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 62910
---

pg_connect

Establece una conexión PostgreSQL

## Descripción

```php
pg_connect(string $connection_string, [int $flags]): PgSql\Connection
```php

`pg_connect` abre una conexión a una base de datos PostgreSQL mediante la cadena de conexión `connection_string`.

Si se realiza una segunda llamada a `pg_connect` con los mismos argumentos, no se establecerá una nueva conexión a menos que se pase `PGSQL_CONNECT_FORCE_NEW` a `flags`, pero se devolverá la conexión anterior.

La antigua sintaxis `$conn = pg_connect("host", "port", "options", "tty", "dbname")` está obsoleta.

## Parámetros

`connection_string`  
La cadena `connection_string` puede estar vacía para utilizar todos los parámetros por omisión o puede contener uno o varios parámetros de configuración separados por espacios. Cada parámetro de configuración tiene la forma `code = valor`. Los espacios alrededor del signo igual son opcionales. Para escribir un valor vacío o un valor que contenga espacios, rodee este valor con comillas simples, por ejemplo: `code = 'un valor'`. Las comillas simples y las barras invertidas dentro del valor deben escapar con una barra invertida, es decir \\ y \\.

Las palabras clave actualmente reconocidas son : `host`, `hostaddr`, `port`, `dbname` (valor por omisión: `user`), `user`, `password`, `connect_timeout`, `options`, `tty` (ignorado), `sslmode`, `requiressl` (obsoleto, utilice `sslmode`) y `service`. La lista de estos argumentos depende de la versión del servidor PostgreSQL.

El parámetro `options` puede utilizarse para pasar parámetros para la línea de comandos que invoca al servidor.

`flags`  
Si `PGSQL_CONNECT_FORCE_NEW` se pasa como argumento, entonces se creará una nueva conexión, incluso si la cadena `connection_string` es idéntica a la de la conexión existente.

Si `PGSQL_CONNECT_ASYNC` se proporciona, la conexión se establecerá de forma asíncrona. El estado de la conexión puede verificarse mediante la función `pg_connect_poll` o mediante la función `pg_connection_status`.

## Valores devueltos

Devuelve una instancia de `PgSql\Connection` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Connection` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `pg_connect`

```
<?php
$dbconn = pg_connect("dbname=marie");
// conexión a una base de datos llamada "marie"

$dbconn2 = pg_connect("host=localhost port=5432 dbname=marie");
// conexión a una base de datos llamada "marie" en el host "localhost" en el puerto "5432"

$dbconn3 = pg_connect("host=mouton port=5432 dbname=marie user=agneau password=foo");
// conexión a una base de datos llamada "marie" en el host "mouton" con un
// nombre de usuario y una contraseña

$conn_string = "host=mouton port=5432 dbname=test user=agneau password=bar";
$dbconn4 = pg_connect($conn_string);
// conexión a una base de datos llamada "test" en el host "mouton" con un
// nombre de usuario y una contraseña

$dbconn5 = pg_connect("host=localhost options='--client_encoding=UTF8'");
//conexión a la base en "localhost" y paso de un parámetro de la línea de
// comandos relacionado con la codificación UTF-8
?>

    
```php

## Véase también

`pg_pconnect`, `pg_close`, `pg_host`, `pg_port`, `pg_tty`, `pg_options`, `pg_dbname`
