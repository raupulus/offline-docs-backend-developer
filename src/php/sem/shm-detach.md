---
title: shm_detach
description: Libera un segmento de memoria compartida
source_url: https://www.php.net/manual/es/function.shm-detach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-detach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: 5b7646656
order: 73570
---

shm_detach

Libera un segmento de memoria compartida

## Descripción

```php
shm_detach(SysvSharedMemory $shm): true
```php

`shm_detach` libera el segmento de memoria compartida identificado por `shm` y creado por `shm_attach`. No se olvide que esta memoria compartida sigue existiendo en Unix, y que los datos siguen siendo accesibles.

## Parámetros

`shm`  
Un segmento de memoria compartida obtenido desde `shm_attach`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El tipo de retorno es ahora `true`; anteriormente, era `bool`. |
| 8.0.0 | `shm` ahora requiere una instancia de `SysvSharedMemory` en lugar de un `resource`. |

## Véase también

shm_attach

shm_remove

shm_remove_var
