---
title: posix_getgid
description: Devuelve el ID real de grupo del proceso actual
source_url: https://www.php.net/manual/es/function.posix-getgid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getgid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65190
---

posix_getgid

Devuelve el ID real de grupo del proceso actual

## Descripción

```php
posix_getgid(): int
```php

Devuelve el ID real numérico de grupo del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el id real de grupo, como un valor de tipo `int`.

## Ejemplos

Ejemplo de `posix_getgid`

Este ejemplo imprimirá el id real de grupo, incluso una vez que el id efectivo de grupo ha sido cambiado.

```
<?php
echo 'Mi id real de grupo es '.posix_getgid(); //20
posix_setegid(40);
echo 'Mi id real de grupo es '.posix_getgid(); //20
echo 'Mi id efectivo de grupo es '.posix_getegid(); //40
?>

    
```php

## Véase también

`posix_getgrgid`, `posix_getegid`, `posix_setgid`, Página GETGID(2) del man de POSIX
