---
title: pg_transaction_status
description: Retorna el estado de la transacción en curso del servidor
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-transaction-status.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63760
---

pg_transaction_status

Retorna el estado de la transacción en curso del servidor

## Descripción

```php
pg_transaction_status(PgSql\Connection $connection): int
```php

Retorna el estado de la transacción en curso del servidor.

> [!CAUTION]
> `pg_transaction_status` proporcionará resultados incorrectos cuando se utilice con un servidor PostgreSQL 7.3 que tenga el parámetro `autocommit` desactivado. La funcionalidad de autocommit está obsoleta y ya no existe en las versiones más recientes del servidor.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

## Valores devueltos

El estado puede ser `PGSQL_TRANSACTION_IDLE` (actualmente inactivo), `PGSQL_TRANSACTION_ACTIVE` (una orden está en curso), `PGSQL_TRANSACTION_INTRANS` (inactivo, dentro de un bloque de transacción válido), o `PGSQL_TRANSACTION_INERROR` (inactivo, dentro de un bloque de transacción fallido). `PGSQL_TRANSACTION_UNKNOWN` se retorna si la conexión es incorrecta. `PGSQL_TRANSACTION_ACTIVE` se retorna solo si la consulta ha sido enviada al servidor y esta aún no ha sido completada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `connection` ahora espera una instancia de `PgSql\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_transaction_status`

```
<?php
  $dbconn = pg_connect("dbname=publisher") or die("Conexión imposible");
  $stat = pg_transaction_status($dbconn);
  if ($stat === PGSQL_TRANSACTION_UNKNOWN) {
      echo 'Conexión incorrecta';
  } else if ($stat === PGSQL_TRANSACTION_IDLE) {
      echo 'Conexión actualmente inactiva';
  } else {
      echo 'Conexión está en curso de transacción';
  }
?>

    
```php
