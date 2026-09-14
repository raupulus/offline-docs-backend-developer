---
title: Error::getTraceAsString
description: Obtener la traza de la pila como un string
source_url: https://www.php.net/manual/es/error.gettraceasstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/gettraceasstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3230
---

Error::getTraceAsString

Obtener la traza de la pila como un string

## Descripción

```php
final public Error::getTraceAsString(): string
```php

Devuelve la traza de la pila como un string.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la traza de la pila como un string.

## Ejemplos

Ejemplo de `Error::getTraceAsString`

```
<?php
function prueba() {
    throw new Error;
}

try {
    prueba();
} catch(Error $e) {
    echo $e->getTraceAsString();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    #0 /home/bjori/tmp/ex.php(7): prueba()
    #1 {main}

## Véase también

Throwable::getTraceAsString
