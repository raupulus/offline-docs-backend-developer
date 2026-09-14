---
title: shm_attach
description: Crea o abre un segmento de memoria compartida
source_url: https://www.php.net/manual/es/function.shm-attach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sem/functions/shm-attach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sem
translation_status: ready
translation_revision: fd2f14b2e
order: 73560
---

shm_attach

Crea o abre un segmento de memoria compartida

## Descripción

```php
shm_attach(int $key, [int $size], [int $permissions]): SysvSharedMemory
```php

`shm_attach` devuelve una instancia que permitirá acceder a la memoria compartida de tipo System V. En la primera llamada, la memoria será creada, con el tamaño `size` y con los permisos `permissions`

En las llamadas siguientes con la misma clave `key`, `shm_attach` devolverá una nueva instancia, pero esta instancia accederá siempre a la misma porción de memoria compartida. En este caso, `size` y `permissions` serán ignorados.

## Parámetros

`key`  
Un identificador numérico de la memoria compartida

`size`  
El tamaño de la memoria. Si no se proporciona, por defecto valdrá el valor de `sysvshm.init_mem` del fichero `php.ini`, de lo contrario 10000 bytes.

`permissions`  
Los permisos (opcionales). Por defecto, valen 0666.

## Valores devueltos

Devuelve una instancia de `SysvSharedMemory` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve una instancia de `SysvSharedMemory` ahora; anteriormente; un `resource` era devuelto. |
| 8.0.0 | `size` es ahora nullable. |

## Véase también

shm_detach

ftok
