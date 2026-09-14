---
title: posix_geteuid
description: Devolver el ID efectivo de usuario del proceso actual
source_url: https://www.php.net/manual/es/function.posix-geteuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-geteuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 65180
---

posix_geteuid

Devolver el ID efectivo de usuario del proceso actual

## Descripción

```php
posix_geteuid(): int
```php

Devuelve el ID efectivo numérico de usuario del proceso actual. Véase también `posix_getpwuid` para información sobre cómo convertirlo en un nombre de usuario utilizable.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el id de usuario, como un valor de tipo `int`

## Ejemplos

Ejemplo de `posix_geteuid`

Este ejemplo mostrará el id del usuario actual y establecerá el id efectivo de usuario en un id aparte usando `posix_seteuid`, luego mostrará la diferencia entre el id real y el id efectivo.

```
<?php
echo posix_getuid()."\n"; //10001
echo posix_geteuid()."\n"; //10001
posix_seteuid(10000);
echo posix_getuid()."\n"; //10001
echo posix_geteuid()."\n"; //10000
?>

    
```php

## Véase también

`posix_getpwuid`, `posix_getuid`, `posix_setuid`, Página GETEUID(2) del man de POSIX
