---
title: shmop_delete
description: Destruye un bloque de memoria compartida
source_url: https://www.php.net/manual/es/function.shmop-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/shmop/functions/shmop-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: shmop
translation_status: ready
translation_reviewed: true
translation_revision: 41d34439e
order: 74210
---

shmop_delete

Destruye un bloque de memoria compartida

## Descripción

```php
shmop_delete(Shmop $shmop): bool
```php

`shmop_delete` se utiliza para destruir un bloque de memoria compartida.

## Parámetros

`shmop`  
El recurso de memoria compartida creado por `shmop_open`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `shmop` ahora requiere una instancia de `Shmop`; anteriormente se esperaba un `resource`. |

## Ejemplos

Eliminación de un bloque de memoria compartida

```
<?php
shmop_delete($shm_id);
?>

   
```php

Este ejemplo elimina el bloque de memoria compartida identificado por `$shm_id`.
