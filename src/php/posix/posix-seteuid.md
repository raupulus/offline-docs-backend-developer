---
title: posix_seteuid
description: Establecer el UID efectivo del proceso actual
source_url: https://www.php.net/manual/es/function.posix-seteuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-seteuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65400
---

posix_seteuid

Establecer el UID efectivo del proceso actual

## Descripción

```php
posix_seteuid(int $user_id): bool
```php

Establece el ID de usuario efectivo del proceso actual. Esta es una función privilegiada y se necesitan los permisos apropiados (usualmente root) en el sistema para tener la capacidad de ejecutar esta función.

## Parámetros

`user_id`  
El id de usuario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`posix_geteuid`, `posix_setuid`, `posix_getuid`
