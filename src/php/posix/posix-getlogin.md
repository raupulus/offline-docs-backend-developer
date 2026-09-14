---
title: posix_getlogin
description: Devuelve el nombre del inicio de sesión
source_url: https://www.php.net/manual/es/function.posix-getlogin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getlogin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65230
---

posix_getlogin

Devuelve el nombre del inicio de sesión

## Descripción

```php
posix_getlogin(): string
```php

Devuelve el nombre del inicio de sesión del usuario propietarios del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de inicio de sesión del usuario, como valor de tipo `string`, o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso de `posix_getlogin`

```
<?php
echo posix_getlogin(); //apache
?>

    
```php

## Véase también

`posix_getpwnam`, Página GETLOGIN(3) del man de POSIX
