---
title: xhprof_disable
description: Detiene el perfilado xhprof
source_url: https://www.php.net/manual/es/function.xhprof-disable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xhprof/functions/xhprof-disable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xhprof
translation_status: ready
translation_revision: a9220267e
order: 102310
---

xhprof_disable

Detiene el perfilado xhprof

## Descripción

```php
xhprof_disable(): array
```php

Detiene el perfilado y devuelve los datos xhprof correspondientes a su ejecución.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de datos xhprof, procedentes de su ejecución. Devuelve `null` si el perfilado no está activado.

## Ejemplos

Ejemplo con `xhprof_disable`

```
<?php
xhprof_enable();

$foo = strlen("foo bar");

$xhprof_data = xhprof_disable();

print_r($xhprof_data);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [main()==>strlen] => Array
            (
                [ct] => 1
                [wt] => 279
            )

        [main()==>xhprof_disable] => Array
            (
                [ct] => 1
                [wt] => 9
            )

        [main()] => Array
            (
                [ct] => 1
                [wt] => 610
            )

    )
