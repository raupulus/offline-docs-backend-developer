---
title: shm_put_var
description: Inserta o modifica una variable en la memoria compartida
source_url: https://www.php.net/manual/es/function.shm-put-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-put-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_reviewed: true
translation_revision: fd2f14b2e
order: 73600
---

shm_put_var

Inserta o modifica una variable en la memoria compartida

## Descripción

```php
shm_put_var(SysvSharedMemory $shm, int $key, mixed $value): bool
```php

`shm_put_var` inserta o modifica la variable `value` con la clave `key` en el segmento de memoria `shm`.

Se emitirán alertas (nivel `E_WARNING`) si `shm` no es un segmento de memoria tipo System V válido, o si no hay suficiente memoria para la solicitud.

## Parámetros

`shm`  
Un segmento de memoria compartida obtenido desde `shm_attach`.

`key`  
La clave de la variable.

`value`  
La variable. Todos los [tipos de variables](#language.types) soportados por la función `serialize` pueden ser utilizados: esto significa que todos los tipos, excepto los recursos y algunos objetos internos, pueden ser serializados.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shm` ahora requiere una instancia de `SysvSharedMemory`; anteriormente, se esperaba un `resource`. |

## Véase también

shm_get_var

shm_has_var
