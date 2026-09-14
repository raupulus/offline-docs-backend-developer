---
title: cubrid_lob2_new
description: Crea un nuevo objeto LOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9240
---

cubrid_lob2_new

Crea un nuevo objeto LOB

## Descripción

```php
cubrid_lob2_new([resource $conn_identifier], [string $type]): resource
```php

La función `cubrid_lob2_new` se utiliza para crear un nuevo objeto LOB (tanto BLOB como CLOB). Esta función debe ser utilizada antes de vincular un objeto LOB.

## Parámetros

`conn_identifier`  
Un identificador de conexión. Si no se especifica, se utilizará la última conexión abierta con la función `cubrid_connect` o la función `cubrid_connect_with_url`.

`type`  
Puede ser "BLOB" o "CLOB", y no es sensible a mayúsculas/minúsculas. El valor por omisión es "BLOB".

## Valores devueltos

Un identificador LOB en caso de éxito, o `false` si ocurre un error.

## Véase también

cubrid_lob2_close
