---
title: shm_remove
description: Elimina un segmento de memoria compartida bajo Unix
source_url: https://www.php.net/manual/es/function.shm-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73620
---

shm_remove

Elimina un segmento de memoria compartida bajo Unix

## Descripción

```php
shm_remove(SysvSharedMemory $shm): bool
```php

`shm_remove` elimina el segmento de memoria compartida `shm`. Todos los datos serán eliminados.

## Parámetros

`shm`  
Un segmento de memoria compartida obtenido desde `shm_attach`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shm` ahora requiere una instancia de `SysvSharedMemory`; anteriormente se esperaba un `resource`. |

## Véase también

shm_remove_var
