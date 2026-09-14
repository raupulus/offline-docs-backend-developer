---
title: ibase_modify_user
description: Modifica un usuario en una base de datos de seguridad
source_url: https://www.php.net/manual/es/function.ibase-modify-user.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-modify-user.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30410
---

ibase_modify_user

Modifica un usuario en una base de datos de seguridad

## Descripción

```php
ibase_modify_user(resource $service_handle, string $user_name, string $password, [string $first_name], [string $middle_name], [string $last_name]): bool
```php

## Parámetros

`service_handle`  
El gestor sobre el servicio del servidor de base de datos.

`user_name`  
El identificador del usuario de base de datos a modificar.

`password`  
La nueva contraseña del usuario.

`first_name`  
El nuevo nombre del usuario.

`middle_name`  
El nuevo segundo nombre del usuario.

`last_name`  
El nuevo apellido del usuario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_add_user

ibase_delete_user
