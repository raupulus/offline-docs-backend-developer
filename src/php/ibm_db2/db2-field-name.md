---
title: db2_field_name
description: Devuelve el nombre de la columna del conjunto de resultados
source_url: https://www.php.net/manual/es/function.db2-field-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-field-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30820
---

db2_field_name

Devuelve el nombre de la columna del conjunto de resultados

## Descripción

```php
db2_field_name(resource $stmt, int $column): string
```php

Devuelve el nombre de la columna del conjunto de resultados

## Parámetros

`stmt`  
Especifica el recurso que contiene el conjunto de resultados.

`column`  
Especifica la columna en el conjunto de resultados. Puede ser un entero comenzando en la posición 0 que representa el número de la columna o un string que contiene el nombre de la columna.

## Valores devueltos

Devuelve un string que contiene el nombre de la columna especificada. Si la columna especificada no existe en el conjunto de resultados, `db2_field_name` devuelve `false`.

## Véase también

db2_field_display_size

db2_field_num

db2_field_precision

db2_field_scale

db2_field_type

db2_field_width
