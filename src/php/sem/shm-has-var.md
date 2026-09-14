---
title: shm_has_var
description: Verifica si una variable existe en memoria compartida
source_url: https://www.php.net/manual/es/function.shm-has-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-has-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73590
---

shm_has_var

Verifica si una variable existe en memoria compartida

## Descripción

```php
shm_has_var(SysvSharedMemory $shm, int $key): bool
```php

Verifica si una variable existe en memoria compartida.

## Parámetros

`shm`  
Un segmento de memoria compartida obtenido desde `shm_attach`.

`key`  
El nombre de la variable.

## Valores devueltos

Devuelve `true` si la variable existe, y `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shm` ahora requiere una instancia de `SysvSharedMemory`; anteriormente se esperaba un `resource`. |

## Véase también

shm_get_var

shm_put_var
