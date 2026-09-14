---
title: sodium_add
description: Suma grandes números
source_url: https://www.php.net/manual/es/function.sodium-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 75960
---

sodium_add

Suma grandes números

## Descripción

```php
sodium_add(string $string1, string $string2): void
```php

Esto suma el argumento `string2` a `string1`, sobrescribiendo el valor almacenado en `string1`. Esta función asume que ambos argumentos son strings binarios que representan enteros sin signo en bytes de orden bajo.

## Parámetros

`string1`  
El string que representa un entero sin signo de longitud arbitraria en bytes de orden bajo. Este argumento se pasa por referencia y contendrá la suma de ambos argumentos.

`string2`  
El string que representa un entero sin signo de longitud arbitraria en bytes de orden bajo.

## Valores devueltos

No se retorna ningún valor.
