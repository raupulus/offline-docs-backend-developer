---
title: ibase_num_params
description: Devuelve el número de parámetros en una consulta preparada iBase
source_url: https://www.php.net/manual/es/function.ibase-num-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-num-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30440
---

ibase_num_params

Devuelve el número de parámetros en una consulta preparada iBase

## Descripción

```php
ibase_num_params(resource $query): int
```php

`ibase_num_params` devuelve el número de parámetros en la consulta especificada por `query`. Es el número de argumentos de sustitución que deben estar presentes al llamar a `ibase_execute`.

## Parámetros

`query`  
La consulta preparada.

## Valores devueltos

Devuelve el número de parámetros, en forma de un `int`.

## Véase también

ibase_prepare

ibase_param_info
