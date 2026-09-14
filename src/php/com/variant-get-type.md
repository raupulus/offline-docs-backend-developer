---
title: variant_get_type
description: Devuelve el tipo de un objeto variant
source_url: https://www.php.net/manual/es/function.variant-get-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-get-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 89ae180a8
order: 7850
---

variant_get_type

Devuelve el tipo de un objeto variant

## Descripción

```php
variant_get_type(variant $variant): int
```php

Devuelve el tipo de un objeto variant.

## Parámetros

`variant`  
El objeto variant.

## Valores devueltos

Devuelve un valor entero que indica el tipo de `variant`, que puede ser una instancia de [???](#class.com), [???](#class.dotnet) o de [???](#class.variant). El valor de retorno puede ser comparado a una de las constantes `VT_*`.

El valor de retorno para los objetos COM y DOTNET será la mayoría de las veces `VT_DISPATCH`; la única razón por la que esta función funciona con estas clases es que COM y DOTNET son descendientes de VARIANT.

## Véase también

`variant_set_type`
