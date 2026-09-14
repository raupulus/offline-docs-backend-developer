---
title: posix_getppid
description: Devolver el identificador del proceso padre
source_url: https://www.php.net/manual/es/function.posix-getppid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getppid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65270
---

posix_getppid

Devolver el identificador del proceso padre

## Descripción

```php
posix_getppid(): int
```php

Devuelve el identificador de proceso del proceso padre del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador, como valor de tipo `int`.

## Ejemplos

Ejemplo de uso de `posix_getppid`

```
<?php
echo posix_getppid(); //8259
?>

    
```php
