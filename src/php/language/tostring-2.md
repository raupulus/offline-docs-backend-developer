---
title: Exception::__toString
description: Representación de la excepción en formato cadena
source_url: https://www.php.net/manual/es/exception.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3380
---

Exception::\_\_toString

Representación de la excepción en formato cadena

## Descripción

```php
public Exception::__toString(): string
```php

Devuelve la representación de la excepción en formato `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación de la excepción en formato `string`.

## Ejemplos

Ejemplo de `Exception::__toString`

```
<?php
try {
    throw new Exception("Some error message");
} catch(Exception $e) {
    echo $e;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    exception 'Exception' with message 'Some error message' in /home/bjori/tmp/ex.php:3
    Stack trace:
    #0 {main}

## Véase también

Throwable::\_\_toString
