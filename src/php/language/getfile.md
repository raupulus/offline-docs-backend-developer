---
title: Error::getFile
description: Obtener el fichero en el que ocurrío el error
source_url: https://www.php.net/manual/es/error.getfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/getfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3180
---

Error::getFile

Obtener el fichero en el que ocurrío el error

## Descripción

```php
final public Error::getFile(): string
```php

Obtiene el nombre del fichero donde ocurrió el error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero el en cual ocurrió el error.

## Ejemplos

Ejemplo de `Error::getFile`

```
<?php
try {
    throw new Error;
} catch(Error $e) {
    echo $e->getFile();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    /home/bjori/tmp/ex.php

## Véase también

Throwable::getFile
