---
title: Exception::getTraceAsString
description: Obtiene la traza de la pila como una cadena de caracteres
source_url: https://www.php.net/manual/es/exception.gettraceasstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/gettraceasstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 09c49da6f
order: 3370
---

Exception::getTraceAsString

Obtiene la traza de la pila como una cadena de caracteres

## Descripción

```php
final public Exception::getTraceAsString(): string
```php

Devuelve la traza de la pila de una excepción como una cadena de caracteres.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la traza de la pila de la excepción como una cadena de caracteres.

## Ejemplos

Ejemplo de `Exception::getTraceAsString`

```
<?php
function test() {
    throw new Exception;
}

try {
    test();
} catch(Exception $e) {
    echo $e->getTraceAsString();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    #0 /home/bjori/tmp/ex.php(7): test()
    #1 {main}

## Véase también

Throwable::getTraceAsString
