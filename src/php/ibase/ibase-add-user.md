---
title: ibase_add_user
description: Añade un usuario a una base de datos de seguridad
source_url: https://www.php.net/manual/es/function.ibase-add-user.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-add-user.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30100
---

ibase_add_user

Añade un usuario a una base de datos de seguridad

## Descripción

```php
ibase_add_user(resource $service_handle, string $user_name, string $password, [string $first_name], [string $middle_name], [string $last_name]): bool
```php

## Parámetros

`service_handle`  
El gestor sobre el servicio del servidor de la base de datos.

`user_name`  
El identificador para el nuevo usuario de la base de datos.

`password`  
La contraseña para el nuevo usuario.

`first_name`  
El nombre para el nuevo usuario de la base de datos.

`middle_name`  
El segundo nombre para el nuevo usuario de la base de datos.

`last_name`  
El apellido para el nuevo usuario de la base de datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

ibase_modify_user

ibase_delete_user
