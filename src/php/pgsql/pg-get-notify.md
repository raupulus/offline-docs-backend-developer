---
title: pg_get_notify
description: Lee el mensaje SQL NOTIFY
source_url: https://www.php.net/manual/es/function.pg-get-notify.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-get-notify.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: cfeb14a38
order: 63240
---

pg_get_notify

Lee el mensaje SQL NOTIFY

## Descripción

```php
pg_get_notify(PgSql\Connection $connection, [int $mode]): array
```php

`pg_get_notify` recibe el mensaje de NOTIFY enviado por un comando SQL `NOTIFY`. Para leer el mensaje asociado, se debe utilizar el comando `LISTEN`.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`mode`  
Un parámetro opcional que controla cómo el `array` devuelto es indexado. `mode` es una constante que puede tomar los siguientes valores: `PGSQL_ASSOC`, `PGSQL_NUM` y `PGSQL_BOTH`. Usando `PGSQL_NUM`, la función devolverá un array con índices numéricos, usando `PGSQL_ASSOC`, devolverá solo índices asociativos mientras que `PGSQL_BOTH` devolverá ambos índices numéricos y asociativos.

## Valores devueltos

Un `array` que contiene el nombre del mensaje `NOTIFY`. Si el servidor lo soporta, el array contiene también la versión del servidor y la carga útil (payload). De lo contrario, si no hay ningún `NOTIFY` pendiente, se devolverá `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_get_notify`

```
<?php
$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "Se ha producido un error.\n";
  exit;
}

// escucha el mensaje 'author_updated' de otros procesos
pg_query($conn, 'LISTEN author_updated;');
$notify = pg_get_notify($conn);
if (!$notify) {
  echo "Ningún mensaje\n";
} else {
  print_r($notify);
}
?>

    
```php

## Véase también

`pg_get_pid`
