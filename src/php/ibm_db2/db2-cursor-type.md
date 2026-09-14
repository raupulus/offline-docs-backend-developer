---
title: db2_cursor_type
description: Devuelve el tipo de cursor utilizado por un recurso
source_url: https://www.php.net/manual/es/function.db2-cursor-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-cursor-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30720
---

db2_cursor_type

Devuelve el tipo de cursor utilizado por un recurso

## Descripción

```php
db2_cursor_type(resource $stmt): int
```php

Devuelve el tipo de cursor utilizado por un recurso. Utilice esta función para determinar si se trabaja con un cursor de avance solo o un cursor flotante.

## Parámetros

`stmt`  
Un recurso válido.

## Valores devueltos

Devuelve `DB2_FORWARD_ONLY` si el recurso utiliza un cursor de avance solo o `DB2_SCROLLABLE` si el recurso utiliza un cursor flotante.

## Véase también

db2_prepare
