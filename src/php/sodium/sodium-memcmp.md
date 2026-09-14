---
title: sodium_memcmp
description: Prueba la igualdad en tiempo constante
source_url: https://www.php.net/manual/es/function.sodium-memcmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-memcmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 77020
---

sodium_memcmp

Prueba la igualdad en tiempo constante

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] sodium_memcmp(string $string1, string $string2): int
```php

Compara dos strings en tiempo constante.

En la práctica, casi siempre se desea utilizar `hash_equals` en su lugar, ya que proporciona la misma lógica pero devuelve un `bool` en lugar de un `int`. Sin embargo, si se utiliza el valor de retorno de una comparación en un cálculo que es sensible al tiempo, y se teme que las conversiones bool-to-int provoquen fugas de tiempo, `sodium_memcmp` es un reemplazo ideal.

## Parámetros

`string1`  
La string a comparar

`string2`  
La otra string a comparar

## Valores devueltos

Devuelve `0` si las dos strings son iguales; `-1` en caso contrario.
