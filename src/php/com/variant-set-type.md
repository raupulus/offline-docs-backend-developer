---
title: variant_set_type
description: Convierte un variant en otro tipo "in situ"
source_url: https://www.php.net/manual/es/function.variant-set-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-set-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 2b220300c
order: 7960
---

variant_set_type

Convierte un variant en otro tipo "in situ"

## Descripción

```php
variant_set_type(variant $variant, int $type): void
```php

Esta función es similar a `variant_cast` excepto que el variant es modificado "in situ"; no se crea ningún nuevo variant. Los argumentos de esta función tienen el mismo significado que los de `variant_cast`.

## Parámetros

`variant`  
El variant.

`type`  

## Valores devueltos

No se retorna ningún valor.

## Véase también

`variant_cast`, `variant_get_type`
