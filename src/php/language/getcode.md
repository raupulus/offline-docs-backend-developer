---
title: Error::getCode
description: Obtener el código de error
source_url: https://www.php.net/manual/es/error.getcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/getcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3170
---

Error::getCode

Obtener el código de error

## Descripción

```php
final public Error::getCode(): int
```php

Devuelve el código de error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el código de error como un `int`

## Ejemplos

Ejemplo de `Error::getCode`

```
<?php
try {
    throw new Error("Un mensaje de error", 30);
} catch(Error $e) {
    echo "El código del Error es: " . $e->getCode();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    El código del Error es: 30

## Véase también

Throwable::getCode
