---
title: pg_change_password
description: Cambia la contraseña de un usuario de PostgreSQL
source_url: https://www.php.net/manual/es/function.pg-change-password.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-change-password.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 491bd06bf
order: 62870
---

pg_change_password

Cambia la contraseña de un usuario de PostgreSQL

## Descripción

```php
pg_change_password(PgSql\Connection $connection, string $user, string $password): bool
```php

`pg_change_password` cambia la contraseña de un usuario de PostgreSQL. Esta función utiliza la función de libpq `PQchangePassword`, que gestiona el cifrado de la contraseña automáticamente según la configuración del servidor.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`user`  
El nombre del usuario de PostgreSQL cuya contraseña se va a cambiar.

`password`  
La nueva contraseña.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

pg_connect
