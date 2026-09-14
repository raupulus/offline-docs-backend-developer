---
title: Exception::getTrace
description: Obtiene la traza de la pila
source_url: https://www.php.net/manual/es/exception.gettrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/gettrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3360
---

Exception::getTrace

Obtiene la traza de la pila

## Descripción

```php
final public Exception::getTrace(): array
```php

Devuelve la traza de pila de una excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el seguimiento de pila de una excepción como un `array`.

## Ejemplos

Ejemplo de `Exception::getTrace`

```
<?php
function test() {
 throw new Exception;
}

try {
 test();
} catch(Exception $e) {
 var_dump($e->getTrace());
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [0]=>
      array(4) {
        ["file"]=>
        string(22) "/home/bjori/tmp/ex.php"
        ["line"]=>
        int(7)
        ["function"]=>
        string(4) "test"
        ["args"]=>
        array(0) {
        }
      }
    }

## Véase también

Throwable::getTrace
