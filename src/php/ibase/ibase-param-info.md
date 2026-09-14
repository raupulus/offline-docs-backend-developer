---
title: ibase_param_info
description: Devuelve información sobre un argumento en una consulta preparada iBase
source_url: https://www.php.net/manual/es/function.ibase-param-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-param-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30450
---

ibase_param_info

Devuelve información sobre un argumento en una consulta preparada iBase

## Descripción

```php
ibase_param_info(resource $query, int $param_number): array
```php

Devuelve un array con información sobre un argumento después de que una consulta haya sido preparada.

## Parámetros

`query`  
Un gestor de consulta preparada InterBase.

`param_number`  
La posición del argumento.

## Valores devueltos

Devuelve un array que contiene las siguientes claves: `name`, `alias`, `relation`, `length` y `type`.

## Véase también

ibase_field_info

ibase_num_params
