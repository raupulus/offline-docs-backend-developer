---
title: db2_field_num
description: Devuelve la posición del nombre de la columna del conjunto de resultados
source_url: https://www.php.net/manual/es/function.db2-field-num.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-field-num.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30830
---

db2_field_num

Devuelve la posición del nombre de la columna del conjunto de resultados

## Descripción

```php
db2_field_num(resource $stmt, int $column): int
```php

Devuelve la posición del nombre de la columna del conjunto de resultados

## Parámetros

`stmt`  
Especifica un recurso que contiene un conjunto de resultados.

`column`  
Especifica la columna en el conjunto de resultados. Esto puede ser un entero comenzando en la posición 0 que representa el número de la columna o un string que contiene el nombre de la columna.

## Valores devueltos

Devuelve un entero que contiene la posición comenzando en 0 del nombre de la columna en el conjunto de resultados. Si la columna especificada no existe en el conjunto de resultados, `db2_field_num` devuelve `false`.

## Véase también

db2_field_display_size

db2_field_name

db2_field_precision

db2_field_scale

db2_field_type

db2_field_width
