---
title: Error::getMessage
description: Obtener el mensaje de error
source_url: https://www.php.net/manual/es/error.getmessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/getmessage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3200
---

Error::getMessage

Obtener el mensaje de error

## Descripción

```php
final public Error::getMessage(): string
```php

Devuelve el mensaje de error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el mensaje de error como una cadena.

## Ejemplos

Ejemplo de `Error::getMessage`

```
<?php
try {
    throw new Error("Un mensaje de error");
} catch(Error $e) {
    echo $e->getMessage();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Un mensaje de error

## Véase también

Throwable::getMessage
