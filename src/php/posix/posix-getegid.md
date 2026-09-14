---
title: posix_getegid
description: Devuelve el ID efectivo de grupo del proceso actual
source_url: https://www.php.net/manual/es/function.posix-getegid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getegid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65170
---

posix_getegid

Devuelve el ID efectivo de grupo del proceso actual

## Descripción

```php
posix_getegid(): int
```php

Devuelve el ID efectivo de grupo efectivo numérico del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `int` del ID del grupo efectivo.

## Ejemplos

Ejemplo de `posix_getegid`

Este ejemplo imprimirá el id efectivo del grupo, una vez que es cambiado con `posix_setegid`.

```
<?php
echo 'Mi id del grupo real es '.posix_getgid(); //20
posix_setegid(40);
echo 'Mi id del grupo real es  '.posix_getgid(); //20
echo 'Mi id del grupo efectivo es  '.posix_getegid(); //40
?>

    
```php

## Notas

`posix_getegid` es diferente de `posix_getgid` ya que el ID efectivo del grupo se puede cambiar mediante una llamada al proceso usando `posix_setegid`.

## Véase también

`posix_getgrgid`, `posix_getgid`, `posix_setgid`
