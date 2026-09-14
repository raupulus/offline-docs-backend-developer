---
title: Exception::getFile
description: Obtiene el fichero en el que se creó la excepción
source_url: https://www.php.net/manual/es/exception.getfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/getfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3320
---

Exception::getFile

Obtiene el fichero en el que se creó la excepción

## Descripción

```php
final public Exception::getFile(): string
```php

Obtiene el nombre del fichero en el que fue creada la excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del fichero en donde fue creada la excepción.

## Ejemplos

Ejemplo de `Exception::getFile`

```
<?php
try {
    throw new Exception;
} catch(Exception $e) {
    echo $e->getFile();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    /home/bjori/tmp/ex.php

## Véase también

Throwable::getFile
