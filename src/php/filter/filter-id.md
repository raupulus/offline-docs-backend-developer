---
title: filter_id
description: Devuelve el ID del filtro al que pertenece un filtro con nombre
source_url: https://www.php.net/manual/es/function.filter-id.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-id.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: 627f933cf
order: 24180
---

filter_id

Devuelve el ID del filtro al que pertenece un filtro con nombre

## Descripción

```php
filter_id(string $name): int
```php

## Parámetros

`name`  
Nombre del filtro a obtener el ID.

## Valores devueltos

ID del filtro en caso de éxito o `false` si el filtro no existe.

## Véase también

filter_list
