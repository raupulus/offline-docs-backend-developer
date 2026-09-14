---
title: Error::getTrace
description: Obtener la traza de la pila
source_url: https://www.php.net/manual/es/error.gettrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/gettrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3220
---

Error::getTrace

Obtener la traza de la pila

## Descripción

```php
final public Error::getTrace(): array
```php

Devuelve la traza de la pila.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la traza de la pila como un `array`.

## Ejemplos

Ejemplo de `Error::getTrace`

```
<?php
function prueba() {
 throw new Error;
}

try {
 prueba();
} catch(Error $e) {
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
        string(6) "prueba"
        ["args"]=>
        array(0) {
        }
      }
    }

## Véase también

Throwable::getTrace
