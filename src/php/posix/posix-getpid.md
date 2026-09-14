---
title: posix_getpid
description: Devolver el identificador del proceso actual
source_url: https://www.php.net/manual/es/function.posix-getpid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getpid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65260
---

posix_getpid

Devolver el identificador del proceso actual

## Descripción

```php
posix_getpid(): int
```php

Devolver el identificador de proceso del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador, como valor de tipo `int`.

## Ejemplos

Ejemplo de uso de `posix_getpid`

```
<?php
echo posix_getpid(); //8805
?>

    
```php

## Véase también

`posix_kill`, Página GETPID(2) del man de POSIX
