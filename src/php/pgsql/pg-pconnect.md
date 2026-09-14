---
title: pg_pconnect
description: Establece una conexión PostgreSQL persistente
source_url: https://www.php.net/manual/es/function.pg-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: 3b2503bdc
order: 63500
---

pg_pconnect

Establece una conexión PostgreSQL persistente

## Descripción

```php
pg_pconnect(string $connection_string, [int $flags]): PgSql\Connection
```php

`pg_pconnect` devuelve una instancia `PgSql\Connection` de conexión persistente.

Si se realiza una segunda llamada a `pg_pconnect` con el mismo `connection_string` como una conexión existente, se devolverá la conexión existente a menos que se pase `PGSQL_CONNECT_FORCE_NEW` a `flags`.

Para activar las conexiones persistentes, la directiva de configuración [pgsql.allow_persistent](#ini.pgsql.allow-persistent) del `php.ini` debe establecerse en `On` (que es su valor por omisión). El número máximo de conexiones puede limitarse mediante la directiva de configuración [pgsql.max_persistent](#ini.pgsql.max-persistent) en el archivo `php.ini` (por omisión, su valor es `-1`, es decir, sin límite). El número total de conexiones puede configurarse con la directiva [pgsql.max_links](#ini.pgsql.max-links) del archivo `php.ini`.

`pg_close` no cerrará las conexiones persistentes generadas por `pg_pconnect`.

## Parámetros

`connection_string`  
La cadena `connection_string` puede estar vacía para utilizar todos los parámetros por omisión o puede contener uno o varios parámetros de configuración separados por espacios. Cada parámetro de configuración tiene la forma `code = valor`. Los espacios alrededor del signo igual son opcionales. Para escribir un valor vacío o un valor que contenga espacios, rodee este valor con comillas simples, por ejemplo: `code = 'un valor'`. Las comillas simples y las barras invertidas dentro del valor deben escaparse con una barra invertida, es decir `\'` y `\\`.

Las palabras clave actualmente reconocidas son : `host`, `hostaddr`, `port`, `dbname`, `user`, `password`, `connect_timeout`, `options`, `tty` (ignorado), `sslmode`, `requiressl` (obsoleto, utilice `sslmode`) y `service`. La lista de estos argumentos depende de la versión del servidor PostgreSQL.

`flags`  
Si `PGSQL_CONNECT_FORCE_NEW` se pasa como argumento, entonces se creará una nueva conexión, incluso si la cadena `connection_string` es idéntica a la de la conexión existente.

## Valores devueltos

Devuelve una instancia de `PgSql\Connection` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PgSql\Connection` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

Ejemplo con `pg_pconnect`

```
<?php
// conexión a una base de datos llamada "marie"
$dbconn = pg_pconnect("dbname=marie");

// conexión a una base de datos llamada "marie" en el host "localhost" en el puerto "5432"
$dbconn2 = pg_pconnect("host=localhost port=5432 dbname=marie");

// conexión a una base de datos llamada "marie" en el host "mouton" con un
// nombre de usuario y una contraseña
$dk

// conexión a una base de datos llamada "test" en el host "mouton" con un
// nombre de usuario y una contraseña
$conn_string = "host=mouton port=5432 dbname=test user=agneau password=bar";
$dbconn4 = pg_pconnect($conn_string);
?>

    
```php

## Véase también

`pg_connect`, [ Conexiones Persistentes](#features.persistent-connections)
