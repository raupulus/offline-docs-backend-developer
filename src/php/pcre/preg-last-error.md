---
title: preg_last_error
description: Devuelve el código de error de la última expresión PCRE ejecutada
source_url: https://www.php.net/manual/es/function.preg-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: 3c68e46ce
order: 61600
---

preg_last_error

Devuelve el código de error de la última expresión PCRE ejecutada

## Descripción

```php
preg_last_error(): int
```php

Devuelve el código de error de la última expresión regular PCRE ejecutada.

Ejemplo con `preg_last_error`

```
<?php

preg_match('/(?:\D+|<\d+>)*[!?]/', 'foobar foobar foobar');

if (preg_last_error() == PREG_BACKTRACK_LIMIT_ERROR) {
    echo '¡Se ha agotado el límite de retroceso!';
}

?>

    
```php

El ejemplo anterior mostrará:

    Backtrack limit was exhausted!

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una de las siguientes constantes ([explicadas en esta página](#pcre.constants)): `PREG_NO_ERROR`, `PREG_INTERNAL_ERROR`, `PREG_BACKTRACK_LIMIT_ERROR` (ver también [pcre.backtrack_limit](#ini.pcre.backtrack-limit)), `PREG_RECURSION_LIMIT_ERROR` (ver también [pcre.recursion_limit](#ini.pcre.recursion-limit)), `PREG_BAD_UTF8_ERROR`, `PREG_BAD_UTF8_OFFSET_ERROR`, `PREG_JIT_STACKLIMIT_ERROR`

## Véase también

`preg_last_error_msg`
