---
title: debug_print_backtrace
description: Muestra la pila de ejecución de PHP
source_url: https://www.php.net/manual/es/function.debug-print-backtrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/debug-print-backtrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: false
translation_revision: 1fd69376c
order: 17600
---

debug_print_backtrace

Muestra la pila de ejecución de PHP

## Descripción

```php
debug_print_backtrace([int $options], [int $limit]): void
```php

`debug_print_backtrace` muestra la pila de ejecución de PHP. Muestra las llamadas a funciones, los ficheros incluidos/requeridos por `include`/`require` así como las llamadas a `eval`.

## Parámetros

`options`  
Este argumento es una máscara de las siguientes opciones:

|  |  |
|----|----|
| DEBUG_BACKTRACE_IGNORE_ARGS | Si se deben omitir el índice "args" y, por lo tanto, todos los argumentos del método/función para preservar la memoria. |

Opciones para `debug_print_backtrace`

`limit`  
Este argumento puede ser utilizado para limitar el número de marcos de la pila a mostrar. Por omisión (`limit`=`0`), todos los marcos de la pila serán mostrados.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `debug_print_backtrace`

```
<?php
// fichero include.php

function a() {
    b();
}

function b() {
    c();
}

function c(){
    debug_print_backtrace();
}

a();

?>

    
```php

```
<?php
// fichero test.php
// Este es el fichero que debe ser ejecutado

include 'include.php';
?>

    
```php

Resultado del ejemplo anterior es similar a:

    #0  c() called at [/tmp/include.php:10]
    #1  b() called at [/tmp/include.php:6]
    #2  a() called at [/tmp/include.php:17]
    #3  include(/tmp/include.php) called at [/tmp/test.php:3]

## Véase también

`debug_backtrace`
