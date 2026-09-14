---
title: error_clear_last
description: Elimina el error más reciente
source_url: https://www.php.net/manual/es/function.error-clear-last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/error-clear-last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 1de948e93
order: 17610
---

error_clear_last

Elimina el error más reciente

## Descripción

```php
error_clear_last(): void
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Elimina el error más reciente, haciéndolo irrecuperable con `error_get_last`.

## Ejemplos

Un ejemplo de `error_clear_last`

```
<?php
var_dump(error_get_last());
error_clear_last();
var_dump(error_get_last());

@$a = $b;

var_dump(error_get_last());
error_clear_last();
var_dump(error_get_last());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    NULL
    NULL
    array(4) {
      ["type"]=>
      int(8)
      ["message"]=>
      string(21) "Undefined variable: b"
      ["file"]=>
      string(9) "%s"
      ["line"]=>
      int(6)
    }
    NULL

## Véase también

[Constantes de errores](#errorfunc.constants)
