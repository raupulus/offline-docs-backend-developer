---
title: posix_initgroups
description: Calcular la lista de acceso al grupo
source_url: https://www.php.net/manual/es/function.posix-initgroups.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-initgroups.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65330
---

posix_initgroups

Calcular la lista de acceso al grupo

## Descripción

```php
posix_initgroups(string $username, int $group_id): bool
```php

Calcula la lista de acceso al grupo para el usuario especificado en el parámetro name.

## Parámetros

`username`  
El usuario para el que se va a calcular la lista.

`group_id`  
Normalmente el número de grupo del fichero de contraseñas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

La página del manua Unix para initgroups(3).
