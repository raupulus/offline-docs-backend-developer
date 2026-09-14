---
title: Exception::getLine
description: Obtiene la línea en el que se creó la excepción
source_url: https://www.php.net/manual/es/exception.getline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/getline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3330
---

Exception::getLine

Obtiene la línea en el que se creó la excepción

## Descripción

```php
final public Exception::getLine(): int
```php

Devuelve el número de la línea donde se creó la excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de la línea donde se creó la excepción.

## Ejemplos

Ejemplo de `Exception::getLine`

```
<?php
try {
    throw new Exception("Algún mensaje de error");
} catch(Exception $e) {
    echo "La excepción se creó en la línea: " . $e->getLine();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    La excepción se creó en la línea: 3

## Véase también

Throwable::getLine
