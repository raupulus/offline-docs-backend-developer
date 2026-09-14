---
title: hash_update_file
description: Se añaden datos en un contexto de hash activo a partir de un fichero
source_url: https://www.php.net/manual/es/function.hash-update-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-update-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: a027e69cf
order: 29340
---

hash_update_file

Se añaden datos en un contexto de hash activo a partir de un fichero

## Descripción

```php
hash_update_file(HashContext $context, string $filename, [resource $stream_context]): bool
```php

## Parámetros

`context`  
Contexto de hash devuelto por `hash_init`.

`filename`  
URL que indica la ubicación del fichero que será hasheado; admite las envolturas `fopen`.

`stream_context`  
Contexto de flujo devuelto por `stream_context_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                      |
|---------|--------------------------------------------------|
| 8.0.0   | `stream_context` ahora es nullable.              |
| 7.2.0   | Acepta una `HashContext` en lugar de un recurso. |

## Véase también

`hash_init`, `hash_update`, `hash_update_stream`, `hash_final`, `hash_file`
