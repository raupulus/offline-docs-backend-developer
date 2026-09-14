---
title: posix_getuid
description: Devolver el ID real de usuario del proceso actual
source_url: https://www.php.net/manual/es/function.posix-getuid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getuid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65320
---

posix_getuid

Devolver el ID real de usuario del proceso actual

## Descripción

```php
posix_getuid(): int
```php

Devuelve el ID real numérico de usuario del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el id de usuario, como valor de tipo `int`

## Ejemplos

Ejemplo de uso de `posix_getuid`

```
<?php
echo posix_getuid(); //10000
?>

    
```php

## Véase también

`posix_getpwuid`, Página GETUID(2) del man de POSIX
