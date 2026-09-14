---
title: db2_stmt_errormsg
description: Devuelve el último mensaje de error de una consulta SQL
source_url: https://www.php.net/manual/es/function.db2-stmt-errormsg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-stmt-errormsg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31100
---

db2_stmt_errormsg

Devuelve el último mensaje de error de una consulta SQL

## Descripción

```php
db2_stmt_errormsg([resource $stmt]): string
```php

Devuelve el último mensaje de error de una consulta SQL.

Si no se pasa un recurso como argumento a la función `db2_stmt_errormsg`, devolverá el mensaje de error asociado con el último intento de retorno de una consulta SQL, por ejemplo, proveniente de `db2_prepare` o `db2_exec`.

## Parámetros

`stmt`  
Un recurso válido.

## Valores devueltos

Devuelve un string que contiene el error del mensaje y el SQLCODE para el último error que se produjo tras la ejecución de una consulta SQL.

## Véase también

db2_conn_error

db2_conn_errormsg

db2_stmt_error
