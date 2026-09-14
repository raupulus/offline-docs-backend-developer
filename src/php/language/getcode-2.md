---
title: Exception::getCode
description: Obtiene el código de una excepción
source_url: https://www.php.net/manual/es/exception.getcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/getcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3310
---

Exception::getCode

Obtiene el código de una excepción

## Descripción

```php
final public Exception::getCode(): int
```php

Devuelve el código de una excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código de Excepción en forma de `int` en `Exception` pero posiblemente en forma de otros tipos en `Exception` descendientes (por ejemplo como `string` en `PDOException`).

## Ejemplos

Ejemplo de `Exception::getCode`

```
<?php
try {
    throw new Exception("Un mensaje de error", 30);
} catch(Exception $e) {
    echo "El código de excepción es: " . $e->getCode();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    El código de excepción es: 30

## Véase también

Throwable::getCode
