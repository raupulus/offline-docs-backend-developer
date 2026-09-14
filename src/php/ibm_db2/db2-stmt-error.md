---
title: db2_stmt_error
description: Devuelve un string que contiene el valor de SQLSTATE retornado por una
  consulta SQL
source_url: https://www.php.net/manual/es/function.db2-stmt-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-stmt-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31090
---

db2_stmt_error

Devuelve un string que contiene el valor de SQLSTATE retornado por una consulta SQL

## Descripción

```php
db2_stmt_error([resource $stmt]): string
```php

Devuelve un string que contiene el valor de SQLSTATE retornado por una consulta SQL.

Si no se pasa un recurso como argumento a la función `db2_stmt_error`, esta retornará el mensaje de error asociado con el último intento de retorno de una consulta SQL, por ejemplo, proveniente de `db2_prepare` o `db2_exec`.

Para comprender los valores de SQLSTATE, se puede ingresar el siguiente comando en el procesador de línea de comandos de DB2: `db2 '? sqlstate-value'`. Asimismo, se puede llamar a la función `db2_conn_errormsg` para obtener un mensaje de error explícito junto con el valor de SQLCODE asociado.

## Parámetros

`stmt`  
Un recurso válido.

## Valores devueltos

Devuelve un string que contiene el valor de SQLSTATE.

## Véase también

db2_conn_error

db2_conn_errormsg

db2_stmt_errormsg
