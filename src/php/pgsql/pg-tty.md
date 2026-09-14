---
title: pg_tty
description: Devuelve el nombre de TTY asociado a la conexión
source_url: https://www.php.net/manual/es/function.pg-tty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-tty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63770
---

pg_tty

Devuelve el nombre de TTY asociado a la conexión

## Descripción

```php
pg_tty([PgSql\Connection $connection]): string
```php

`pg_tty` devuelve el nombre de TTY de la conexión asociada a `connection`.

> [!NOTE]
> `pg_tty` está obsoleto, ya que el servidor no presta atención a la configuración TTY, pero se mantiene por razones de compatibilidad.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`. Cuando `connection` es `null`, se usa la conexión predeterminada. La conexión predeterminada es la última conexión hecha por `pg_connect` o `pg_pconnect`

> [!WARNING]
> Desde PHP 8.1.0, usar la conexión predeterminada está obsoleto.

## Valores devueltos

Una `string` que contiene el depurador TTY de la conexión `connection`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `connection` ahora es nullable. |

## Ejemplos

Ejemplo con `pg_tty`

```
<?php
$pgsql_conn = pg_connect("dbname=mark host=localhost");

if ($pgsql_conn) {
   print "Depurador TTY del servidor es: " . pg_tty($pgsql_conn) . "<br/>\n";
} else {
   print pg_last_error($pgsql_conn);
   exit;
}
?>

    
```php
