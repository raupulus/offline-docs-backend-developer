---
title: mysqli_get_links_stats
description: Devuelve información sobre los enlaces abiertos y almacenados en caché
source_url: https://www.php.net/manual/es/function.mysqli-get-links-stats.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/functions/mysqli-get-links-stats.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54850
---

mysqli_get_links_stats

Devuelve información sobre los enlaces abiertos y almacenados en caché

## Descripción

```php
mysqli_get_links_stats(): array
```php

La función `mysqli_get_links_stats` devuelve información sobre los enlaces MySQL abiertos y almacenados en caché.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La función `mysqli_get_links_stats` devuelve un array asociativo que contiene tres elementos, cuyas claves son las siguientes:

`total`  
Un `int` que indica el número total de enlaces abiertos, independientemente de su estado.

`active_plinks`  
Un `int` que representa el número de conexiones persistentes activas.

`cached_plinks`  
Un `int` que representa el número de conexiones persistentes inactivas.
