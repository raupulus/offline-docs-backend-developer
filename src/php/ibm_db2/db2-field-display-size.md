---
title: db2_field_display_size
description: Devuelve el máximo de octetos requeridos para mostrar una columna
source_url: https://www.php.net/manual/es/function.db2-field-display-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-field-display-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30810
---

db2_field_display_size

Devuelve el máximo de octetos requeridos para mostrar una columna

## Descripción

```php
db2_field_display_size(resource $stmt, int $column): int
```php

Devuelve el máximo de octetos requeridos para mostrar una columna en un conjunto de resultados.

## Parámetros

`stmt`  
Especifica el recurso que contiene el conjunto de resultados.

`column`  
Especifica la columna en el conjunto de resultados. Puede ser un entero comenzando en la posición 0 que representa el número de la columna o un string que contiene el nombre de la columna.

## Valores devueltos

Devuelve un valor entero con el máximo de octetos requeridos para mostrar la columna especificada. Si la columna no existe en el conjunto de resultados, `db2_field_display_size` devuelve `false`.

## Véase también

db2_field_name

db2_field_num

db2_field_precision

db2_field_scale

db2_field_type

db2_field_width
