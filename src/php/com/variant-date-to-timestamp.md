---
title: variant_date_to_timestamp
description: Convierte un valor de fecha/hora variante en un timestamp Unix
source_url: https://www.php.net/manual/es/function.variant-date-to-timestamp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-date-to-timestamp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 7810
---

variant_date_to_timestamp

Convierte un valor de fecha/hora variante en un timestamp Unix

## Descripción

```php
variant_date_to_timestamp(variant $variant): int
```php

Convierte `variant` de un valor `VT_DATE` (o similar) en un timestamp Unix. Esto permite la interoperabilidad fácil entre las partes Unix de PHP y COM.

## Parámetros

`variant`  
El variant.

## Valores devueltos

Devuelve un timestamp Unix, o `null` en caso de fallo.

## Véase también

`variant_date_from_timestamp`, `date`, `strftime`
