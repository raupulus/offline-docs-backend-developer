---
title: Exception::getMessage
description: Obtiene el mensaje de Excepción
source_url: https://www.php.net/manual/es/exception.getmessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/getmessage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3340
---

Exception::getMessage

Obtiene el mensaje de Excepción

## Descripción

```php
final public Exception::getMessage(): string
```php

Devuelve el mensaje de Excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el mensaje de Excepción en formato cadena.

## Ejemplos

Ejemplo de `Exception::getMessage`

```
<?php
try {
    throw new Exception("Algún mensaje de error");
} catch(Exception $e) {
    echo $e->getMessage();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Algún mensaje de error

## Véase también

Throwable::getMessage
