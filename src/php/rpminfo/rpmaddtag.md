---
title: rpmaddtag
description: Añade un tag recuperado en una consulta
source_url: https://www.php.net/manual/es/function.rpmaddtag.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmaddtag.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72430
---

rpmaddtag

Añade un tag recuperado en una consulta

## Descripción

```php
rpmaddtag(int $tag): bool
```php

Añade un tag recuperado en una consulta previa.

## Parámetros

`tag`  
Una de las constantes `RPMTAG_*`, ver la página de las [constantes rpminfo](#rpminfo.constants).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

rpminfo

rpmdbinfo

rpmdbsearch
