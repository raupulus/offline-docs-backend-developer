---
title: oci_free_statement
description: Libera todos los recursos asociados con una sentencia o cursor
source_url: https://www.php.net/manual/es/function.oci-free-statement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-free-statement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 57420
---

oci_free_statement

Libera todos los recursos asociados con una sentencia o cursor

## Descripción

```php
oci_free_statement(resource $statement): bool
```php

Libera los recursos asociados con un cursor o sentencia de Oracle, el cual fue recibido desde una resultado de `oci_parse` u obtenido desde Oracle.

## Parámetros

`statement`  
Un identificador de sentecia válido de OCI.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
