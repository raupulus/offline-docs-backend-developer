---
title: ErrorException::getSeverity
description: Obtiene la severidad de la excepción
source_url: https://www.php.net/manual/es/errorexception.getseverity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/errorexception/getseverity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 09c49da6f
order: 3270
---

ErrorException::getSeverity

Obtiene la severidad de la excepción

## Descripción

```php
final public ErrorException::getSeverity(): int
```php

Devuelve la severidad de la excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nivel de la severidad de la excepción.

## Ejemplos

Ejemplo de `ErrorException::getSeverity`

```
<?php
try {
    throw new ErrorException("Mensaje de la excepción", 0, E_USER_ERROR);
} catch(ErrorException $e) {
    echo "La severidad de la excepción es: " . $e->getSeverity();
    var_dump($e->getSeverity() === E_USER_ERROR);
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    La severidad de la excepción es: 256
    bool(true)
