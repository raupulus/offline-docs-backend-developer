---
title: posix_setuid
description: Establecer el UID del proceso actual
source_url: https://www.php.net/manual/es/function.posix-setuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-setuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 265acc36e
order: 65450
---

posix_setuid

Establecer el UID del proceso actual

## Descripción

```php
posix_setuid(int $user_id): bool
```php

Establece el ID real de usuario del proceso actual. Esta es una función privilegiada que necesita los privilegios apropiados (normalmente root) del sistema para que sea capaz de realizar esta función.

## Parámetros

`user_id`  
El id de usuario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `posix_setuid`

Este ejemplo mostrará el id de usuario actual y después lo establecerá a un valor diferente.

```
<?php
echo posix_getuid()."\n"; //10001
echo posix_geteuid()."\n"; //10001
posix_setuid(10000);
echo posix_getuid()."\n"; //10000
echo posix_geteuid()."\n"; //10000
?>

    
```php

## Véase también

`posix_setgid`, `posix_seteuid`, `posix_getuid`, `posix_geteuid`
