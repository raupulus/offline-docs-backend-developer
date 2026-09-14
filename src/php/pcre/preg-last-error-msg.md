---
title: preg_last_error_msg
description: Devuelve el mensaje de error de la última ejecución de regex PCRE
source_url: https://www.php.net/manual/es/function.preg-last-error-msg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-last-error-msg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: true
translation_revision: 3ec7b6131
order: 61590
---

preg_last_error_msg

Devuelve el mensaje de error de la última ejecución de regex PCRE

## Descripción

```php
preg_last_error_msg(): string
```php

Devuelve el mensaje de error de la última ejecución de regex PCRE.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el mensaje de error en caso de éxito, o `"No error"` si no se ha producido ningún error.

## Ejemplos

Ejemplo de `preg_last_error_msg`

```
<?php

preg_match('/(?:\D+|<\d+>)*[!?]/', 'foobar foobar foobar');

if (preg_last_error() !== PREG_NO_ERROR) {
    echo preg_last_error_msg();
}

?>

    
```php

El ejemplo anterior mostrará:

    Backtrack limit exhausted

## Véase también

`preg_last_error`
