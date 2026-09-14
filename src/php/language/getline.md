---
title: Error::getLine
description: Obtener la línea en la que ocurrió el error
source_url: https://www.php.net/manual/es/error.getline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/getline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3190
---

Error::getLine

Obtener la línea en la que ocurrió el error

## Descripción

```php
final public Error::getLine(): int
```php

Obtiene el número de línea donde ocurrió el error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de línea en la que ocurrió el error.

## Ejemplos

Ejemplo de `Error::getLine`

```
<?php
try {
    throw new Error("Un mensaje de error");
} catch(Error $e) {
    echo "El error se ocasionó en la línea: " . $e->getLine();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    El error se ocasionó en la línea: 3

## Véase también

Throwable::getLine
