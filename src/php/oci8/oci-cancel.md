---
title: oci_cancel
description: Cancela la lectura del cursor
source_url: https://www.php.net/manual/es/function.oci-cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 57200
---

oci_cancel

Cancela la lectura del cursor

## Descripción

```php
oci_cancel(resource $statement): bool
```php

Invalida un cursor, liberando todos los recursos asociados y cancela la capacidad para leer desde él.

## Parámetros

`statement`  
Una sentencia de OCI.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
