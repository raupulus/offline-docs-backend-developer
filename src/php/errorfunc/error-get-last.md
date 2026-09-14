---
title: error_get_last
description: Obtener el último error que ocurrió
source_url: https://www.php.net/manual/es/function.error-get-last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/error-get-last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 1de948e93
order: 17620
---

error_get_last

Obtener el último error que ocurrió

## Descripción

```php
error_get_last(): array
```php

Obtiene información sobre el último error que ocurrió.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una matriz asociativa describiendo el último error con las claves "type" (tipo), "message" (mensaje), "file" (archivo) y "line" (línea). Si el error ha sido causado por una función interna de PHP, el "message" (mensaje) comienza con su nombre. Devuelve `null` si no ha habido aún un error.

## Ejemplos

Un ejemplo de `error_get_last`

```
<?php
echo $a;
print_r(error_get_last());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [type] => 8
        [message] => Undefined variable: a
        [file] => C:\WWW\index.php
        [line] => 2
    )

## Véase también

[Constantes de error](#errorfunc.constants), La variable `$php_errormsg`, `error_clear_last`, [La directiva `display_errors`](#ini.display-errors), [La directiva `html_errors`](#ini.html-errors), [La directiva `xmlrpc_errors`](#ini.xmlrpc-errors)
