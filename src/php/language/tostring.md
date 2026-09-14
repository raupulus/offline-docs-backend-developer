---
title: Error::__toString
description: Representación de string del error
source_url: https://www.php.net/manual/es/error.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3240
---

Error::\_\_toString

Representación de string del error

## Descripción

```php
public Error::__toString(): string
```php

Devuelve la representación de `string` del error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la representación de `string` del error.

## Ejemplos

Ejemplo de `Error::__toString`

```
<?php
try {
    throw new Error("Un mensaje de error");
} catch(Error $e) {
    echo $e;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Error: Un mensaje de error in /home/bjori/tmp/ex.php:3
    Stack trace:
    #0 {main}

## Véase también

Throwable::\_\_toString
