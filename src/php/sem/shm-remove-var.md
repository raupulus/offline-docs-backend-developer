---
title: shm_remove_var
description: Elimina una variable de la memoria compartida
source_url: https://www.php.net/manual/es/function.shm-remove-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-remove-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73610
---

shm_remove_var

Elimina una variable de la memoria compartida

## Descripción

```php
shm_remove_var(SysvSharedMemory $shm, int $key): bool
```php

Elimina la variable `key` de la memoria compartida `shm` y libera la memoria.

## Parámetros

`shm`  
Un segmento de memoria compartida obtenido desde `shm_attach`.

`key`  
La clave de la variable.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shm` ahora requiere una instancia de `SysvSharedMemory` en lugar de un `resource`. |

## Véase también

shm_remove
