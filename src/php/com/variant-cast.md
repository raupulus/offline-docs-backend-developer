---
title: variant_cast
description: Convierte un variant en un nuevo objeto variant de tipo diferente
source_url: https://www.php.net/manual/es/function.variant-cast.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-cast.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 89ae180a8
order: 7770
---

variant_cast

Convierte un variant en un nuevo objeto variant de tipo diferente

## Descripción

```php
variant_cast(variant $variant, int $type): variant
```php

Esta función crea una copia de `variant` y realiza entonces una conversión para forzar la copia a tener el tipo dado por `type`.

Esta función es en realidad la función VariantChangeType() de la biblioteca COM; consulte MSDN para más información.

## Parámetros

`variant`  
El variant.

`type`  
`type` debe ser un tipo entre las constantes `VT_*`.

## Valores devueltos

Devuelve un variant del `type` proporcionado.

## Véase también

`variant_set_type`
