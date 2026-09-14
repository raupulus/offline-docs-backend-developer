---
title: variant_date_from_timestamp
description: Devuelve una representación de fecha en variant de un timestamp Unix
source_url: https://www.php.net/manual/es/function.variant-date-from-timestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-date-from-timestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 7800
---

variant_date_from_timestamp

Devuelve una representación de fecha en variant de un timestamp Unix

## Descripción

```php
variant_date_from_timestamp(int $timestamp): variant
```php

Convierte `timestamp` desde un timestamp Unix al tipo variant `VT_DATE`. Esto permite una interoperabilidad más fácil entre los sistemas Unix de PHP y COM.

## Parámetros

`timestamp`  
Un timestamp Unix.

## Valores devueltos

Devuelve un variant `VT_DATE`.

## Véase también

`variant_date_to_timestamp`, `mktime`, `time`
