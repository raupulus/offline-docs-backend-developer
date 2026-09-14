---
title: ibase_delete_user
description: Elimina un usuario de una base de datos de seguridad
source_url: https://www.php.net/manual/es/function.ibase-delete-user.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-delete-user.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30270
---

ibase_delete_user

Elimina un usuario de una base de datos de seguridad

## Descripción

```php
ibase_delete_user(resource $service_handle, string $user_name): bool
```php

## Parámetros

`service_handle`  
El gestor sobre el servicio del servidor de la base de datos.

`user_name`  
El identificador del usuario que debe ser eliminado de la base de datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_add_user

ibase_modify_user
