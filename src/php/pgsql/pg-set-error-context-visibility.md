---
title: pg_set_error_context_visibility
description: Determina la visibilidad de los mensajes de error de contexto devueltos
  por pg_last_error y pg_result_error
source_url: https://www.php.net/manual/es/function.pg-set-error-context-visibility.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-set-error-context-visibility.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: ebd624e43
order: 63710
---

pg_set_error_context_visibility

Determina la visibilidad de los mensajes de error de contexto devueltos por

pg_last_error

y

pg_result_error

## Descripción

```php
pg_set_error_context_visibility(PgSql\Connection $connection, int $visibility): int
```php

Determina la visibilidad de los mensajes de error de contexto devueltos por `pg_last_error` y `pg_result_error`

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`visibility`  
La visibilidad requerida: `PGSQL_SHOW_CONTEXT_NEVER`, `PGSQL_SHOW_CONTEXT_ERRORS` o `PGSQL_SHOW_CONTEXT_ALWAYS`.

## Valores devueltos

El nivel de visibilidad anterior: `PGSQL_SHOW_CONTEXT_NEVER`, `PGSQL_SHOW_CONTEXT_ERRORS` o `PGSQL_SHOW_CONTEXT_ALWAYS`.

## Ejemplos

Ejemplo de `pg_set_error_context_visibility`

```
      
      <?php
      $dbconn = pg_connect("dbname=publisher") or die("No se puede conectar");
      if (!pg_connection_busy($dbconn)) {
      pg_send_query($dbconn, "select * from doesnotexist;");
      }
      pg_set_error_context_visibility($dbconn, PGSQL_SHOW_CONTEXT_ALWAYS);
      $res1 = pg_get_result($dbconn);
      echo pg_result_error($res1);
      ?>
      
     
```php

## Véase también

`pg_last_error`, `pg_result_error`
