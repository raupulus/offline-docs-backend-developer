---
title: pg_put_line
description: Envía una string al servidor PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-put-line.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-put-line.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c43a3cd9b
order: 63560
---

pg_put_line

Envía una string al servidor PostgreSQL

## Descripción

```php
pg_put_line([PgSql\Connection $connection], string $query): bool
```php

`pg_put_line` envía una string (terminada por `null`) al servidor PostgreSQL. Esto es necesario en conjunción con un comando `COPY FROM` de PostgreSQL.

`COPY` es una carga muy rápida de datos soportada por PostgreSQL. Los datos se pasan sin ser analizados y en una simple transacción.

Una alternativa en lugar de usar el comando bruto `pg_put_line` es usar `pg_copy_from`. Es una interfaz mucho más simple.

> [!NOTE]
> Tenga en cuenta que la aplicación debe agregar explícitamente los dos caracteres "\\" al final de la string para indicar al servidor que ha terminado de enviar datos, antes de llamar a `pg_end_copy`.

> [!WARNING]
> El uso de `pg_put_line` hace que fallen la mayoría de los objetos de gran tamaño, incluyendo `pg_lo_read` y `pg_lo_tell`. Puede usar `pg_copy_from` y `pg_copy_to` en su lugar.

## Parámetros

`connection`  
Una `PgSql\Connection` instancia. Cuando `connection` no es especificado, se usa la conexión por defecto. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

`query`  
Una línea de texto para enviar directamente al servidor PostgreSQL. Un carácter de finalización `null` se agrega automáticamente.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_put_line`

```
<?php
  $conn = pg_pconnect("dbname=foo");
  pg_query($conn, "create table bar (a int4, b char(16), d float8)");
  pg_query($conn, "copy bar from stdin");
  pg_put_line($conn, "3\tBonjour le monde\t4.5\n");
  pg_put_line($conn, "4\tAurevoir le monde\t7.11\n");
  pg_put_line($conn, "\\.\n");
  pg_end_copy($conn);
?>

    
```php

## Véase también

`pg_end_copy`
