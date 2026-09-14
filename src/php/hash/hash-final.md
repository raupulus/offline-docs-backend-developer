---
title: hash_final
description: Finaliza un hachaje incremental y devuelve el resultado de la huella
  digital
source_url: https://www.php.net/manual/es/function.hash-final.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-final.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: 20dcfbb0d
order: 29270
---

hash_final

Finaliza un hachaje incremental y devuelve el resultado de la huella digital

## Descripción

```php
hash_final(HashContext $context, [bool $binary]): string
```php

## Parámetros

`context`  
Contexto de hachaje devuelto por `hash_init`.

`binary`  
Cuando es `true`, la salida será datos brutos binarios. Cuando es `false`, la salida será dígitos hexadecimales en minúscula.

## Valores devueltos

Devuelve una cadena de caracteres que contiene la huella digital calculada en dígitos hexadecimales en minúscula a menos que `binary` esté fijado a `true`. En este caso, se devuelve la representación bruta binaria de la huella digital.

## Historial de cambios

| Versión | Descripción                                      |
|---------|--------------------------------------------------|
| 7.2.0   | Acepta una `HashContext` en lugar de un recurso. |

## Véase también

`hash_init`, `hash_update`, `hash_update_stream`, `hash_update_file`
