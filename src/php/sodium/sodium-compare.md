---
title: sodium_compare
description: Comparar grandes números
source_url: https://www.php.net/manual/es/function.sodium-compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76000
---

sodium_compare

Comparar grandes números

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_compare(string $string1, string $string2): int
```php

Compara dos strings como si fueran enteros no signados de longitud arbitraria, en bytes de orden bajo, sin fuga de canal secundario.

## Parámetros

`string1`  
Operando izquierdo

`string2`  
Operando derecho

## Valores devueltos

Devuelve `-1` si `string1` es más pequeño que `string2`.

Devuelve `1` si `string1` es más grande que `string2`.

Devuelve `0` si las dos strings son iguales.
