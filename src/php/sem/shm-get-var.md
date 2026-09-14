---
title: shm_get_var
description: Lee una variable en la memoria compartida
source_url: https://www.php.net/manual/es/function.shm-get-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-get-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73580
---

shm_get_var

Lee una variable en la memoria compartida

## Descripción

```php
shm_get_var(SysvSharedMemory $shm, int $key): mixed
```php

`shm_get_var` devuelve la variable identificada por `variable_key`, en el segmento de memoria compartida identificado por `shm_identifier`. La variable siempre está presente en la memoria compartida.

## Parámetros

`shm`  
Un segmento de memoria compartida obtenido desde `shm_attach`.

`key`  
La clave de la variable.

## Valores devueltos

Devuelve la variable correspondiente a la clave dada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shm` ahora requiere una instancia de `SysvSharedMemory` en lugar de un `resource`. |

## Véase también

shm_has_var

shm_put_var
