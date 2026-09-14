---
title: hash_update
description: Añade datos en el contexto de hash activo
source_url: https://www.php.net/manual/es/function.hash-update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: 4c852f20e
order: 29360
---

hash_update

Añade datos en el contexto de hash activo

## Descripción

```php
hash_update(HashContext $context, string $data): true
```php

## Parámetros

`context`  
Contexto de hash devuelto por `hash_init`.

`data`  
Mensaje que será incluido en la huella de hash.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                               |
|---------|-----------------------------------------------------------|
| 8.4.0   | Posee ahora un tipo de retorno `true` en lugar de `bool`. |
| 7.2.0   | Acepta una `HashContext` en lugar de un recurso.          |

## Véase también

`hash_init`, `hash_update_file`, `hash_update_stream`, `hash_final`
